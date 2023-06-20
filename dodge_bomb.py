import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900

moving = {
    pg.K_UP: (0, -5), 
    pg.K_DOWN: (0, +5), 
    pg.K_LEFT: (-5, 0), 
    pg.K_RIGHT: (+5, 0)
}


def collision(obj: pg.Rect) -> tuple[bool, bool]:
    """
    
    オブジェクトが画面内にいるかいないかを判定する関数
    引数2 obj : オブジェクトsurfaceのRect
    戻り値 : 横、縦方向のはみ出し判定(画面内：True, 画面外：False)
    """
    yoko, tate = True, True
    if (obj.left < 0) or (WIDTH < obj.right):
        yoko = False
    if (obj.top < 0) or (HEIGHT < obj.bottom):
        tate = False
    return yoko, tate


def main():
    tmr = 0
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img_1 = pg.image.load("ex02/fig/0.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)  # 爆弾用の乱数、x軸
    y = random.randint(0, HEIGHT)  # 爆弾用の乱数、y軸
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y  # 練習２
    vx, vy = +5, +5  #練習２
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock() 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bb_rct):
            kk_img = kk_img_1  # 59行目までゲームオーバー時の画像変更(未完成)
            kk_rct = kk_img.get_rect()
            kk_rct.center = 900, 400
            screen.blit(kk_img, kk_rct)
            tmr_ex = tmr  #64行目まで爆弾激突後の画面表示処理
            while(tmr_ex > tmr -150):
                tmr += 1
                clock.tick(50)
                continue
            print("ゲームオーバー")
            return
        
        key_lst = pg.key.get_pressed()  #74行目までキーボード入力に応じたこうかとんの移動処理
        sum_mv = [0, 0]
        for k, mv in moving.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        if collision(kk_rct) != (True, True):  # ここから77行目までこうかとんが画面外に出ないようにする処理
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)  #  練習２
        yoko, tate = collision(bb_rct)
        if not yoko:  # 爆弾が横にはみでたら
            vx *= -1
        if not tate:  # 爆弾がたてにはみでたら
            vy *= -1
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        vx *= 1.005  # 爆弾を１フレーム当たり1.005倍に加速
        vy *= 1.005
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()