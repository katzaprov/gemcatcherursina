from ursina import *
from random import *
app = Ursina()
from winsound import PlaySound,SND_FILENAME

#initialise vars
littleg = 9.8
boxes = []
score = 0
health = 40
Text.default_font = '8514oem.ttf'






scoreboard = Text('Loading',world_scale=20,origin=Vec2(-.5,.5),position=window.top_left,)
healthboard = Text('Loading',world_scale=20,origin=Vec2(-.5,.5),position=window.top_left-(0,0.04),)
def update():
    global scoreboard
    global healthboard
    healthboard.text = f'{"health: " + f'{health}' + ' ' + '|'*(health//2)}'
    scoreboard.text = f'score: {score}'




class Obj(Entity):
    def __init__(self,):
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
                health -=30

            gem = randint(1,4)
            if self.gemtype == gem:
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
            if self.gemtype == gem:
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
            if self.gemtype == gem:
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




class MC(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='cube'
        self.texture='white_cube'
        self.position = Vec3(0,0,0)
        self.scale = Vec3(4,1,1)
        self.collider = 'box'
        self.mome = Vec3(0,0,0)
        Drag = 0

    def update(self):
        speed = 10
        if held_keys['shift']:
            if held_keys['a'] or held_keys['q']:
                self.position += Vec3(-5*speed,0,0)*time.dt
            if held_keys['d'] or held_keys['e']:
                self.position += Vec3(5*speed,0,0)*time.dt
        else:
            if held_keys['a'] or held_keys['q']:
                self.position += Vec3(-speed,0,0)*time.dt
            if held_keys['d'] or held_keys['e']:
                self.position += Vec3(speed,0,0)*time.dt
        if self.position[0] > 10:
            self.position = Vec3(-10,0,0)
        elif self.position[0] < -10:
            self.position = Vec3(10,0,0)
        

        print(self.position[0])


        global health
        if health <= 0:
            global score
            print('Game Over\n')
            print(score)
            raise SystemExit()



script_dir = os.path.dirname(__file__) 
sound_path = '\\'.join([script_dir, 'assets', 'sounds', 'alterraboot.wav'])
print(sound_path)
print('hello world')
PlaySound(sound_path,SND_FILENAME)

EditorCamera()

block1 = Obj()
block2 = Obj()
block3 = Obj()
char = MC()
app.run()