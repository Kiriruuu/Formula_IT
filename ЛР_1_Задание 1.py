numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = 0
for number in numbers:
    if number is not None:
        total_sum += number
len_of_numbers = len(numbers)
average_of_numbers = total_sum / len_of_numbers
numbers [4] = average_of_numbers
print("Измененный список:",numbers)

"""
(Через исключение индекса не получалось получить верное значение для ср.арифм. значения, поэтому пришлось использовать цикл "for")
skip_index = 4
sum_of_numbers = sum(numbers[:skip_index])
len_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / len_of_numbers
numbers [4] = average_of_numbers
print("Измененный список:",numbers)
"""
