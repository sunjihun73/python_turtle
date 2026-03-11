# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import turtle

def turtleFunc(name):
    myT = None

    myT = turtle.Turtle()
    myT.color('green')
    myT.shape('turtle')

    for i in range(0, 4):
        myT.forward(300)
        myT.right(90)

    turtle.done()

    # turtle.shape('turtle')
    # turtle.forward(200)
    # turtle.right(90)
    # turtle.forward(200)
    # turtle.right(90)
    # turtle.forward(200)
    # turtle.right(90)
    # turtle.forward(200)
    # turtle.done()

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    turtleFunc('PyCharm')

