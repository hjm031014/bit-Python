import turtle as t
x=0
y=0

while(y<420):
    t.speed(10)
    t.goto(x,y)
    t.pendown()
    t.forward(400)
    t.penup()
    y+=20


x=0
y=0

t.right(90)

while(x<420):
    t.speed(10)
    t.goto(x,y)
    
    t.pendown()
    t.forward(-400)
    t.penup()
    
    x+=20

t.penup()

def a():
    t.color("red")

def b():
    t.color("blue")

def c(x,y):
    t.goto(x,y)
    t.stamp()
    t.penup()
    
t.onkeypress(a,"r") #빨간색 변경
t.onkeypress(b,"b") #파란색 변경
t.listen()

t.onscreenclick(c)




