# 스택 (Stack): Last-In, First-Out (LIFO) 원칙을 따르는 자료 구조입니다. 가장 마지막에 삽입된 요소가 가장 먼저 제거되는 특징을 가집니다.
# 인터럽트 (Interrupt): CPU가 현재 실행 중인 작업을 일시 중단하고,
# 우선순위가 높은 다른 작업을 먼저 처리하도록 하는 신호입니다. 이를 통해 컴퓨터는 여러 작업을 효율적으로 관리할 수 있습니다.
# 컴퓨터 처리 사이클: 기본적인 컴퓨터 작업 처리 과정은 입력(데이터 읽기) -> 처리(계산 및 데이터 조작) -> 출력(결과 표시)의 순서로 이루어집니다.
# 이를 명령어 사이클(Instruction Cycle)이라고도 합니다.
# CPU 작업과 인터럽트: CPU는 할당된 작업을 지속적으로 수행하며, 키보드 입력, 마우스 클릭과 같은 외부 장치의 요청이나
# 특정 이벤트 발생 시 인터럽트가 발생하여 해당 작업을 우선적으로 처리합니다.
# 함수 (Function): 특정 작업을 수행하기 위해 미리 정의된 코드 블록입니다. 함수를 사용하면 코드의 재사용성을 높이고,
# 프로그램을 논리적인 단위로 나누어 관리하기 용이하게 만들어 가독성과 유지보수성을 향상시킵니다.
# 수식 트리 (Expression Tree): 수식을 트리 형태로 표현한 것입니다. 
# 연산자는 내부 노드에, 피연산자는 단말 노드에 위치하며, 중위, 전위, 후위 표기법으로 변환하거나 수식 계산에 활용됩니다.
# 트리 순회 (Tree Traversal): 트리의 모든 노드를 한 번씩 방문하는 방법입니다. 
# 대표적으로 전위 순회(Pre-order), 중위 순회(In-order), 후위 순회(Post-order) 방식이 있습니다.
# 0-주소 명령어 (Zero-Address Instruction): 연산 시 필요한 피연산자의 주소를 명시적으로 
# 지정하지 않는 명령어 형식입니다. 스택 기반의 컴퓨터 구조에서 주로 사용되며, 연산은 스택의 최상단 데이터들을 대상으로 이루어집니다.
# 스택의 기본 연산:
# push: 스택의 가장 윗부분(top)에 데이터를 추가하는 연산입니다.
# pop: 스택의 가장 윗부분(top)에서 데이터를 제거하고 그 값을 반환하는 연산입니다.
# peek (또는 top): 스택의 가장 윗부분(top)에 있는 데이터를 제거하지 않고 그 값을 반환하는 연산입니다.
# isFull: 스택이 가득 찼는지 여부를 확인하는 연산입니다. (배열 등으로 구현 시 크기 제한이 있을 경우 필요)
# isEmpty: 스택이 비어있는지 여부를 확인하는 연산입니다.
# 내부 데이터를 배열로 둔다.
# [0,0,0,0,0,0,0,0,0,0] 0 1 2 3 4 5 5 6 7 8 9
# top 인덱스 - 스택의 마지막 데이터를 가리킨다.

# 스택 구현을 위한 아이디어:
# - 내부 데이터를 저장하기 위해 리스트(배열)를 사용합니다.
# - 예시: [0,0,0,0,0,0,0,0,0] -> 각 인덱스 0, 1, 2, ..., 8, 9 에 해당하는 요소
# - top 인덱스: 스택의 가장 마지막 데이터(가장 위에 있는 데이터)의 위치를 가리키는 변수입니다.
#   스택이 비어있을 경우 보통 -1로 초기화합니다.

