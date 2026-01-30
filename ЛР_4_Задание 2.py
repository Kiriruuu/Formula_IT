# TODO импортировать необходимые молули
from collections import OrderedDict
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        rows = [OrderedDict(row) for row in reader]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
         json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
