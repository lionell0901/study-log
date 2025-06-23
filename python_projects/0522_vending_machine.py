# 벤딩 머신 만들자
# 처음에 과자랑 음료 선택하자.
# 그리고 목록 보여줘

# 제품 데이터 (딕셔너리 형태로 구성)
products = {
    "과자": {
        "초코파이": 1500,
        "오레오": 2000,
        "초코쿠키": 1000
    },
    "음료": {
        "콜라": 1000,
        "사이다": 1000,
        "환타": 1000
    }
}

def display_items(category_name, items):
    """선택된 카테고리의 제품 목록을 보여줍니다."""
    print(f"\n--- {category_name} ---")
    for i, (item, price) in enumerate(items.items()):
        print(f"{i+1}. {item}: {price}원")
    print("--------------------")

def select_item(category_items):
    """사용자가 제품을 선택하도록 합니다."""
    while True:
        try:
            choice = int(input("원하는 제품의 번호를 선택하세요: "))
            if 1 <= choice <= len(category_items):
                # 사용자가 입력한 번호는 1부터 시작하므로, 리스트 인덱스로 변환 (0부터 시작)
                selected_item_name = list(category_items.keys())[choice - 1]
                selected_item_price = category_items[selected_item_name]
                return selected_item_name, selected_item_price
            else:
                print("잘못된 번호입니다. 다시 선택해주세요.")
        except ValueError:
            print("숫자로 입력해주세요.")

def run_kiosk():
    """자판기 프로그램을 실행합니다."""
    print("환영합니다! 저희 자판기를 이용해주셔서 감사합니다.")

    # 1. 카테고리 선택
    while True:
        print("\n어떤 종류를 원하시나요?")
        print("1. 과자")
        print("2. 음료")
        category_choice = input("번호를 선택하세요 (1 또는 2): ")

        if category_choice == "1":
            selected_category_name = "과자"
            items_to_display = products["과자"]
            break
        elif category_choice == "2":
            selected_category_name = "음료"
            items_to_display = products["음료"]
            break
        else:
            print("잘못된 선택입니다. 1 또는 2를 입력해주세요.")

    # 2. 제품 목록 보여주기
    display_items(selected_category_name, items_to_display)

    # 3. 제품 선택
    chosen_item_name, chosen_item_price = select_item(items_to_display)

    # 4. 선택 결과 보여주기
    print(f"\n선택하신 제품은 '{chosen_item_name}'이고, 가격은 {chosen_item_price}원입니다.")
    print("감사합니다!")

# 프로그램 실행
if __name__ == "__main__":
    run_kiosk()
