import turtle#导入python中的画画工具包
import time
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
love=input('请输入表白语句，然后回车，默认为"I Love You":\n')
me=input('请输入要表白的人:\n')
if love=='':                    #如果未输入表白语句，则使用默认语句
    love='I Love you'
turtle.setup(width=900,height=600)#爱心的画布的大小
turtle.color('red','pink')#爱心的颜色及外边笔的颜色
turtle.pensize(10)#画笔的粗细
turtle.speed(1000000)#绘制速度

turtle.up()#画笔向上

turtle.hideturtle()
turtle.goto(0,-180)
turtle.showturtle()
turtle.down()
turtle.speed(5)
turtle.begin_fill()#开始填充
turtle.left(140)
turtle.forward(224)
LittleHeart()
turtle.left(120)
LittleHeart()
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,0)
turtle.showturtle()
turtle.color('#CD5C5C','pink')
turtle.write(love,font=('gungsuh',30,),align="center")
turtle.up()
turtle.hideturtle()
if me !='':
    turtle.color('black', 'pink')
    time.sleep(2)
turtle.goto(180,-180)
turtle.showturtle()
turtle.write(me, font=(20,), align="center", move=True)
window=turtle.Screen()
window.exitonclick()
