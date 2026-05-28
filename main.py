from ursina import *
from random import *
app = Ursina()

#initialise vars
littleg = 0.05 # needs tweaking
score = 0
health = 40
gem_parent = Entity()
gem_parent.visible_self = False
PLAYERSPEED = 0.1 # player acceleration
PLAYER_DRAG = 0.03
PLAYER_MAX_SPEED = 0.2
GEM_MAX_SPEED = 0.4 # needs tweaking

def act_drag(input:Vec3):
    output = Vec3()
    tput = tuple(input)
    for i in tput:
        if i > 0:
            output[tput.index(i)] = max(0, i - PLAYER_DRAG)
        elif i < 0:
            output[tput.index(i)] = min(0, i + PLAYER_DRAG)
    return output

def sign(x):
    return (x > 0) - (x < 0)

def cap(x,cap):
    return sign(x)*min(cap,abs(x))

def colour(): # UNUSED!!!
    gemtype = randint(1,4)
    if gemtype == 1:
        gcolor = color.green
    elif gemtype == 2:
        gcolor = color.blue
    elif gemtype == 3:
        gcolor = color.orange
    elif gemtype == 4:
        gcolor = color.yellow
    print(gemtype)
    return gemtype,gcolor

class Ui(Entity):
    def __init__(self,**kwargs):
        super().__init__()
        self.parent = camera
        self.model='quad'
        self.texture='whitepixel.bmp'
        self.position = Vec2(8,8)
        self.scale = Vec2(1,1)


class Gem(Entity):
    def __init__(self,**kwargs):
        super().__init__()
        self.model='cube'
        self.texture='white_cube'
        self.position = Vec3(0.05,25,0)
        self.collider = 'box'
        self.gemtype = 1
        self.color = color.yellow
        self.v = Vec3(0,0,0)
        self.Drag = 0
        self.world_parent = gem_parent
    def update(self):
        global score
        global health
        self.v -= Vec3(0,littleg,0)
        self.Drag = .5*1.225*(self.v[1]*self.v[1])*1.05*(self.scale[1]*self.scale[2])
        self.v += Vec3(0,self.Drag,0)
        
        if self.intersects(player).hit:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.Drag = 0
            self.v = Vec3(0,0,0)
            print('catch')
            if self.gemtype == 1:
                score += 10
            if self.gemtype == 2:
                health += 10
            if self.gemtype == 3:
                health -= 10
            if self.gemtype == 4:
                score += 30

            self.gemtype = randint(1,4)
            if self.gemtype == 1:
                self.color = color.green
            if self.gemtype == 2:
                self.color = color.blue
            if self.gemtype == 3:
                self.color = color.orange
            if self.gemtype == 4:
                self.color = color.yellow
            print(self.gemtype)

        if self.position[1] <= -2:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.v = Vec3(0,0,0)
            self.Drag = 0
            print('down')

            self.gemtype = randint(1,4)
            if self.gemtype == 1:
                self.color = color.green
            if self.gemtype == 2:
                self.color = color.blue
            if self.gemtype == 3:
                self.color = color.orange
            if self.gemtype == 4:
                self.color = color.yellow
            print(self.gemtype)

        if self.position[1] >= 30:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.v = Vec3(0,0,0)
            self.Drag = 0
            print('up')        

            self.gemtype = randint(1,4)
            if self.gemtype == 1:
                self.color = color.green
            if self.gemtype == 2:
                self.color = color.blue
            if self.gemtype == 3:
                self.color = color.orange
            if self.gemtype == 4:
                self.color = color.yellow
            print(self.gemtype)
        for i in self.v:
            self.v[tuple(self.v).index(i)] = cap(i,GEM_MAX_SPEED)
        self.position += self.v
 #       print(f'pos {self.position}')
#        print(f'velocity {self.v}')

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='cube'
        self.texture='white_cube'
        self.position = Vec3(0,0,0)
        self.collider = 'box'
        self.v = Vec3(0,0,0)
        self.scale = Vec3(3,1,1)
    def update(self):
        if health <= 0:
            raise SystemExit() # death, "raise SystemExit()" exits the program
        '''
        if held_keys['shift']:
            if held_keys['a'] or held_keys['q']:
                self.v += Vec3(0-PLAYERSPEED*5,0,0)
            if held_keys['d'] or held_keys['r']:
                self.v += Vec3(PLAYERSPEED*5,0,0)
        else:   '''
        if held_keys['a'] or held_keys['q']:
            self.v += Vec3(0-PLAYERSPEED,0,0)
        if held_keys['d'] or held_keys['r']:
            self.v += Vec3(PLAYERSPEED,0,0)
        for i in self.v:
            self.v[tuple(self.v).index(i)] = cap(i,PLAYER_MAX_SPEED)
        self.position += self.v
        self.v = act_drag(self.v)

EditorCamera()

for i in range(10): # gem num
    Gem()
player = Player()
app.run()