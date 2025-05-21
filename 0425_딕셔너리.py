colors = {"red":"빨강색", "blue":"파랑색", "green":"초록색"}
#키값은 문자열을 주로 사용하고, 만일에 같은 키값을 두번쓰면 두번째꺼로 업데이트한다.

exercise = {"벤치":"가슴", "스쿼트":"하체", "데드리프트":"등"}
for key in exercise:
    print(exercise[key], end = '')
    print(exercise["데드리프트"])
    print(exercise.keys())
    print(exercise.values())
    print(exercise.items())
    exercise["턱걸이"] = "광배근"
    print(exercise)
    exercise["윗몸일으키기"] = "복근"
    print(exercise)
    exercise.pop("턱걸이")
    print(exercise)
    exercise.clear()
    print(exercise)

#인덱싱이나 슬라이싱 불가
print(colors["red"],type(colors))
print(colors["green"])
print(colors["blue"])

print(colors.keys()) #키 값들의 목록을 보여준다.

#추가
colors["black"] = "검은색"
print(colors)
colors["red"] = "빨강"
print(colors)

#없는 키값의 경우 파이썬이 어떻게 동작하는지
if "pink" in colors.keys():
    print(colors["pink"])
else:
    print("pink is not exist")

print(colors.items()) #튜플로 넘겨준다(쌍으로 세트)
print(colors.values()) #값만 가져올 수도 있다
print(colors.keys()) #키값만 가져올수도 있다


#특정키 삭제 - pop(키값)
colors.pop("red")
print(colors)
colors.clear() #전체 삭제
print(colors)