class MyStack:
    # MyStack 클래스 생성자(초기화 메서드)
    def __init__(self, size=10): # 스택의 크기를 매개변수로 받으며, 기본값은 10입니다.
        # 최소 스택 크기를 10으로 설정합니다.
        if size < 10:
            self.size = 10 # 사용자가 10보다 작은 값을 입력하면 최소 크기인 10으로 강제합니다.
        else:
            self.size = size # 그 외의 경우에는 사용자가 입력한 크기를 사용합니다.
        
        # 스택으로 사용할 리스트를 초기화합니다.
        self.stack=[] 
        # 지정된 크기만큼 0으로 채워진 리스트를 생성합니다.
        for i in range(0, size): # append를 size만큼 반복하여 리스트를 만듭니다.
            self.stack.append(0) # 모든 요소를 0으로 초기화합니다. (실제 사용 시 push될 값으로 덮어쓰여짐)
        
        # 스택의 top을 초기화합니다. top은 가장 최근에 추가된 데이터의 인덱스를 나타냅니다.
        # 스택이 비어있을 때는 -1로 설정하여, 첫 번째 데이터가 인덱스 0에 저장되도록 합니다.
        self.top = -1
    
    # 스택이 가득 찼는지 확인하는 메서드
    def isFull(self):
        # top이 스택의 마지막 인덱스(size - 1)와 같다면 스택은 가득 찬 상태입니다.
        if self.size-1 == self.top:
            return True # 가득 찼으면 True 반환
        else:
            return False # 그렇지 않으면 False 반환
    
    # 스택에 데이터를 추가하는 push 메서드
    # 데이터가 isFull상태가 아니면 top 증가시키고 그 안에 값 넣기 (isFull 체크 후 실행)
    def push(self, data):
        # 스택이 가득 찼는지 먼저 확인합니다.
        if self.isFull():
            #print("스택이 꽉 찼습니다!") # 사용자에게 알림 (필요시 주석 해제)
            return # 가득 찼으면 아무 작업도 하지 않고 함수를 종료합니다.
        
        # 스택이 가득 차지 않았다면 top을 1 증가시킵니다.
        self.top +=1 
        # 증가된 top 위치에 새로운 데이터를 저장합니다.
        self.stack[self.top]=data
    
    # 스택의 내용을 출력하는 메서드 (디버깅 또는 확인용)
    def print(self):
        i=0
        # 스택의 처음부터 top까지 저장된 모든 데이터를 출력합니다.
        while i <= self.top: # top이 가리키는 위치까지 반복합니다.
            print(self.stack[i], end=" ") # 데이터를 한 줄에 공백으로 구분하여 출력합니다.
            i+=1
        print() # 모든 데이터 출력 후 줄바꿈
    
    # 스택이 비어있는지 확인하는 메서드
    def isEmpty(self):
        # top이 -1이면 (초기 상태이거나 모든 데이터가 pop된 상태) 스택은 비어있습니다.
        if self.top == -1:
            return True # 비어있으면 True 반환
        return False # 그렇지 않으면 False 반환 (데이터가 하나라도 있으면 False)
    
    def pop(self):
        if self.isEmpty():
            return None
        item = self.stack[self.top]
        self.top-=1
        return item
    
    # 스택의 가장 윗부분(top) 데이터를 확인하는 peek 메서드
    def peek(self):
        # 스택이 비어있는지 먼저 확인합니다.
        if self.isEmpty():
            #print("스택이 비어있습니다.") # 사용자에게 알림 (필요시 주석 해제)
            return None # 비어있으면 None을 반환하여 데이터가 없음을 알립니다.
        # 스택이 비어있지 않으면 top 위치의 데이터를 반환합니다. (데이터를 제거하지 않음)
        return self.stack[self.top]
        self.top -= 1
        return item
    
def reverse(arr):
    s = MyStack(len(arr))
    for i in arr:
        s.push(i)
    result = ""
    while not s.isEmpty():
        result += s.pop()
    return result
    
    
# 이 스크립트 파일이 직접 실행될 때 아래 코드를 실행합니다. (프로그램의 시작점)
if __name__ == "__main__":
    s1 = MyStack() # 기본 크기(10)로 MyStack 객체 생성
    s1.push(5)     
    s1.push(6)
    s1.push(7)
    s1.push(8)
    s1.push(9)
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)    # 스택 크기가 10이므로, 이 값(인덱스 9)까지 정상적으로 push 됩니다.
    s1.push(6)    # isFull() 조건에 의해 이 push는 실행되지 않습니다 (무시됨).
    s1.push(7)    # isFull() 조건에 의해 이 push는 실행되지 않습니다 (무시됨).
    s1.push(8)    # isFull() 조건에 의해 이 push는 실행되지 않습니다 (무시됨).
    s1.push(8)    # isFull() 조건에 의해 이 push는 실행되지 않습니다 (무시됨).
    s1.push(2)    # isFull() 조건에 의해 이 push는 실행되지 않습니다 (무시됨).
    print("------------------------------------")
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    s1.print()    # 스택 내용 출력 (결과: 5 6 7 8 9 1 2 3 4 5)   
    
    print(reverse("korea"))
    #스택을 사용하여 문자열뒤집기
    #se = MyStack(30)