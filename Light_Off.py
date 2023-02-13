# Погаси світло
import turtle as t
from random import randint
CELL = 100 # розмір клітини
DELTA = 40 # розмір бордюра
# размер в клетках для игрового поля
DIM = 5

s=t.Screen()
t.tracer(0)
t.setup(width=CELL*(DIM+2), height=CELL*(DIM+2))
t.setworldcoordinates(-DELTA, -DELTA, CELL*DIM+DELTA, CELL*DIM+DELTA)
t.title("Погаси світло")


# ігрове поле заповнюється
field = [randint(0,1) for _ in range(DIM * DIM)]


def check_win(field):
    ''' Перевіряється чи існує виграш
        Повертає 1 якщо виграли Х
        Повертає -1 якщо виграли О
        Повертає 0 якщо нема '''

    return 0
        
def check_hit(x,y):
    ''' перевіряємо чи клацнули по полі
        якщо ні повертаємо 99, (бо False приймає як 0)
        вираховуємо номери клітки
        повертаємо індекс'''
    # перевіряємо чи клацнули по полі
    if x < 0 or x > CELL*DIM or y < 0 or y > CELL*DIM:
        return 99 # за межами полю

    # вираховуємо номери клітки
    i=int(x/CELL) # стовпчик Х
    j=int(y/CELL) # рядок У
    
    return j*DIM+i

def check_restart(x,y):
    ''' перевіряємо клік по кнопкі '''
    if x > 0 and x < CELL*DIM and y > -40 and y < -20 :
        return True
    return False
    
def draw_text(text,x,y):
    ''' Робимо надпис на вказаних координатах '''
    t.up()
    t.goto(x,y)
    t.write(text,align='center',font=("Arial", 16, "normal"))

def draw_button_restart():
    ''' малюємо кнопку СПОЧАТКУ '''
    w=CELL*DIM # ширина кнопки
    h=DELTA/2 # висота кнопки
    t.color("black", "green")
    t.pensize(1)
    t.up()
    t.home()
    t.goto(0,-h)
    t.down()
    t.begin_fill()
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.up()
    t.end_fill()
    draw_text("Спочатку",CELL*DIM/2,-h*2) # посередині і знизу



def myhit(x,y):
    ''' Обробка клика '''
    global field
    print(field)
    if check_restart(x,y) == True:
        print("Restart")
        field = [randint(0,1) for _ in range(DIM * DIM)]
        draw_field()
        return
        
    #if win != 0: # якщо вже виграли
    #    return
    pos = check_hit(x,y)

    if  pos == 99: # не в просторі поля
        return

    print(pos)

    field[pos]=1-field[pos] # інвертуємо себе
    # перетворюємо індекс в двовимірні координати
    i = pos%DIM # номер стовпчика
    j = int(pos/DIM) # номер рядка
    ''' промацуємо клітки і інвертуємо'''
    if i+1 < DIM:
        field[pos+1]=1-field[pos+1] # справа
    if i-1 >= 0:
        field[pos-1]=1-field[pos-1] # зліва
    if j+1 < DIM:
        field[pos+DIM]=1-field[pos+DIM] # зверху
    if j-1 >= 0:
        field[pos-DIM]=1-field[pos-DIM] #  знизу

    draw_field()
    

def draw_light(x,y,c):
    ''' малюємо квадрат з коорд лівого нижнього кута '''
    t.color("goldenrod", "orange") if c == 1 else t.color("goldenrod", "white")
    t.penup()
    t.goto(x+CELL/10,y+CELL/10)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(CELL*0.8)
        t.left(90)
    t.end_fill()
    t.penup()
    return
    
def draw_field():
    t.reset()
    ''' малюємо поле '''

    for j in range(DIM):
        for i in range(DIM):
            draw_light(i*CELL,j*CELL,field[j*DIM+i])

    draw_button_restart()

if __name__ == "__main__":
    draw_field() # малюємо поле
    print(field)
    s.onclick(myhit)
    t.done()
    
