#for 문안에서 또 for문이 작동하는 경우다.
#외부의 루프가 m번 돌고, 내부 루프가 n번 돌면 m * n번 수행을 한다.
#가급적 2중 for문까지만 동작하게끔 한다.

# for i in range(1,6):
#     for j in range(1,6):
#         print( f"i={i} j={j}")

#문제1. 이중 for문 사용해서 1~100까지 출력하는데 한줄에 10개씩
# k = 1
# for i in range(0,10):
#     for j in range(0,10):
#         print(f"{k}", end="\t")
#         k += 1
#     print() #줄바꿈


## 내가 풀었음(중간에 막힘)
# for i in range(10):
#     for j in range(10):
#         number = i * 10 + j + 1
#     print(i)

#문제2. 이중 for문
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 ,,,, 10까지 더하기

# ###강사님 풀이
# for i in range(1,11):
#     sum = 0
#     for j in range(1,i+1):
#         if j<i:
#             print(j, end = "+")   
#         else:
#             print(j, end = "=")   
#         sum+=j
#     print(sum)

## 내가 풀었음(중간에 막힘)
# j = 1
# for i in range(1,11):
#     total = 0
#     for j in range(1, 1+j):

# for i in range(0,10):
#     print("*" * i)
#     print()

"""
다이아몬드 문제 만들기
             *
            ***
           *****
          *******
           *****
            ***
             *
"""
# 쪼개서 생각해보자. 우선 총 출력할 개수는 7줄이다.
#    *    #공백개수 3개 별 1개  라인1 별의개수는 2n-1 / 공백은 공백+라인=4 공백은 4-라인
#   ***   #공백개수 2개 별 3개  라인2                                   4-라인수
#  *****  #공백개수 1개 별 5개  라인3
# ******* #공백개수 0개 별 7개  라인4
#  *****  #공백개수 1개 별 5개  라인1 별의개수는 (-1)*2+1 =5
#   ***   #공백개수 2개 별 3개  라인2 (공백개수-1)*2 + 1 = 3
#    *    #공백개수 3개 별 1개  라인3 (lines-3)*2 + 1 = 1

###강사 풀이법
#위에처럼 다이아몬드 옆에 일단 풀어주기
#파이썬 특성 살려서 풀어보기
# lines = 7
# for i in range(1, lines+1):
#     print(" "* (lines-i), end="")
#     print("*" * (2*i-1))
# 위에 나머지 풀어보자
#for문으로 풀어보기

lines = 4
for i in range(1, lines+1):
    for j in range(0, (lines-i)):
        print(" ", end="")
    for j in range(0, 2*i-1):
        print("*", end="")
    print()

lines = lines - 1
for i in range(0, lines+1):
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, (lines-i)*2 + 1):
        print("*", end="")
    print()

##나의 풀이법
# n = 4
# total_line = 2 * n - 1
# for row in range(1, total_line+1):
#     space = abs(n - row)
#     stars = 2*(n-space)-1