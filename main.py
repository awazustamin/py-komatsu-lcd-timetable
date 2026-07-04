import pygame
import sys
import argparse
import json
import requests
import os
from datetime import datetime, timezone, timedelta

# サイズと初期表示倍率
BASE_RES = (1920, 1080)
INITIAL_SCALE = 0.5
FONT_NAME = "meiryo"

# 色の定義
COLOR_BG = (0, 0, 0)
COLOR_TEXT = (255, 255, 255)
YELLOW_TEXT = (246, 255, 224)
COLOR_NORMAL = (83, 188, 97)
COLOR_KAISOKU = (245, 198, 74)

API_URL = "https://www.ishikawa-railway.jp/api/v1/timetables/station/komatsu"
JSON_FILE = "komatsu.json"

parser = argparse.ArgumentParser(
    description="IRいしかわ鉄道 小松駅LCD発車標"
)

parser.add_argument(
    "--debug",
    action="store_true",
    help="デバッグモードを有効にする"
)

parser.add_argument(
    "--file",
    default="komatsu.json",
    metavar="FILE",
    help="読み込むJSONファイルを指定します（デフォルト: komatsu.json）"
)

args = parser.parse_args()

debug_offset = 0

DEBUG_MODE = args.debug
JSON_FILE = args.file

def setup_display(width):
    height = int(width * (BASE_RES[1] / BASE_RES[0]))
    size = (width, height)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen, size

def fetch_api():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
    except:
        pass

def get_train_list(offset_min=0):
    if not os.path.exists(JSON_FILE):
        return [{"time":"--：--","dest_jp":"----","dest_en":"","plat":"-","type_jp":"--","type_en":""}]*3, \
               [{"time":"--：--","dest_jp":"----","dest_en":"","plat":"-","type_jp":"--","type_en":""}]*3

    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        JST = timezone(timedelta(hours=+9))
        now = datetime.now(JST) + timedelta(minutes=offset_min)
        now_str = now.strftime("%H:%M")

        f_res, k_res = [], []

        for d in data['directions']:
            is_f = "福井" in d['name']

            trains = []
            old_trains = []

            for entry in d['timetables']:
                for t in entry['diagrams']:
                    raw_time = t['departure_time']

                    # 時刻の整形
                    h, m = raw_time.split(":")
                    h_str = f"{int(h):2}".replace(" ", "\u2007")
                    display_time = f"{h_str}：{m.zfill(2)}"

                    dest = t['arrival_station_name']
                    if len(dest) == 2:
                        dest = f"{dest[0]}　{dest[1]}"

                    train = {
                        "sort_key": raw_time.zfill(5),
                        "time": display_time,
                        "dest_jp": dest,
                        "dest_en": t['arrival_station_name_en'],
                        "plat": str(t.get('platform') or ("3" if is_f else "1")),
                        "type_jp": t['train_type_name'] or "普通",
                        "type_en": t['train_type_name_en'] or "Local"
                    }

                    if raw_time.zfill(5) >= now_str:
                        trains.append(train)
                    else:
                        old_trains.append(train)

            trains = sorted(trains, key=lambda x: x['sort_key'])

            # 3本未満なら始発から補充
            if len(trains) < 3:
                old_trains = sorted(old_trains, key=lambda x: x['sort_key'])
                trains.extend(old_trains[:3 - len(trains)])

            sorted_t = trains[:3]

            while len(sorted_t) < 3:
                empty_time = "\u2007 \u2007：\u2007 \u2007"
                sorted_t.append({
                    "time": empty_time,
                    "dest_jp": "      ",
                    "dest_en": "",
                    "plat": " ",
                    "type_jp": "    ",
                    "type_en": ""
                })

            if is_f:
                f_res = sorted_t
            else:
                k_res = sorted_t

        return f_res, k_res

    except:
        return [{"time":"--：--","dest_jp":"----","dest_en":"","plat":"-","type_jp":"--","type_en":""}]*3, \
               [{"time":"--：--","dest_jp":"----","dest_en":"","plat":"-","type_jp":"--","type_en":""}]*3

