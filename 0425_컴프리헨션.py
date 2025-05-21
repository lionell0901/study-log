# # 스택하고 힙을 시스템이 프로세스한테 할당한다.
# # 스택에는 변수 자신이 저장된다.
# # 힙에는 데이터가 저장된다. 저장된 주소를 변수한테 전달
# # a(100번지) ===========> (1,2,3,4,5,6,7,8,9,10)
# # b = a : 동일한 데이터 공간을 공유한다
# # b(100번지)
# # b라는 메모리 공간을 스택에 만들고,a의 값(데이터가 있는 곳의 주소)을 복사한다. -> 소프트 카피
# # 소프트 카피의 목적은 메모리 절약, 쓸데없는 복사과정(overhead)이 필요 없다.
# # 하드 카피, 깊은 카피의 경우 직접 구현하거나 deepcopy 모듈을 사용하거나 컴프리헨션을 사용한ㄷ,

# b = [] #새로 기억공간을 만든다.
# for item in a: #a로부터 데이터를 하나씩 가져와서 item 이라는 변수에 저장한다.
#     b.append(item)
# b[3]= 99
# print(a)
# print(b)

# #컴프리헨션 :리스트 복사 [변수명 for 변수명 in 리스트형변수]
# c = [item for item in a] #하드카피
# c[5] = 55
# print("a=", a)
# print("c=, c")

# d = [item*2 for item in a]
# print("d=", d)

# #조건을 부여할 수도 있다. [변수명 for 변수명 in 리트스함수 if 변수명>)
# #짝수와 홍
# ood.list = [X for in a i a a
            
# word_list = ["rain"], [desk], [python, cloud, java, html]

# #1 복사 - 하드카피

# word_list = [w for in word_list]
# print(wokrd_list)

# #복사하면서 대문자로 바꾸고 싶다.
# word_list3= (va
             
# #단어와 단어길이
# word_list3 = [(w, len(w)) for w in word_list]
# print(word_list3)

# ------- 아래는 AI
a = [1,2,3,4,5,6,7,8,9,10]

# 얕은 복사 (소프트 카피처럼 보이지만 숫자니까 괜찮음)
b = []
for item in a:
    b.append(item)
b[3] = 99
print("a =", a)
print("b =", b)

# 하드카피 느낌
c = [item for item in a]
c[5] = 55
print("a =", a)
print("c =", c)

# 값 2배
d = [item * 2 for item in a]
print("d =", d)

# 짝수만 고르기
even_list = [x for x in a if x % 2 == 0]
print("even_list =", even_list)

# 단어 리스트
word_list = ["rain", "desk", "python", "cloud", "java", "html"]

# 복사
word_copy = [w for w in word_list]
print("word_copy =", word_copy)

# 대문자로 바꾸기
word_upper = [w.upper() for w in word_list]
print("대문자 리스트 =", word_upper)

# 단어와 길이 튜플로 만들기
word_len_pair = [(w, len(w)) for w in word_list]
print("단어와 길이 =", word_len_pair)


#단어길이가 5글자 이상인 것만 
word_list = [w for w in word_list if len(w)>=5]
print(word_list)

#[변형할값 for 변수 in 리스트 if 조건]

#문제1. 단어중에 java라는 단어가 있는것만 추출하기
word_list = [w for w in word_list if w == "java"]
print(word_list)
#문제2. 단어중에 길이가 5개보다 짧은 java라는 단어가 있는 것만 추출하기
word_list = [w for w in word_list if len(w) < 5 and w == "java"]
print(word_list)