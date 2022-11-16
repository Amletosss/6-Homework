print('Task 1')
print('Введите последовательность целых чисел через пробел')
entered_list = input().split()
elements_int = map(int, entered_list)
elements = list(elements_int)
number = 0
multiplication = 1

if not elements:
    print('Список пуст! Произведение равно 0.')

else:
    for i in range(len(elements)):
        if i % 2 == 0:
            number += elements[i]

multiplication = number * elements[-1]
print('Ваш список: ', elements)
print('Произведение последнего с четными = ', multiplication, '\n')