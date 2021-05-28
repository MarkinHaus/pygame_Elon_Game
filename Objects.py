import pygame
from random import randint


class Backgraund:

    def __init__(self, screen, time_, image_n, w):
        img = pygame.image.load('Texturen/' + str(image_n)).convert_alpha()
        self.screen = screen
        self.Bglist = [img]
        self.time = time_
        self.w = w + int(self.Bglist[0].get_width()/8)
        self.Bglist_ = [image_n]
        self.i = 0

    def add_bg(self, image_n):
        img = pygame.image.load('Texturen/' + str(image_n)).convert_alpha()
        self.Bglist.append(img)
        self.Bglist_.append(image_n)

    def remove_bg(self, image_n):
        img = pygame.image.load('Texturen/' + str(image_n)).convert_alpha()
        self.Bglist.remove(img)
        self.Bglist_.remove(image_n)

    def get_list(self):
        return self.Bglist_

    def show(self, num=0, move=False, speed=15):
        if move:
            self.i -= speed + self.time.get_time()
            self.screen.blit(self.Bglist[num], (self.i, 0))
            self.screen.blit(self.Bglist[num], (-self.Bglist[num].get_width()+self.i, 0))
            if 0 >= self.i:
                self.i = self.w
        else:
            self.screen.blit(self.Bglist[num], (0, 0))


class Text:

    def __init__(self, screen):
        self.screen = screen
        '#CalibriLight.ttf'
    def show(self, text, xy, color=(0, 0, 0), size=30, text_type='freesansbold.ttf'):
        self.screen.blit(pygame.font.SysFont(text_type, size)
                         .render(str(text), False, color), xy)


class Objects:

    def __init__(self):
        self.mode = {'color': (255, 255, 255), 's_l_a': False,
                     'py': False, 'wh': (0, 0), 'p_on_p': (0, 0),
                     'on_hit': False, 'object': None}

    def set_all(self, color=(255, 255, 255), py=False, sla=False, wh=(0, 0), p_on_p=(0, 0), obj=None):
        self.mode['color'] = color
        self.mode['py'] = py
        self.mode['s_l_a'] = sla
        self.mode['wh'] = wh
        self.mode['p_on_p'] = p_on_p
        self.mode['object'] = obj

    def set_color(self, color):
        self.mode['color'] = color

    def set_py(self, py):
        self.mode['py'] = py

    def set_sla(self, sla):
        self.mode['s_l_a'] = sla

    def set_wh(self, wh):
        self.mode['wh'] = wh

    def set_ponp(self, p_on_p):
        self.mode['p_on_p'] = p_on_p

    def set_obj(self, objects):
        self.mode['object'] = objects

    def test_on_hit_l(self, x, y):
        if self.mode['p_on_p'][0]+self.mode['wh'][0] >= x >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0]+self.mode['wh'][1] >= y >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0]+self.mode['wh'][0] >= y <= self.mode['p_on_p'][1]+self.mode['wh'][1] \
                and self.mode['p_on_p'][0] <= x >= self.mode['p_on_p'][1]:
            self.mode['on_hit'] = True
        else:
            self.mode['on_hit'] = False
        return self.mode['on_hit']

    def load(self):
        return self.mode

    def g_rect(self):
        return pygame.Rect(self.mode['p_on_p'][0], self.mode['p_on_p'][1], self.mode['wh'][0], self.mode['wh'][1])


