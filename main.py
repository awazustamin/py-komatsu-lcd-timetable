from time import sleep
import pygame
import sys

#サイズと初期表示倍率
BASE_RES = (1920, 1080)
INITIAL_SCALE = 0.5
FONT_NAME = "meiryo"

#色の定義
COLOR_BG = (0, 0, 0)
COLOR_TEXT = (255, 255, 255)
YELLOW_TEXT = (255, 253, 157)

def setup_display(width):
    #横幅を基準に16:9のウィンドウを作成する
    height = int(width * (BASE_RES[1] / BASE_RES[0]))
    size = (width, height)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen, size

def main():
    pygame.init()

    #初期ウィンドウとキャンバスの準備
    current_w = int(BASE_RES[0] * INITIAL_SCALE)
    screen, win_size = setup_display(current_w)
    pygame.display.set_caption("")

    canvas = pygame.Surface(BASE_RES)
    
    #リソースの読み込み
    title_font = pygame.font.SysFont(FONT_NAME, 80, bold=True)
    clock = pygame.time.Clock()

    CYCLE_MS = 12000 
    JP_DURATION = 8000

    #メインループ
    while True:

        #現在のサイクル内の時間を計算
        current_time = pygame.time.get_ticks() % CYCLE_MS
        is_japanese = current_time < JP_DURATION

        #日英文面の定義
        if is_japanese:
            txt_local = "普通"
            txt_rosen = "IRいしかわ鉄道線"
            txt_houmen1 = "加賀温泉・福井方面"
            txt_houmen2 = "松任・金沢方面"
            txt_type = "種別"
            txt_delay = "列車名／遅れ"
            txt_time = "時刻"
            txt_destination = "行先"
            txt_platform = "のりば"
        else:
            txt_local = "Local"
            txt_rosen = "Ishikawa Railway"
            txt_houmen1 = "for Kagaonsen, Fukui"
            txt_houmen2 = "for Mattō, Kanazawa"
            txt_type = "Type"
            txt_delay = "Train Name/Delay"
            txt_time = "Departure Time"
            txt_destination = "Destination"
            txt_platform = "Platform"



        #種別の色定義
        color_syubetsu = (0, 176, 80)

        #イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.VIDEORESIZE:
                #リサイズ時にアスペクト比を維持して再生成
                screen, win_size = setup_display(event.w)

        #描画処理（1920x1080のキャンバスに対して行う）
        canvas.fill(COLOR_BG)
        
        #pygame.draw.rect(描画先, 色, (x, y, 幅, 高さ))

        #方面を表示するところの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 0, 1920, 102))

        #種別等が書いてあるところのバーの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 104, 1920, 32))

        #1段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 136, 242, 135))

        #1段目種別の図形
        pygame.draw.rect(canvas, color_syubetsu, (3, 139, 236, 129))

        #2段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 271, 242, 135))

        #2段目種別の図形
        pygame.draw.rect(canvas, color_syubetsu, (3, 274, 236, 129))

        #3段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 406, 242, 135))

        #3段目種別の図形
        pygame.draw.rect(canvas, (0, 176, 80), (3, 409, 236, 129))

        #方面を表示するところの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 540, 1920, 102))

        #種別等が書いてあるところのバーの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 644, 1920, 32))

        #4段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 677, 242, 135))

        #4段目種別の図形
        pygame.draw.rect(canvas, color_syubetsu, (3, 680, 236, 129))

        #5段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 812, 242, 135))

        #5段目種別の図形
        pygame.draw.rect(canvas, color_syubetsu, (3, 815, 236, 129))

        #6段目種別の図形の枠
        pygame.draw.rect(canvas, (255, 255, 255), (0, 947, 242, 135))

        #6段目種別の図形
        pygame.draw.rect(canvas, color_syubetsu, (3, 950, 236, 129))

        #フォント設定
        main_font = pygame.font.SysFont(FONT_NAME, 80, bold=False)
        rosen1 = pygame.font.SysFont(FONT_NAME, 68, bold=False)
        syousai = pygame.font.SysFont(FONT_NAME, 19, bold=False)

        #路線名
        rosen = rosen1.render(txt_rosen, True, COLOR_TEXT)
        canvas.blit(rosen, (53, 51 - rosen.get_height() // 2))
        canvas.blit(rosen, (53, 591 - rosen.get_height() // 2))

        #方面
        houmen = rosen1.render(txt_houmen1, True, COLOR_TEXT)
        canvas.blit(houmen, (961, 51 - rosen.get_height() // 2))

        houmen1 = rosen1.render(txt_houmen2, True, COLOR_TEXT)
        canvas.blit(houmen1, (961, 591 - rosen.get_height() // 2))

        #詳細
        type = syousai.render(txt_time, True, COLOR_TEXT)
        canvas.blit(type, (117 - type.get_width() // 2, 120 - type.get_height() // 2))
        canvas.blit(type, (117 - type.get_width() // 2, 660 - type.get_height() // 2))

        delay = syousai.render(txt_delay, True, COLOR_TEXT)
        canvas.blit(delay, (598 - delay.get_width() // 2, 120 - delay.get_height() // 2))
        canvas.blit(delay, (598 - delay.get_width() // 2, 660 - delay.get_height() // 2))

        time = syousai.render(txt_time, True, COLOR_TEXT)
        canvas.blit(time, (1162 - time.get_width() // 2, 120 - time.get_height() // 2))
        canvas.blit(time, (1162 - time.get_width() // 2, 660 - time.get_height() // 2))

        yukisaki = syousai.render(txt_destination, True, COLOR_TEXT)
        canvas.blit(yukisaki, (1511 - yukisaki.get_width() // 2, 120 - yukisaki.get_height() // 2))
        canvas.blit(yukisaki, (1511 - yukisaki.get_width() // 2, 660 - yukisaki.get_height() // 2))

        platform = syousai.render(txt_platform, True, COLOR_TEXT)
        canvas.blit(platform, (1826 - platform.get_width() // 2, 120 - platform.get_height() // 2))
        canvas.blit(platform, (1826 - platform.get_width() // 2, 660 - platform.get_height() // 2))

        #1段目種別
        text_surf1 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf1, (121 - text_surf1.get_width() // 2, 203 - text_surf1.get_height() // 2))

        #1段目時刻
        text_time1 = main_font.render("16：53", True, YELLOW_TEXT)
        canvas.blit(text_time1, (995, 203 - text_time1.get_height() // 2))

        #2段目種別
        text_surf2 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf2, (121 - text_surf2.get_width() // 2, 338 - text_surf2.get_height() // 2))

        #3段目種別
        text_surf3 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf3, (121 - text_surf3.get_width() // 2, 473 - text_surf3.get_height() // 2))

        #4段目種別
        text_surf4 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf4, (121 - text_surf4.get_width() // 2, 744 - text_surf4.get_height() // 2))

        #5段目種別
        text_surf5 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf5, (121 - text_surf5.get_width() // 2, 879 - text_surf5.get_height() // 2))

        #6段目種別
        text_surf6 = main_font.render(txt_local, True, COLOR_TEXT)
        canvas.blit(text_surf6, (121 - text_surf6.get_width() // 2, 1014 - text_surf6.get_height() // 2))

        #ケーリングと画面更新
        #キャンバスを現在のウィンドウサイズに合わせて転送
        scaled_frame = pygame.transform.smoothscale(canvas, win_size)
        screen.blit(scaled_frame, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()