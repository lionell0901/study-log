# 자판기 => 객체 지향
# can I take coffee?
# I want to drink

# class 활용해서

# 1. 음료 -> 콜라, 환타, 사이다, 웰치스, 밀키스, 포카리스웨트
# 2. 과자 -> 새우깡, 포카칩, 치토스, 양파링, 초코송이

# 전체 시나리오
# 과자 or 음료 선택할 수 있도록 한다.
# 과자나 음료 목록이 활성화된다.(목록에는 상품명과 돈)
# 동전을 넣으면 동전 값 입력 받고, 거스름돈 돌려준다.
# 총 10회가 지나가면 재료 소진으로 주문을 받지 않는다.

class VendingMachine:
    def __init__(self): # 초기화 함수 생성자
        self.money = 0
        self.drink_list = {
            "콜라": 1000,
            "환타": 1000,
            "사이다": 1000,
            "웰치스": 1200,
            "밀키스": 1300,
            "포카리스웨트": 1500
        }
        self.snack_list = {
            "새우깡": 1000,
            "포카칩": 1200,
            "치토스": 1000,
            "양파링": 1000,
            "초코송이": 1000,
            "오징어땅콩": 1500
        }
        self.drink_stock = {drink: 10 for drink in self.drink_list}
        self.snack_stock = {snack: 10 for snack in self.snack_list}
        self.purchase_history = []  # 구매 내역 저장

    def insert_coin(self, coin): # 동전 투입 함수
        self.money += coin
        print(f"투입된 동전: {coin}원")
        print(f"현재 잔액: {self.money}원")

    """
    def insert_coin(self, coin):
        self.money += coin
        print(f'투입된 동전: {coin}원')
        print(f'현재 잔액: {self.money}원')
    """

    def select_drink(self): # 음료 선택 함수
        print("음료 목록을 보고 원하는 음료의 번호를 선택하세요:")
        for index, (drink, price) in enumerate(self.drink_list.items(), start=1):
            print(f"{index}. {drink} - {price}원 (재고: {self.drink_stock[drink]}개)")
        while True:
            try:
                choice = int(input("음료 번호를 선택하세요: ")) - 1
                drink = list(self.drink_list.keys())[choice]
                price = self.drink_list[drink]
                break
            except (IndexError, ValueError):
                print("목록에 있는 번호를 다시 선택해 주세요.")
        
        if self.drink_stock[drink] > 0:
            print(f"{drink} 선택 - 가격: {price}원")
            coin = int(input("동전을 투입하세요: "))
            self.insert_coin(coin)
            while self.money < price:
                print("잔액이 부족합니다. 추가로 동전을 투입하세요.")
                coin = int(input("추가로 동전을 투입하세요: "))
                self.insert_coin(coin)
            self.money -= price
            self.drink_stock[drink] -= 1
            self.purchase_history.append((drink, price))  # 구매 내역에 추가
            print(f"{drink}가 제공되었습니다. 남은 잔액: {self.money}원")
        else:
            print(f"{drink}의 재고가 소진되었습니다.")

    def select_snack(self): # 과자 선택 함수
        print("과자 목록을 보고 원하는 과자의 번호를 선택하세요:")
        for index, (snack, price) in enumerate(self.snack_list.items(), start=1):
            print(f"{index}. {snack} - {price}원 (재고: {self.snack_stock[snack]}개)")
        while True:
            try:
                choice = int(input("과자 번호를 선택하세요: ")) - 1
                snack = list(self.snack_list.keys())[choice]
                price = self.snack_list[snack]
                break
            except (IndexError, ValueError):
                print("목록에 있는 번호를 다시 선택해 주세요.")
        
        if self.snack_stock[snack] > 0:
            print(f"{snack} 선택 - 가격: {price}원")
            coin = int(input("동전을 투입하세요: "))
            self.insert_coin(coin)
            while self.money < price:
                print("잔액이 부족합니다. 추가로 동전을 투입하세요.")
                coin = int(input("추가로 동전을 투입하세요: "))
                self.insert_coin(coin)
            self.money -= price
            self.snack_stock[snack] -= 1
            self.purchase_history.append((snack, price))  # 구매 내역에 추가
            print(f"{snack}가 제공되었습니다. 남은 잔액: {self.money}원")
        else:
            print(f"{snack}의 재고가 소진되었습니다.")
    
    def get_change(self): # 거스름돈 반환 함수
        change = self.money
        self.money = 0
        return change
    
    def get_drink_list(self): # 음료 목록 반환 함수
        return self.drink_list
    
    def get_snack_list(self): # 과자 목록 반환 함수
        return self.snack_list
    
    def get_drink_price(self, drink): # 음료 가격 반환 함수
        return self.drink_price[drink]
    
    def get_snack_price(self, snack): # 과자 가격 반환 함수
        return self.snack_price[snack]
    
    def get_drink_stock(self, drink): # 음료 재고 반환 함수
        return self.drink_stock[drink]
    
    def show_drink_list(self): # 음료 목록 출력 함수
        print("음료 목록:")
        for drink, price in self.drink_list.items():
            print(f"{drink} - {price}원")
    
    def show_snack_list(self): # 과자 목록 출력 함수
        print("과자 목록:")
        for snack, price in self.snack_list.items():
            print(f"{snack} - {price}원")
    
    def show_drink_stock(self): # 음료 재고 출력 함수
        print("음료 재고:")
        for drink in self.drink_list:
            print(f"{drink} - {self.get_drink_stock(drink)}개")
    
    def show_snack_stock(self): # 과자 재고 출력 함수
        print("과자 재고:")
        for snack in self.snack_list:
            print(f"{snack} - {self.get_snack_stock(snack)}개")
    
    def drink_order(self, drink): # 음료 주문 함수
        if drink in self.drink_list:
            print(f"{drink} 주문")
        else:
            print("해당 음료가 없습니다.")
    
    def snack_order(self, snack): # 과자 주문 함수
        if snack in self.snack_list:
            print(f"{snack} 주문")
        else:   
            print("해당 과자가 없습니다.")
    
    def show_purchase_history(self): # 구매 내역 출력 함수
        if self.purchase_history:
            print("구매 내역:")
            total_spent = 0
            for item, price in self.purchase_history:
                print(f"- {item}: {price}원")
                total_spent += price
            print(f"총 지출 금액: {total_spent}원")
        else:
            print("구매 내역이 없습니다.")
    
    def main(self): # 메인 함수
        while True:
            print("\n메뉴를 선택하세요:")
            print("1. 음료 선택")
            print("2. 과자 선택")
            print("3. 거스름돈 반환")
            print("4. 구매 내역 출력")
            print("5. 종료")
            choice = int(input("번호를 선택하세요: "))
            if choice == 1:
                self.select_drink()
            elif choice == 2:
                self.select_snack()
            elif choice == 3:
                print(f"거스름돈: {self.get_change()}원")
            elif choice == 4:
                self.show_purchase_history()
            elif choice == 5:
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 번호를 입력했습니다. 다시 선택해 주세요.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.main()