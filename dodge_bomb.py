import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1200, 700


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)  # 爆弾用の乱数、x軸
    y = random.randint(0, HEIGHT)  # 爆弾用の乱数、y軸
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y  # 練習２
    vx, vy = +5, +5  #練習２
    moving = {pg.K_UP: (0, -5), pg.K_DOWN: (0, +5), pg.K_LEFT: (-5, 0), pg.K_RIGHT: (+5, 0)}
    kk_rct = kk_img.get_rect()
    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
 
        for k, mv in moving.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]

        kk_rct[0] += sum_mv[0]
        kk_rct[1] += sum_mv[1]

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)  #  練習２
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()