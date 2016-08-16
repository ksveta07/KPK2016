from turtle import Turtle

def init_drawman():
    """ инициализация параметров"""
    global t, x_current, y_current, drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale = 10

def test_drawman():
    """Тестирование работы Чертёжника
     : return: None"""
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0,-20)
    pen_up()
    to_point(0, 0)

def pen_down():
    """ Опускает перо"""
    t.pendown()

def pen_up():
    """ Поднимает перо"""
    t.penup()

def on_vector(dx, dy):
    """ Смещается на вектор"""
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    """ Запоминает текущие координаты"""
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(drawman_scale*x_current, drawman_scale*y_current)

init_drawman()

if __name__ == '__main__':
    """ Главная функция"""
    import time
    test_drawman()
    time.sleep(5)# задержка экрана