def main():
    global debug_offset
    pygame.init()
    current_w = int(BASE_RES[0] * INITIAL_SCALE)
    screen, win_size = setup_display(current_w)
    pygame.display.set_caption("")

    canvas = pygame.Surface(BASE_RES)
    clock = pygame.time.Clock()

    if JSON_FILE == "komatsu.json":
        fetch_api()

    f_list, k_list = get_train_list(debug_offset)
    last_update = pygame.time.get_ticks()

    while True:
        now_ticks = pygame.time.get_ticks()
        if now_ticks - last_update > 3600000:
            if JSON_FILE == "komatsu.json":
                fetch_api()

            f_list, k_list = get_train_list(debug_offset)
            last_update = now_ticks

        current_time_cycle = now_ticks % 12000
        is_japanese = current_time_cycle < 8000

        if is_japanese:
            txt_rosen, txt_houmen1, txt_houmen2 = "IRいしかわ鉄道線", "加賀温泉・福井方面", "松任・金沢方面"
            txt_delay, txt_time, txt_destination, txt_platform = "列車名／遅れ", "時刻", "行先", "のりば"
        else:
            txt_rosen, txt_houmen1, txt_houmen2 = "Ishikawa Railway", "for Kagaonsen, Fukui", "for Mattō, Kanazawa"
            txt_delay, txt_time, txt_destination, txt_platform = "Train Name/Delay", "Departure Time", "Destination", "Platform"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen, win_size = setup_display(event.w)
            elif event.type == pygame.KEYDOWN and DEBUG_MODE:
                if event.key == pygame.K_b: debug_offset += 10
                elif event.key == pygame.K_n: debug_offset += 60
                elif event.key == pygame.K_g: debug_offset -= 10
                elif event.key == pygame.K_h: debug_offset -= 60
                f_list, k_list = get_train_list(debug_offset)

        canvas.fill(COLOR_BG)

        # 背景ヘッダー
        pygame.draw.rect(canvas, (53, 58, 65), (0, 0, 1920, 102))
        pygame.draw.rect(canvas, (53, 58, 65), (0, 104, 1920, 32))
        pygame.draw.rect(canvas, (53, 58, 65), (0, 540, 1920, 102))
        pygame.draw.rect(canvas, (53, 58, 65), (0, 644, 1920, 32))

        main_font = pygame.font.SysFont(FONT_NAME, 80)
        rosen_f = pygame.font.SysFont(FONT_NAME, 68)
        syousai_f = pygame.font.SysFont(FONT_NAME, 19)

        # 路線・方面
        r_s = rosen_f.render(txt_rosen, True, COLOR_TEXT)
        canvas.blit(r_s, (53, 51 - r_s.get_height() // 2))
        canvas.blit(r_s, (53, 591 - r_s.get_height() // 2))
        h1 = rosen_f.render(txt_houmen1, True, COLOR_TEXT); canvas.blit(h1, (965, 51 - r_s.get_height() // 2))
        h2 = rosen_f.render(txt_houmen2, True, COLOR_TEXT); canvas.blit(h2, (963, 591 - r_s.get_height() // 2))

        # ヘッダーテキスト
        for by in [120, 660]:
            for tx, px in [(txt_time, 117), (txt_delay, 598), (txt_time, 1162), (txt_destination, 1480), (txt_platform, 1826)]:
                s = syousai_f.render(tx, True, COLOR_TEXT)
                canvas.blit(s, (px - s.get_width() // 2, by - s.get_height() // 2))

        # 列車データ描画
        for i in range(3):
            for lst, y_base, y_rect_base in [(f_list, [203, 338, 473], [136, 271, 406]), 
                                             (k_list, [744, 879, 1014], [677, 812, 947])]:
                train = lst[i]
                yc = y_base[i]
                yr = y_rect_base[i]

                # 快速判定による背景色変更 (#ff7f00)
                current_rect_color = COLOR_KAISOKU if train["type_jp"] == "快速" else COLOR_NORMAL
                
                pygame.draw.rect(canvas, (255, 255, 255), (0, yr, 242, 135))
                pygame.draw.rect(canvas, current_rect_color, (3, yr + 3, 236, 129))

                # 描画 (121, 1140, 1480, 1825 の座標は完全維持)
                s_s = main_font.render(train["type_jp"] if is_japanese else train["type_en"], True, COLOR_TEXT)
                canvas.blit(s_s, (121 - s_s.get_width() // 2, yc - s_s.get_height() // 2))
                
                # 時刻 (特殊空白により「：」の位置は常に固定)
                t_s = main_font.render(train["time"], True, YELLOW_TEXT)
                canvas.blit(t_s, (1140 - t_s.get_width() // 2, yc - t_s.get_height() // 2))
                
                d_s = main_font.render(train["dest_jp"] if is_japanese else train["dest_en"], True, COLOR_TEXT)
                canvas.blit(d_s, (1480 - d_s.get_width() // 2, yc - d_s.get_height() // 2))
                
                p_s = main_font.render(train["plat"], True, YELLOW_TEXT)
                canvas.blit(p_s, (1825 - p_s.get_width() // 2, yc - p_s.get_height() // 2))

        screen.blit(pygame.transform.smoothscale(canvas, win_size), (0, 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()