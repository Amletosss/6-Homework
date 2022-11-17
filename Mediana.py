print('Task 4')
print('Введите последовательность целых чисел через пробел')
import statistics
entered_list = input().split()
elements_int = map(int, entered_list)
elements = list(elements_int)
length = len(elements)
sorted_elements = sorted(elements)
print('Отсортированный список: ', sorted_elements)
print('Медиана списка (нахождение с помощью модуля statistics: ', statistics.median(elements))

if length % 2 == 1:
    mid_index = length // 2
    print('Медиана списка: ', sorted_elements[mid_index])
else:
    left_mid_index = (length // 2) - 1
    right_mid_index = (length // 2)
    mid_of_list = (sorted_elements[left_mid_index] + sorted_elements[right_mid_index]) / 2
    print('Медиана списка: ', mid_of_list)


