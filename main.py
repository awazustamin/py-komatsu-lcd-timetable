import pygame
import sys

#サイズと初期表示倍率
BASE_RES = (1920, 1080)
INITIAL_SCALE = 0.5
FONT_NAME = "meiryo"

#色の定義
COLOR_BG = (0, 0, 0)
COLOR_TEXT = (255, 255, 255)

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

    #メインループ
    while True:
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

        #1段目種別の図形
        pygame.draw.rect(canvas, (255, 255, 255), (0, 136, 242, 135))

        #1段目種別の図形の枠
        pygame.draw.rect(canvas, (0, 176, 80), (3, 139, 236, 129))

        #2段目種別の図形
        pygame.draw.rect(canvas, (255, 255, 255), (0, 271, 242, 135))

        #2段目種別の図形の枠
        pygame.draw.rect(canvas, (0, 176, 80), (3, 274, 236, 129))

        #3段目種別の図形
        pygame.draw.rect(canvas, (255, 255, 255), (0, 406, 242, 135))

        #3段目種別の図形の枠
        pygame.draw.rect(canvas, (0, 176, 80), (3, 409, 236, 129))

        #方面を表示するところの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 540, 1920, 102))

        #種別等が書いてあるところのバーの図形
        pygame.draw.rect(canvas, (53, 58, 65), (0, 644, 1920, 32))

        #フォント設定
        main_font = pygame.font.SysFont(FONT_NAME, 80, bold=False)
        rosen1 = pygame.font.SysFont(FONT_NAME, 68, bold=False)
        syousai = pygame.font.SysFont(FONT_NAME, 19, bold=False)

        #路線名
        rosen = rosen1.render("IRいしかわ鉄道線", True, COLOR_TEXT)
        canvas.blit(rosen, (53, 7))

        #方面
        houmen = rosen1.render("加賀温泉・福井方面", True, COLOR_TEXT)
        canvas.blit(houmen, (961, 7))

        #1段目種別
        text_surf1 = main_font.render("普通", True, COLOR_TEXT)
        canvas.blit(text_surf1, (121 - text_surf1.get_width() // 2, 203 - text_surf1.get_height() // 2))

        #2段目種別
        text_surf2 = main_font.render("普通", True, COLOR_TEXT)
        canvas.blit(text_surf2, (121 - text_surf2.get_width() // 2, 338 - text_surf2.get_height() // 2))

        #3段目種別
        text_surf3 = main_font.render("普通", True, COLOR_TEXT)
        canvas.blit(text_surf3, (121 - text_surf3.get_width() // 2, 473 - text_surf3.get_height() // 2))

        #ケーリングと画面更新
        #キャンバスを現在のウィンドウサイズに合わせて転送
        scaled_frame = pygame.transform.scale(canvas, win_size)
        screen.blit(scaled_frame, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()