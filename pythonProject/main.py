import pgzrun
import random
WIDTH = 1000
HEIGHT = 500
jumping = False

velocity_y = 0
gravity = 0.5
#enemy = Actor('')
cell = Actor('border')
cell1 = Actor('floor')
fon = Actor('fon.png')
pistol = Actor('pistol.png')
pokerface = Actor('pokerface12.png')
rebelion = Actor('rebelion.png')
table = Actor('table.png', (240, 250))
table1 = Actor('table.png', (240, 350))
table2 = Actor('table.png', (240, 450))
dante = Actor('милашка.png', (60, 400))
portal = Actor('pngwing.com (7).png', (600, 30))
enemies = []
enemiesplat1 = []
enemiesplat2 = []

for i in range(5):
    x = random.randint(300, 890)
    y = 400
    enemy = Actor('ff.png', (x, y))
    enemy.hp = 50
    enemies.append(enemy)
for i in range(2):
    x = random.randint(260, 460)
    y = 230
    enemy1 = Actor('ff.png', (x, y))
    enemy1.hp = 50
    enemiesplat1.append(enemy1)
for i in range(3):
    x = random.randint(620, 890)
    y = 190
    enemy2 = Actor('ff.png', (x, y))
    enemy2.hp = 50
    enemiesplat2.append(enemy2)
# my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]]
# def map_draw():
#     for i in range(len(my_map)):
#         for j in range(len(my_map[0])):
#             if my_map[i][j] == 0:
#                 cell.left = cell.width*j
#                 cell.top = cell.height*i
#                 cell.draw()
#             elif my_map[i][j] == 1:
#                 cell1.left = cell.width*j
#                 cell1.top = cell.height*i
#                 cell1.draw()


mode = 'menu'
def draw():
    if mode == 'menu':
        pokerface.draw()
        table.draw()
        table1.draw()
        table2.draw()
        screen.draw.text('Начать игру', center=(240, 250), fontsize = 40, color='#834545')
        screen.draw.text('Статистика', center=(240, 350), fontsize=40, color='#834545')
        screen.draw.text('Выйти', center=(240, 450), fontsize=40, color='#834545')
    elif mode == 'game':
        # dante.draw()
        fon.draw()
        dante.draw()
        portal.draw()
    # d


        # map_draw()
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(enemiesplat1)):
            enemiesplat1[i].draw()
        for i in range(len(enemiesplat2)):
            enemiesplat2[i].draw()

        for i in range(20):
            cell.left = i * 50
            cell.top = 450
            cell.draw()
        for i in range (5,9):
            cell1.left =  i * 50
            cell1.top = 278.5
            cell1.draw()
        for i in range(12, 18):
            cell1.left = i * 50
            cell1.top = 240
            cell1.draw()



def update(dt):
    global jumping, velocity_y
    jumping, velocity_y
    if mode == 'game' and keyboard.a and dante.x >= 25 :
        dante.x = dante.x - 5
    elif mode == 'game' and keyboard.d:w
        dante.x = dante.x + 5
    if jumping:
        dante.y += velocity_y
        velocity_y += gravity
        if dante.y >= 400:  # допустим, земля на y=300
            dante.y = 400
            velocity_y = 0
            jumping = False
    if dante.collidelist(enemies) == -1:
        pass
    else:
        pass




# if mode == 'game' and keyboard.W and dante.y <= 100:
#     animate(dante, tween='bounce_end', duration=1, y=240)

#управелние
# def on_key_down(key):
#     if keyboard.W:
#         animate(dante, tween='bounce_end', duration=1, y= dante.y - 100)
def on_key_down(key):
    global jumping, velocity_y
    if key == keys.W and not jumping:
        velocity_y = -13  # начальная скорость прыжка
        jumping = True


def on_mouse_down(pos):
    global mode
    if mouse.LEFT and table.collidepoint(pos):
        mode = 'game'
    if mouse.LEFT and table1.collidepoint(pos):
        mode = 'stat'
    if mouse.LEFT and mode == 'game' or mode == ('game2'):
        for i in range(len(enemies)):
            if enemies[i].colliderect(dante):
                enemies.pop(i)
                break
        for i in range(len(enemiesplat1)):
            if enemiesplat1[i].colliderect(dante):
                enemiesplat1.pop(i)
                break
        for i in range(len(enemiesplat2)):
            if enemiesplat2[i].colliderect(dante):
                enemiesplat2.pop(i)
                break
    # if mouse.LEFT and table2.collidepoint(pos):
    #     #     stop










pgzrun.go()