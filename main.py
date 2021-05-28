from Objects import *
import pygame
import time
import pickle


pygame.init()
pygame.font.init()
display_width = 1260
display_height = 860
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')


def lev1():
    global loss, score
    score = 1
    coll1 = 0
    coll = 0
    game_lev1 = True
    t1 = time.time()
    while game_lev1:
        key = ''
        pygame.display.set_caption("Game. FPS: %.2f" % (fps.get_fps()))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            '#print(event, event.type)'
            if event.type == pygame.KEYDOWN:
                k = event.key
                if k == pygame.K_SPACE:
                    key = 'J'
                if k == pygame.K_y:
                    key = 'D'
            if event.type == pygame.QUIT:
                pygame.quit()
                game_lev1 = False
                # sve()
        '---------print------------'
        '#Bg'
        Bg1.show()
        Bg2.show()
        Bg3.show(move=True, speed=0.75)
        Bg4.show(move=True, speed=0.5)
        Bg5.show(move=True, speed=8)
        Bg6.show(move=True, speed=12)
        '# MapGen'
        zz = 1-(score/200)
        if zz+1 >= 0.85:
            map_gen.print_obj(zz+1)
            # print(zz+1)
        for obj in map_gen.oblist:
            text.show('score:'+str(obj.id)+' coll:'+str(coll1), [1050, 20])
            score = obj.id
            # obj.print(screen, 10+score/2.5, time_)
            if obj.print(screen, 10+score/2.5, time_):
                map_gen.oblist.remove(obj)
                del obj
            else:
                pass
        '# player'

        if map_gen.oblist:
            ob_ponp = map_gen.oblist[0].ponp
        else:
            ob_ponp = 1000000, 1000000
        if ob_ponp[1] == 600 and autoplay:
            if ob_ponp[0] <= 300:
                key = 'J'
        elif ob_ponp[1] == 601 and autoplay:
            if ob_ponp[0] <= 400:
                key = 'J'
        elif ob_ponp[1] == 450 and autoplay:
            if ob_ponp[0] <= 350:
                key = 'D'

        pl.control(key)
        # if key_ != 0:
        #     print([pl.mode['p_on_p'], pl.mode['wh'], ob_ponp, ob_wh], key_)
        # data.append([[pl.mode['p_on_p'], pl.mode['wh'], ob_ponp, ob_wh], key_])
        if pl.test_coll(map_gen.oblist):
            coll += 1
            coll1 += 1
            text.show('HIT', (display_width/2, display_height/2))
        else:
            coll = 0
        if coll >= 3:
            loss = True
            game_lev1 = False
            end()
        if score >= endScore:
            loss = False
            game_lev1 = False
            end()
        '# Mouse'
        mouse_.showM(mouse)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)
        delay = (t1-time.time())/FPS
        if delay > 0:
            # print(delay)
            time.sleep(delay)
        t1 = time.time()
        # time_.set_time(score/5)
    # sve()


def end():
    # sve()
    global loss, score
    game_lev1 = True
    t1 = time.time()
    while game_lev1:
        key = ''
        pygame.display.set_caption("Game. FPS: %.2f" % (fps.get_fps()))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            '#print(event, event.type)'
            if event.type == pygame.MOUSEBUTTONDOWN:
                lev1()
            if event.type == pygame.QUIT:
                pygame.quit()
                game_lev1 = False
                # sve()
        '---------print------------'
        '#Bg'
        delay = (t1-time.time())/FPS
        if delay > 0:
            # print(delay)
            time.sleep(delay)
        t1 = time.time()

        Bg1.show()
        Bg2.show()
        Bg3.show(move=True, speed=0.75)
        Bg4.show(move=True, speed=0.5)
        Bg5.show(move=True, speed=8)
        Bg6.show(move=True, speed=12)

        text.show('END , score:'+str(score), (display_width / 2-200, display_height / 2), [0, 0, 0], 100)
        if loss:
            text.show('FAIL', (display_width / 2, (display_height / 2)+100), [0, 0, 0], 100)
        else:
            text.show('WIN', (display_width / 2, (display_height / 2) + 100), [0, 0, 0], 100)
        '# Mouse'
        mouse_.showM(mouse)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)


# def sve():
#     global data
#     try:
#         pickle_out = open('data.pickle', "wb")
#         pickle.dump(data, pickle_out)
#         pickle_out.close()
#     except FileNotFoundError:
#         print('@|error> in SaveData')
#
if __name__ == '__main__':
    autoplay = False
    endScore = 10
    box = True
    # try:
    #    pickle_in = open('data.pickle', "rb")
    #    data = pickle.load(pickle_in)
    #    print(data)
    # except FileNotFoundError:
    #    print('@|error> in LoadData')

    '---------------FPS-----------------'
    fps = pygame.time.Clock()
    FPS = 60
    FPS_mov = 24
    time_ = T()
    '---------------mouse---------------'
    mouse_ = Mouse('musket.png', screen)

    '-------------text------------------'
    text = Text(screen)

    '#---------------bg-----------------'
    Bg = Backgraund(screen, time_, 'a.png', 1260, )
    Bg1 = Backgraund(screen, time_, 'BackgroundMoonandSun.png', 1260)
    Bg2 = Backgraund(screen, time_, 'sonnen.png', 1260)
    Bg3 = Backgraund(screen, time_, 'Wolken.png', 1260)
    Bg4 = Backgraund(screen, time_, 'Berge.png', 1260)
    Bg5 = Backgraund(screen, time_, 'Baum.png', 1260)
    Bg6 = Backgraund(screen, time_, 'graund.png', 1260)
    Bg7 = Backgraund(screen, time_, 'SpaceXLaunchMainBuilding.png', 1260)
    Bg8 = Backgraund(screen, time_, 'ElonMusketWithWeed.png', 1260)
    Bg9 = Backgraund(screen, time_, 'BFX.png', 1260)

    '---------------PL-----------------'
    pl = Player(screen, time_, 'rfg.png', 'rf.png', 'rfk.png')

    '#------------Map-gen---------------'
    ma_p = []
    for line in open('map.txt'):
        ma_p.append(int(line))
    map_gen = MapGen(time)
    map_gen.get_net_img()
    '---------------Bid-----------------'
    loss = False

    lev1()
