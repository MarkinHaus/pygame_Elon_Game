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

#try:
#    pickle_in = open('data.pickle', "rb")
#    data = pickle.load(pickle_in)
#    print(data)
#except FileNotFoundError:
#    print('@|error> in LoadData')

'---------------FPS-----------------'
fps = pygame.time.Clock()
FPS = 600
time_ = T()
'---------------mouse---------------'
mouse_ = Mouse('musket.png', screen)

'-------------text------------------'
text = Text(screen)

'#---------------bg-----------------'
Bg = Backgraund(screen, time_, 'a.png', 1260,)
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


def lev1():
    global loss, score
    score = 1
    coll = 0
    coll1 = 0
    game_lev1 = True
    while game_lev1:
        key = ''
        key_ = 0
        pygame.display.set_caption("Game. FPS: %.2f" % (fps.get_fps()))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            '#print(event, event.type)'
            if event.type == 2:
                k = event.key
                if k == pygame.K_SPACE:
                    key = 'J'
                    key_ = 1
                if k == pygame.K_e:
                    key = 'D'
                    key_ = 2
            if event.type == 12:
                '#exit'
                game_lev1 = False
                #sve()
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
            print(zz+1)
        for obj in map_gen.oblist:
            text.show('score:'+str(obj.id)+' coll:'+str(coll1), [1050, 20])
            score = obj.id
            #obj.print(screen, 10+score/2.5, tim  e_)
            if obj.print(screen, 10+score/2.5, time_):
                map_gen.oblist.remove(obj)
            else:
                pass
        '# player'
        if map_gen.oblist:
            ob_ponp = map_gen.oblist[0].ponp
            ob_wh = map_gen.oblist[0].wh
        else:
            ob_ponp = 1000000, 1000000
            ob_wh = 1000000, 1000000
        if ob_ponp[1] == 600:
            if ob_ponp[0] <= 300:
                key = 'J'
        elif ob_ponp[1] == 601:
            if ob_ponp[0] <= 400:
                key = 'J'
        elif ob_ponp[1] == 450:
            if ob_ponp[0] <= 350:
                key = 'D'
        pl.control(key)
        #if key_ != 0:
        #    print([pl.mode['p_on_p'], pl.mode['wh'], ob_ponp, ob_wh], key_)
        #data.append([[pl.mode['p_on_p'], pl.mode['wh'], ob_ponp, ob_wh], key_])
        #if pl.test_coll(map_gen.oblist):
        #    coll += 1
        #    coll1 += 1
        #    text.show('HIT', (display_width/2, display_height/2))
        #else:
        #    coll = 0
        #if coll >= 3:
        #    loss = True
        #    game_lev1 = False
        #    end()
        #'# Mouse'
        mouse_.showM(mouse)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)
        #time_.set_time(score/5)
    #sve()


def end():
    #sve()
    global loss, score
    game_lev1 = True
    while game_lev1:
        key = ''
        pygame.display.set_caption("Game. FPS: %.2f" % (fps.get_fps()))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            '#print(event, event.type)'
            if event.type == 2:
                k = event.key
                print(k)
                if k == pygame.K_SPACE:
                    key = 'J'
                if k == pygame.K_e:
                    key = 'D'
                print(k, key)
                '# pres key'
                pass
            if event.type == 12:
                '#exit'
                game_lev1 = False
                #sve()
        '---------print------------'
        '#Bg'
        Bg1.show()
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


#def sve():
#    global data
#    try:
#        pickle_out = open('data.pickle', "wb")
#        pickle.dump(data, pickle_out)
#        pickle_out.close()
#    except FileNotFoundError:
#        print('@|error> in SaveData')
#

lev1()
