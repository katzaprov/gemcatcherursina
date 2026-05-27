from ursina import *
from random import *
app = Ursina()

#initialise vars
littleg = 12
boxes = []
score = 0
health = 40

def colour(prior):
    gemtype = randint(1,4)
    while prior == gemtype:
        gemtype = randint(1,4)
    if gemtype == 1:
        gcolor = color.green
    if gemtype == 2:
        gcolor = color.blue
    if gemtype == 3:
        gcolor = color.orange
    if gemtype == 4:
        gcolor = color.yellow
    print(gemtype)
    return gemtype,gcolor

class ui():
    def __init__(self,**kwargs):
        super().__init__()
        if self.model not in kwargs:
            self.model='quad'
        if self.texture not in kwargs:
            self.texture='whitepixel.bmp'
        if self.position not in kwargs:
            self.position = Vec2(8,8)
        if self.scale not in kwargs:
            self.scale = Vec2(1,1)


class Obj(Entity):
    def __init__(self,**kwargs):
        super().__init__()
        self.model='cube'
        self.texture='white_cube'
        self.position = Vec3(0.05,25,0)
        self.scale = Vec3(1,1,1)
        self.collider = 'box'
        self.gemtype = 1
        self.color = color.yellow
        self.mome = Vec3(0,0,0)
        self.Drag = 0
        boxes.append(self.name)


    def update(self):
        global score
        global health
        self.mome -= Vec3(0,littleg,0) * time.dt
        self.Drag = .5*1.225*(self.mome[1]*self.mome[1])*1.05*(self.scale[1]*self.scale[2])*time.dt
        self.mome += Vec3(0,self.Drag,0) *time.dt
        
        if self.intersects(char).hit:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.Drag = 0
            self.mome = Vec3(0,0,0)
            print('catch')
            if self.gemtype == 1:
                score += 10
            if self.gemtype == 2:
                health += 10
            if self.gemtype == 3:
                health -= 10
            if self.gemtype == 4:
                score += 30

            gem = randint(1,4)
            while self.gemtype == gem:
                self.gem = randint(1,4)
            if gem == 1:
                self.color = color.green
            if gem == 2:
                self.color = color.blue
            if gem == 3:
                self.color = color.orange
            if gem == 4:
                self.color = color.yellow
            print(gem)
            self.gemtype = gem

        if self.position[1] <= -2:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.mome = Vec3(0,0,0)
            self.Drag = 0
            print('down')

            gem = randint(1,4)
            while self.gemtype == gem:
                self.gem = randint(1,4)
            if gem == 1:
                self.color = color.green
            if gem == 2:
                self.color = color.blue
            if gem == 3:
                self.color = color.orange
            if gem == 4:
                self.color = color.yellow
            print(gem)
            self.gemtype = gem

        if self.position[1] >= 30:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.mome = Vec3(0,0,0)
            self.Drag = 0
            print('up')        

            gem = randint(1,4)
            while self.gemtype == gem:
                self.gem = randint(1,4)
            if gem == 1:
                self.color = color.green
            if gem == 2:
                self.color = color.blue
            if gem == 3:
                self.color = color.orange
            if gem == 4:
                self.color = color.yellow
            print(gem)
            self.gemtype = gem

        self.position += self.mome * time.dt
        print(f'pos {self.position}')
        print(f'momentum {self.mome}')




class MC(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        if self.model not in self.attributes:
            self.model='cube'
        if self.texture not in self.attributes:
            self.texture='white_cube'
        if self.position not in self.attributes:
            self.position = Vec3(0,0,0)
        if self.scale not in self.attributes:
            self.scale = Vec3(4,1,1)
        self.collider = 'box'
        try:
            self.mome
        except:
            self.mome = Vec3(0,0,0)
    
    def input(self, key):
        if held_keys['shift']:
            if key == 'a' or key == 'q':
                self.position += Vec3(-2,0,0)
            if key == 'd' or key == 'r':
                self.position += Vec3(2,0,0)
        else:
            if key == 'a' or key == 'q':
                self.position += Vec3(-.5,0,0)
            if key == 'd' or key == 'r':
                self.position += Vec3(.5,0,0)


    def update(self):
        self.position += self.mome * time.dt


cam = EditorCamera()

block1 = Obj()
block2 = Obj()
block3 = Obj()
char = MC()
app.run()