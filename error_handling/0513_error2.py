try:
    f = open("file.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
except FileExistsError as e:
    print(e)
finally:
    f.close()