choose = int(input("Выберите функцию: 1 - Сложение, 2 - Вычитание, 3 - Деление, 4 - Умножение "))  #Выбор функции
hm = int(input("Введите кол-во чисел ")) #Кол-во чисел
total = int(0)
if (choose == 1): #Сложение
    for i in range(hm):
        num = int(input("Введите число "))
        total = int(total + num)
    print(total)
elif (choose == 2): #Вычитание
    total = int(input("Введите число "))
    for i in range(hm-1):
        num = int(input("Введите число "))
        total = int(total - num)
    print(total)
elif (choose == 3): #Деление
    total = int(input("Введите число "))
    for i in range(hm-1):
        num = int(input("Введите число "))
        if (num != 0):
           total = int(total / num)
        else:
           print("На ноль делить нельзя, он будет проигнорирован")
    print(total)
elif (choose == 4): #Умножение
    total = int(input("Введите число "))
    for i in range(hm-1):
        num = int(input("Введите число "))
        total = int(total * num)
    print(total)
else:
    print("Error")