class Collision:

    def __init__(self):
        self.collision_ = False
        self.list1 = []

    def set_fix(self, ob2):
        ob2.mode = ob2.load()
        list1 = []
        for i in range(ob2.mode['wh'][0]+1):
            x = i + ob2.mode['p_on_p'][0]
            y = 0

            for i1 in range(ob2.mode['wh'][1]+1):
                y = i1 + ob2.mode['p_on_p'][1]
                list1.append((x, y))

        self.list1 = list1

    def collision_f(self, ob1):
        i2 = 0
        ob1.mode = ob1.load()
        while i2 != self.list1.__len__():
            a = self.list1[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    def collision(self, ob1, ob2):
        ob1.mode = ob1.load()
        ob2.mode = ob2.load()
        ob2.list = []
        a = 0
        for i in range(ob2.mode['wh'][0]+1):
            x = i + ob2.mode['p_on_p'][0]
            if i == 0 or i == ob2.mode['wh'][0]:
                a = 1

            for i1 in range(ob2.mode['wh'][1]+1):
                y = i1 + ob2.mode['p_on_p'][1]
                if a == 1:
                    ob2.list.append((x, y))
                    a = 0
                elif i1 == 0 or i1 == ob2.mode['wh'][1]:
                    ob2.list.append((x, y))
                    a = 0
        i2 = 0
        while i2 != ob2.list.__len__():
            a = ob2.list[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    def coll_rect(self, ob1, ob2):
        rect1 = ob1.g_rect()
        rect2 = ob2.g_rect()
        return rect1.colliderect(rect2)




class Mouse:

    def __init__(self, img, screen):
        imgmouse = pygame.image.load('Texturen/' + str(img)).convert_alpha()
        self.imgmouse = imgmouse
        self.screen = screen
        pygame.mouse.set_visible(False)

    def showM(self, mouse):
        self.screen.blit(self.imgmouse, mouse)


class Button(Objects):

    def __init__(self, screen, name, point, wh):
        Objects.__init__(self)
        self.img = pygame.image.load('Texturen/' + str(name)).convert_alpha()
        self.screen = screen
        self.set_all(wh=wh, p_on_p=point)

    def show(self, mouse, click):
        self.screen.blit(self.img, self.mode['p_on_p'])
        if click == 1:
            return self.test_on_hit_l(mouse[0], mouse[1])
        else:
            return False


class T:
    def __init__(self):
        self.time = 0

    def set_time(self, t):
        self.time = t

    def get_time(self):
        return self.time


class Player(Collision, Objects):
    def __init__(self, screen, time_c, img1, img2, img3):
        Collision.__init__(self)
        Objects.__init__(self)
        self.set_wh((210, 210))
        self.set_ponp((30, 425))
        self.time = time_c
        self.screen = screen
        self.now = 0
        self.in_jump = False
        self.in_d = False
        self.jump_p = 0
        self.down_p = 0
        self.j_w = 0
        self.d_w = 0
        # Run
        img = pygame.image.load('Texturen/' + str(img1)).convert_alpha()
        img1 = pygame.image.load('Texturen/' + str(img2)).convert_alpha()
        self.img0 = [img, img1]
        # jump
        self.img1 = pygame.image.load('Texturen/' + str(img3)).convert_alpha()
        # duck
        self.img2 = pygame.image.load('Texturen/' + str(img3)).convert_alpha()

    def t_now(self):
        if self.now == 0:
            self.now = 1
        else:
            self.now = 0

    def height(self):
        if self.in_jump:
            if self.jump_p == 0:
                if self.mode['p_on_p'][1] > 425-150:
                    self.set_ponp((self.mode['p_on_p'][0], self.mode['p_on_p'][1] - 10 - self.time.get_time()))
                else:
                    if self.j_w <= 10:
                        self.j_w += 1 + self.time.get_time()/1.5
                    else:
                        self.j_w = 0
                        self.jump_p = 1
            if self.jump_p == 1:
                if self.mode['p_on_p'][1] < 425:
                    self.set_ponp((self.mode['p_on_p'][0], self.mode['p_on_p'][1] + 10 + self.time.get_time()))
                else:
                    self.jump_p = 0
                    self.in_jump = False
                    #self.set_ponp((30, 425))

    def down(self):
        if self.in_d:
            if self.down_p == 0:
                if self.mode['p_on_p'][1] < 425+100:
                    self.set_ponp((self.mode['p_on_p'][0], self.mode['p_on_p'][1] + 10 + self.time.get_time()))
                else:
                    if self.d_w <= 10:
                        self.d_w += 1 + self.time.get_time()/1.5
                    else:
                        self.d_w = 0
                        self.down_p = 1
            if self.down_p == 1:
                if self.mode['p_on_p'][1] > 425:
                    self.set_ponp((self.mode['p_on_p'][0], self.mode['p_on_p'][1] - 10 - self.time.get_time()))
                else:
                    self.down_p = 0
                    self.in_d = False
                    #self.set_ponp((30, 425))

    def run(self):
        self.screen.blit(self.img0[self.now], self.mode['p_on_p'])
        self.t_now()

    def jump(self):
        self.screen.blit(self.img1, self.mode['p_on_p'])
        self.height()

    def duck(self):
        self.screen.blit(self.img2, self.mode['p_on_p'])
        self.down()

    def control(self, key):
        if self.in_jump:
            self.jump()
        elif self.in_d:
            self.duck()
        elif key == 'J':
            self.in_jump = True
            self.jump()
        elif key == 'D':
            self.in_d = True
            self.duck()
        else:
            self.run()

    def test_coll(self, ob_next):
        if not ob_next:
            return False
        for ob in ob_next:
            return self.coll_rect(self, ob)


class MapObj(Objects):
    def __init__(self, ponp, wh, img, id):
        Objects.__init__(self)
        self.ponp = [1260, ponp[1]]
        self.wh = wh
        self.img = img
        self.id = id
        self.set_wh(self.wh)
        self.set_ponp(self.ponp)

    def print(self, screen, speed, time):
        self.ponp[0] -= speed + time.get_time()/0.5
        screen.blit(self.img, self.ponp)
        self.set_ponp(self.ponp)
        if 0 >= self.ponp[0]:
            return True
        return False


class MapGen:

    def __init__(self, time):
        self.time = time
        img = pygame.image.load('Texturen/spik.png').convert_alpha()
        img1 = pygame.image.load('Texturen/Nspik.png').convert_alpha()
        img2 = pygame.image.load('Texturen/rekt.png').convert_alpha()
        self.img0 = [img, img1, img2]
        self.pos = [[1260, 600], [1260, 450], [1260, 601]]
        self.wh = [(115, 20), (115, 20), (50, 50)]
        self.id = 0
        self.t = time.time()
        self.oblist = []

    def get_net_img(self):
        i = randint(0, 2)
        self.id += 1
        self.oblist.append(MapObj(self.pos[i], self.wh[i], self.img0[i], self.id))

    def print_obj(self, t):
        if self.time.time() - t > self.t:
            self.t = self.time.time()
            self.get_net_img()

        return self.oblist
