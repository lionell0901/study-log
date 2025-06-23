# # for i in [1,2,3,4,5,6,7,8,9,10]:
# #     print(i)

# for i in [1,2,3,4,5,6,7,8]:
#     print(i)

# # #range(시작, 종료, 증감치) 시작값부터 시작해서 종료값 -1까지 증감치를 가지고 생성해낸다.
# # print(range(1,11))

# for i in range(100, 1, -10):
#     print(i)
#     if i%3 == 0:
#         print()

# # for i in range(1,11):
# #     print(i)

# # a = list(range(1,11))
# # print(a)

# #  100부터 시작해서 0까지 짝수를 나열하라
# # for i in range(100,1,-2):
# #     print(i)

# # #문제1 1,2,3,4,5,6,7,8,9,10 줄바꿈
# # #     11 12 13 14 ....

# # for i in list(range(1,101)):
# #     print(i, = ' ')
# #     if i%10 ==0:
# #         print()

# #문자의 unicode -> ord
# print(ord('A')) #유니코드 65
# print(ord('B')) #유니코드 66
# print(ord('a'))end #유니코드 97
# print(ord('b')) #유니코드 98
# print(ord('z')) #유니코드 122
# print(ord('0')) #유니코드 48
# print(ord('1')) #유니코드 49
# print(ord('9'))

# #코드값을 주면 문자로 chr(코드값)
# print(chr(48))
# print(chr(49))
# print(chr(50))
# print(chr(66))

#for문을 써서 알파벳 a~z까지 출력
# for i in range(ord('A'),ord('Z')+1):
#     print(chr(i), end=' ')
# print()

#키보드로부터 문장을 입력받아서 각 문장의 개수 / 대소문자 구분 X
# A ===> 5
# B ===> 0
# count = [,0,0,0,0,0, 26개 알파벳]

# 강사님 1번 방법
# sentence = input("문장 입력 : ")
# count = [0] * 26  # A~Z 각각의 개수 저장

# for i in sentence:
#     if 'A' <= i <= 'Z':  # 대문자
#         count[ord(i) - ord('A')] += 1
#     elif 'a' <= i <= 'z':  # 소문자
#         count[ord(i) - ord('a')] += 1

# for i in range(26):
#     print(f"{chr(i + ord('A'))} ===> {count[i]}")


#강사님 2번 방법(dict 타입) 'A'존재 안하면 하나 만들고 1 존재하면 +1
sentence = input("문장입력:")
result = {}
for i in sentence.lower():
    if i in result.keys():
        result[i]+=1
    else:
        result[i]=1
for item in result.items():
    print(item)

# result = {}
# for i in sentence.lower():
#     if i in result.keys():
#         result[i]+=1
#     else:
#         result[i]=1
# for item in result.items():
#     print(item)

#문장을 입력 받는다.
#대소문자를 찾는다.(대소문자 관계 없이)
#
#대소문자의 개수
