#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Путешествие по эпохам"
FPS = 30

# Объекты
fon = Actor('bd', size = (600, 400))
kope = Actor('kope', (400, 230), size = (300, 400))
robot = Actor('robot3', size = (200, 200))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 300))
button_menu = Actor("bonus", (300, 280))
button_game = Actor("bonus", (300, 180))
button_gallery = Actor("bonus", (300, 280))
win = Actor('win')
legko = Actor("uroven", (150, 80), size = (200, 100))
slogno = Actor("uroven", (150, 280), size = (200, 100))


# Переменные
count = 0
damage = 1
hp = 20
price1 = 25
price2 = 50
mode = 'menu'

#Отрисовка
def draw():
    global hp, mode, count
    if mode == 'legko':
        fon.draw()
        kope.draw()
        screen.draw.text(count, center=(570, 30), color="white", fontsize = 30)
        #Бонусы
        bonus_1.draw()
        screen.draw.text("+ 10 лет каждые 2с", center=(100, 80), color="white", fontsize = 20)
        screen.draw.text(price1, center=(100, 110), color="white", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+ 5 очков каждые 2с", center=(100, 280), color="white", fontsize = 20)
        screen.draw.text(price2, center=(100, 310), color="white", fontsize = 20)
        #Условия отрисовки 
        if  hp <= 0 and kope.image == 'kope':
            hp = 30
            kope.image = 'koleco'
        elif hp <= 0 and kope.image == 'koleco':
            hp = 40
            kope.image = 'shpaga'
        elif hp <= 0 and kope.image == 'shpaga':
            hp = 50
            kope.image = 'radio'
        elif hp <= 0 and kope.image == 'radio':
            hp = 60
            kope.image = 'nout'
        elif hp <= 0 and kope.image == 'nout':
            hp = 70
            kope.image = 'robot3'
            #Финальное окно
        elif hp <= 0 and kope.image == 'robot3':
            win.draw()
            screen.draw.text("Вы          ", center=(280, 100), color="#00FFFF", fontsize = 50)
            screen.draw.text("в       ", center=(340, 100), color="#1E90FF", fontsize = 50)
            screen.draw.text("будущем!", center=(430, 100), color="#0000CD", fontsize = 50)
    elif mode == 'slogno':
        fon.draw()
        kope.draw()
        screen.draw.text(count, center=(570, 30), color="white", fontsize = 30)
        #Бонусы
        bonus_1.draw()
        screen.draw.text("+ 10 лет каждые 2с", center=(100, 80), color="white", fontsize = 20)
        screen.draw.text(price1, center=(100, 110), color="white", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+ 5 очков каждые 2с", center=(100, 280), color="white", fontsize = 20)
        screen.draw.text(price2, center=(100, 310), color="white", fontsize = 20)
        #Условия отрисовки 
        if  hp <= 0 and kope.image == 'kope':
            hp = 50
            kope.image = 'koleco'
        elif hp <= 0 and kope.image == 'koleco':
            hp = 70
            kope.image = 'shpaga'
        elif hp <= 0 and kope.image == 'shpaga':
            hp = 100
            kope.image = 'radio'
        elif hp <= 0 and kope.image == 'radio':
            hp = 120
            kope.image = 'nout'
        elif hp <= 0 and kope.image == 'nout':
            hp = 140
            kope.image = 'robot3'
            #Финальное окно
        elif hp <= 0 and kope.image == 'robot3':
            win.draw()
            screen.draw.text("Вы          ", center=(280, 100), color="#00FFFF", fontsize = 50)
            screen.draw.text("в       ", center=(340, 100), color="#1E90FF", fontsize = 50)
            screen.draw.text("будущем!", center=(430, 100), color="#0000CD", fontsize = 50)
    elif mode == 'menu':
        fon.draw()
        legko.draw()
        screen.draw.text('Легкий режим', center=(150, 80), color="white", fontsize = 20)
        slogno.draw()
        screen.draw.text('Сложный режим', center=(150, 280), color="white", fontsize = 20)
        
    
#Функции бонусов
def for_bonus_1():
    global hp
    hp -= 10

def for_bonus_2():
    global count
    count += 5


#Обработка кликов
def on_mouse_down(button, pos):
    global count, damage, hp, price1, price2, mode
    if button == mouse.LEFT:
        if kope.collidepoint(pos) and (mode == 'legko' or mode == 'slogno'):
            count += 1
            hp -= damage
            kope.y = 200
        elif bonus_1.collidepoint(pos):
            if count >= price1:
                schedule_interval(for_bonus_1, 2)
                count -= price1
                price1 *= 2
        elif bonus_2.collidepoint(pos):
            if count >= price2:
                schedule_interval(for_bonus_2, 2)
                count -= price2
                price2 *= 2 
        if mode == 'menu':
            if legko.collidepoint(pos):
                mode = 'legko'
            elif slogno.collidepoint(pos):
                mode = 'slogno'