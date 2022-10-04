# Задача №1

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

list = [int(input("Введите значения в список: ")) for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {list}')
print(sum(list[i] for i in range(1, len(list), 2))) """


# Задача №2

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

list = [int(input("Введите значения в список: ")) for i in range(int(input('Введите длину списка: ')))]
for i in range(len(list) // 2 + len(list) % 2):
    print(list[i] * list[-(i + 1)]) """


#Задача №3

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

lst = [float(input("Введите значения в список: ")) for i in range(int(input('Введите длину списка: ')))]

lst = ['.' + str(item).split('.')[1] for item in lst]
lst = list(map(float, lst))
print(max(lst) - min(lst)) """


# Задача № 4

""" n = int(input("Введите искомое число в двоичной системе счисления: "))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(f"Указанное Вами число в десятичной системе счисления равняется {b}") """

# Задача № 4 (еще раз...)

""" n = int(input("Введите искомое число в двоичной системе счисления: "))
print(bin(n))
 """

 # Задача № 5

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

fib1 = fib2 = 1
n = int(InputNumbers("Введите число:"))
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end= ' ') """