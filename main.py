import random

a = random.randint(0, 10)
print("Я загадал число от 0 до 10, у тебя 3 попытки")
count = 3
while count != 0:
    b = int(input("Введи число: "))
    if a == b:
        print("Молодец")
        break
    elif a < b:
        print("Бери меньше")
        count -= 1
    elif a > b:
        print("Бери больше")
        count -= 1
if count == 0:
    print("У тебя закончились попытки, а я загадал число: ", a)