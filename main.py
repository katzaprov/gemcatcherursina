from ursina import *
from random import randint,randrange

print("Janidite is green, it’s what you're employed to gather and it’s good money.")
print("Hoplitite is blue, it can be used to fix your hull but its quality degrades over time so it’s best used fresh and doesn’t sell for much.")
print("Dynomite is orange. It's highly reactive and starts a chain reaction, destroying janidite and messing up your hull.")
print("Aurelite is chock full of gold, and gallium too. It’ll sell for a load of money and it’ll dissolve your hull at the atomic level.")
input("Press ENTER to continue")

app = Ursina(show_ursina_splash=True,)
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

def gemrand():
    gemtypebuff = randint(1,10)
    if gemtypebuff in range(1,5):
        gemtypebuff = 1
    elif gemtypebuff == 6:
        gemtypebuff = 2
    elif gemtypebuff in range(7,9):
        gemtypebuff = 3
    else:
        gemtypebuff = 4
    
    if gemtypebuff == 1:
        colorbuff = color.green
    if gemtypebuff == 2:
        colorbuff = color.blue
    if gemtypebuff == 3:
        colorbuff = color.orange
    if gemtypebuff == 4:
        colorbuff = color.yellow
    return gemtypebuff,colorbuff


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
                health += 7
            if self.gemtype == 3:
                health -= 10
                score -= 6
            if self.gemtype == 4:
                score += 30
                health -=30
            gemcalc = gemrand()
            self.color = gemcalc[1]
            self.gemtype = gemcalc[0]

        if self.position[1] <= -2:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.mome = Vec3(0,0,0)
            self.Drag = 0
            print('down')

            gemcalc = gemrand()
            self.color = gemcalc[1]
            self.gemtype = gemcalc[0]

        if self.position[1] >= 30:
            self.position = Vec3(randrange(-10,10)+0.05,randrange(25,30),0)
            self.mome = Vec3(0,0,0)
            self.Drag = 0
            print('up') 

            gemcalc = gemrand()
            self.color = gemcalc[1]
            self.gemtype = gemcalc[0]       


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
        if self.position[0] > 20:
            self.position = Vec3(-20,0,0)
        elif self.position[0] < -20:
            self.position = Vec3(20,0,0)
        

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

#EditorCamera()
camera.position = Vec3(0,15,-80)
camera.orthographic = True

for i in range(3):
    Obj()
char = MC()
app.run()