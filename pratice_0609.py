class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드를 가리키는 포인터

    def append(self, data):
        new_node = Node(data)  # 새 노드를 만든다
        if self.head is None:  # 리스트가 비어 있다면?
            self.head = new_node  # head가 이 노드를 가리키게
            return
        curr = self.head
        while curr.next:  # 마지막 노드까지 이동
            curr = curr.next
        curr.next = new_node  # 마지막 노드의 next에 새 노드 연결
    
    def delete(self, target):
        curr = self.head
        prev = None
        while curr:
            if curr.data == target:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next
    
    def print_all(self):
        curr = self.head  # 현재 노드를 head로 설정
        while curr:  # 리스트의 끝까지 반복
            print(curr.data, end=" → ")  # 현재 노드의 데이터를 출력
            curr = curr.next  # 현재 노드를 다음 노드로 업데이트
        print("None")  # 리스트의 끝을 나타내는 표시


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.print_all()        # 1 → 2 → 3 → None

ll.delete(2)
ll.print_all()        # 1 → 3 → None

#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def print_all(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

print("🟢 뒤집기 전:")
ll.print_all()   # 출력: 1 → 2 → 3 → None

ll.reverse()     # 리스트 뒤집기 실행

print("🔁 뒤집은 후:")
ll.print_all()   # 출력: 3 → 2 → 1 → None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def insert_at(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.haad
            self.head = new_node
            return
        
        curr = self.head
        count = 0
        while curr:
            if count == index - 1:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            count+=1
        
        raise IndexError("Index out of range")
    
    def print_all(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at(self, index, value):
        new_node = Node(value)  # 새 노드를 만든다

        # 1. 맨 앞에 삽입
        if index == 0:
            new_node.next = self.head  # 새 노드의 다음을 현재 head로
            self.head = new_node  # head를 새 노드로 변경
            return

        # 2. 중간 삽입
        curr = self.head
        count = 0
        while curr:
            if count == index - 1:  # 삽입할 위치의 바로 앞 노드를 찾으면
                new_node.next = curr.next  # 새 노드의 다음을 현재 노드의 다음으로
                curr.next = new_node  # 현재 노드의 다음을 새 노드로
                return
            curr = curr.next
            count += 1

        raise IndexError("Index out of range")  # 인덱스가 범위를 벗어나면 오류 발생

    def print_all(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")

# 🧪 테스트 코드
ll = LinkedList()
ll.append(10)
ll.append(30)

ll.insert_at(1, 20)  # 인덱스 1에 20 삽입: 10 → 20 → 30
ll.insert_at(0, 5)   # 인덱스 0에 5 삽입: 5 → 10 → 20 → 30
ll.print_all()       # 리스트 출력: 5 → 10 → 20 → 30 → None
