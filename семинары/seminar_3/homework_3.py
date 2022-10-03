# Задача №1

def InputNumbers(inputText):
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
print(sum(list[i] for i in range(1, len(list), 2)))