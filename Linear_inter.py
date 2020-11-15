'''# Point-to-Point Comparison Method of Linear Interpolation
计算机控制系统中逐点比较法的直线插补程序。能够显示插补阶梯状直线与各个转折点坐标。'''

import turtle as t

'''象限判断0'''
def space_judge0(a):
    if a > 0:
       ZF = 1
    else:
       ZF = -1
    return ZF

'''象限判断1'''
def space_judge1(a):
    if a > 0:
        ZF = 1
    else:
        ZF = -1
    return ZF

'''画布，目标曲线初始化'''
def Canvas_init():
    t.setup(width=800, height=800, startx=0, starty=100)
    '''坐标轴绘制'''
    t.pendown()
    t.pensize(3)
    t.goto(500,0)
    t.goto(490,10)
    t.goto(500,0)
    t.goto(490,-10)
    t.goto(500,0)
    t.goto(-500,0)
    t.goto(0,0)
    t.goto(0,300)
    t.goto(10,290)
    t.goto(0,300)
    t.goto(-10,290)
    t.goto(0,300)
    t.goto(0,-300)
    t.penup()
    t.goto(0,0)
    '''目标曲线绘制'''
    t.pendown()
    t.pensize(2)
    t.goto(XE, YE)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('blue')
    t.speed(1)

'''标点'''
def dot(x,y,z):
    t.color('red')
    t.right(90)
    t.penup()
    t.fd(z)
    t.left(90)
    t.pendown()
    t.circle(z)
    t.penup()
    t.goto(x,y)
    t.color('blue')
    t.pendown()

'''输入以及各参数初始化'''
XE = int(input('输入横坐标X:')) * 50
YE = int(input('输入横坐标Y:')) * 50
'''步进精度'''
x_step = int(input('输入x步进量:'))*50
y_step = int(input('输入y步进量:'))*50
NXY =int(abs(XE/50)+abs(YE/50)*(x_step+y_step))
NXY_store = NXY
FM=0
X=0
Y=0

Canvas_init()

'''逐点比较法'''
while (NXY != 0 ):
    if FM >= 0:
        ZF = space_judge0(XE)
        X = X + ZF * x_step
        t.goto(X,Y)
        dot(X,Y,int(x_step)/10)
        if Y/X == YE/XE:
            FM = 0
        else:
            FM = (Y * XE) - abs(X * YE)
        print(int(NXY_store+1-NXY), ':(', X/50, ',', Y/50, ')')
    else:
        ZF = space_judge1(YE)
        Y = Y + ZF * y_step
        t.goto(X,Y)
        dot(X,Y,int(y_step)/10)
        if Y/X == YE/XE:
            FM = 0
        else:
            FM = abs(Y * XE) - (X * YE)
        print(int(NXY_store+1-NXY), ':(', X/50, ',', Y/50, ')')
    NXY = NXY - 1
    if X >= XE and Y >= YE:
        break

'''保留图片窗口'''
t.done() 



