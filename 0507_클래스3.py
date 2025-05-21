class Book:
    title = "채식주의자"
    def __init__(self,title="홍길동전", paramprice=10000):
        print("self:",self) #객체주소
        self.title = title  #self를 이용해서 
        self.price = paramprice
        self.count = 20
        self.process() #함수도 매개변수로 self를 받아가야 한다.
    def process(self):
        self.total_price = self.price * self.count
    def output(self):
        print(self.title, self.price, self.count, self.total_price)
    pass


#title이라는 클래스 내부 변수에 접근하려면 접근 연산자로
b = Book("어린왕자") #객체가 만들어진다
print(b)
print(b.title)
b.process()
b.output()

b2 = Book("아 지갑놓고 나왔다.")
print(b2)
b2.output()

b3= Book("사피엔스")
print(b3)
print(b3.title)
b3.output()