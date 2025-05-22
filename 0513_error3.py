try:
    a = [1,2,3,4,5]
    b = a[5]  # IndexError 발생
    c = 10/0  # ZeroDivisionError 발생
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e: #폭포수(cascading)
    print(e)


#raise 예외 문구 강제 예외 발생
#원래 함수 종료 구문은 return 하는일이 많다.
#return 값은 전송, 함수가 끝날때까 마무리 작업을 하고 나온다.
#생성자에 오류가 발생했을때 어떻게 할것인가?
#->return 사용불가 그래서 만든 것이 raise
#->정리작업도 하고 온다.

class Test:
    def __init__(self):
        raise Exception("객체 생성 오류")
try:
    t1 = Test()
except Exception as e:
    print(e)


