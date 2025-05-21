# 클래스 공간 (Class Namespace)
class Person:
#이 공간은 클래스 공간이다. 클래스 정의할때 딱 한번 실행된다
# 객체 만들때마다 실행되지 않는다. 그래서 list타입이나 dict타입 등을 함부로 여기에
# 선언하면 안된다.

    name = "홍길동"
    age = 12
    phone = []

    #생성자에서 변수를 만들자.
    def __init__(self):
        self.name = ""
        self.age = 0
        self.phone = []

    def append(self, name="임꺽정", age=13, phone="010-1234-5678"):
        self.name = name
        self.age = age
        self.phone.append(phone)


    def output(self):
        print(self.name, self.age, self.phone)

p1 = Person()
p1.append("장길산", 11, "010-1234-5678")

p2 = Person()
p1.append("김종서",13, "010-0000-00001")

p1.output()
p2.output()

"""
주급 : 이름, 시간당급여액, 근무시간 => 객체지향으로 한사람분만

"""

class Pay:
    def __init__(self, name, pay_per_hour, hours):
        self.name = name
        self.pay_per_hour = pay_per_hour
        self.hours = hours
    def pay(self):
        return self.pay_per_hour * self.hours

    def output(self):
        print(self.name, self.pay_per_hour, self.hours, self.pay())

p1 = Pay("홍길동", 10000, 10)
print(p1.pay())

pList =[
    Pay("홍길동", 10000, 10),
    Pay("임꺽정", 15000, 10),
    Pay("장길산", 12000, 10)
]

for p in pList:
    p.output()

class WeekPayManager:
    def __init__(self):
        self.wList = [
            WeekPay("홍길동", 10000, 10),
            WeekPay("임꺽정", 15000, 10),
            WeekPay("장길산", 12000, 10)
        ]  # 클래스 공통 공간

    def output(self):
        for w in self.wList:
            w.output()

mgr = WeekPayManager()
mgr.output()
