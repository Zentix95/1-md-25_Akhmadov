def sp1():
    spisok = [1, 3, 2, 4, 5]
    a = int(input('Введите число '))
    if a in spisok:
        print('Поздравляю, Вы угадали число!')
    else: print('Нет такого числа!')

print(sp1())
