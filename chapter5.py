
# import
import turtle

#전역변수
swidth = 500
sheight = 500

# 함수
def turtleFunc(name):
  turtle.title("무지개색 원 그리기")
  turtle.shape("turtle")
  turtle.setup(width = swidth + 50, height = sheight + 50)
  turtle.screensize(swidth, sheight)
  turtle.penup()
  turtle.goto(0, -sheight/2)
  turtle.pendown()
  turtle.speed(20)

  for radius in range(1, 250):
    if radius % 7 == 1:
      turtle.pencolor("red")
    elif radius % 7 == 2:
      turtle.pencolor("orange")
    elif radius % 7 == 3:
      turtle.pencolor("yellow")
    elif radius % 7 == 4:
      turtle.pencolor("green")
    elif radius % 7 == 5:
      turtle.pencolor("blue")
    elif radius % 7 == 6:
      turtle.pencolor("navyblue")
    else:
      turtle.pencolor("purple")

    turtle.circle(radius)

  turtle.done()
  # turtleFunc end.

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    turtleFunc('PyCharm')