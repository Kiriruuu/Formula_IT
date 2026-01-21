def find_common_participants(first_group, second_group, separator=','):
    first_set = set(first_group.split(separator))
    second_set = set(second_group.split(separator))

    common_participants = sorted(first_set & second_set)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем отличным от запятой
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|'
)

print(result)
