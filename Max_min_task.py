print('Task 2')
elements = [10.2, -2.2, 0, 1.1]
if not elements:
    print('Список пуст! Произведение равно 0.')
else:
    max_number = max(elements)
    min_number = min(elements)
    difference = max_number - min_number
    print('Массив чисел: ', elements)
    print('Разность max и min значений = ', round(difference, 1), '\n')
