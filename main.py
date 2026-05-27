from ursina import *
from random import randrange
app = Ursina()

#initialise vars
littleg = 12
boxes = []

class Obj(Entity):
    def __init__(self,**kwargs):
        super().__init__()
        if self.model not in kwargs:
            self.model='cube'
        if self.texture not in kwargs:
            self.texture='white_cube'
        if self.position not in kwargs:
            self.position = Vec3(0.05,25,0)
        if self.scale not in kwargs:
            self.scale = Vec3(1,1,1)
        boxes.append(self.name)
        self.collider = 'box'


        self.mome = Vec3(0,0,0)
        self.grav = True
    def update(self,):
        try:
            if self.intersects(char) or self.intersects():
                
                if 'w' in held_keys or 'a' in held_keys:
                    self.position[1] += 2
                    self.mome += Vec3(0,20,0)
                else:   
                    self.position[1] = 2
                    self.mome[1] = 0 - (self.mome[1])
            else:
                if self.grav == True:
                    self.mome -= Vec3(0,littleg,0) * time.dt
                    Drag = .5*1.225*(self.mome[1]*self.mome[1])*1.05*(self.scale[1]*self.scale[2])*time.dt
                    self.mome += Vec3(0,Drag,0) *time.dt
                if self.position[1] <= -2:
                    self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
                    self.mome = Vec3(0,0,0)
                    Drag = 0
                    
                    print('down')
                elif self.position[1] >= 30:
                    self.position = Vec3(randrange(-10,10)+0.05,0,0)
                    self.mome = Vec3(0,0,0)
                    Drag = 0
                    print('up')
                self.position += self.mome * time.dt
        finally:
            pass
        print(f'y is {self.position[1]}')

    def input(self, key):






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
            self.scale = Vec3(1,1,1)
        self.collider = 'box'
        try:
            self.mome
        except:
            self.mome = Vec3(0,0,0)
        try:
            self.grav
        except:
            self.grav = False
    
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