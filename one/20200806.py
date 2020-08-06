#画太阳花

from turtle import *
def drawSunFlower():
    color('red','yellow')
    begin_fill()
    while True:
        forward(300)
        left(172)
        if abs(pos())<1:
            break
            end_fill()
            done()
    Screen().exitonclick()
# drawSunFlower()
#########################################分割线#######################################################
import turtle

def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)  # 直线前进
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)
def drawSnakeFn():
    if __name__ == "__main__":
       turtle.setup(1500, 1400, 0, 0)
       turtle.pensize(30)  # 画笔尺寸
       turtle.pencolor("green")
       turtle.seth(-40)    # 前进的方向
       drawSnake(70, 80, 2, 15)
       turtle.Screen().exitonclick()
# drawSnakeFn()
#########################################分割线#######################################################

import turtle as t #turtle库是python的内部库，直接import使用即可

def draw_diamond(turt):
    for i in range(1,3):
        turt.forward(100) #向前走100步🐢
        turt.right(45) #海龟头向右转45度
        turt.forward(100) #继续向前走100步🐢
        turt.right(135) #海龟头再向右转135度


def draw_art():
    window = t.Screen() #创建画布

    brad = t.Turtle() #创建一个Turtle的实例
    brad.shape('turtle') #形状是一个海归turtle，也可以是圆圈circle，箭头(默认)等等

    window.bgcolor("grey")
    brad.color("orange") #海龟的颜色是红色red，橙色orange等
    brad.speed('slow') #海龟画图的速度是快速fast，或者slow等

    for i in range(1,37): #循环36次
        draw_diamond(brad) #海龟画一个形状/花瓣，也就是菱形
        brad.right(10) #后海龟头向右旋转10度

    brad.right(90) #当图形画完一圈后，把海龟头向右转90度
    brad.forward(300) #画一根长线/海龟往前走300步

    window.exitonclick() #点击屏幕退出


draw_art() #调用函数开始画图
































































