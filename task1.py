import re

# Открываем файл и читаем его содержимое
with open('task1-en.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Поиск слов, после которых стоит точка
words_with_dot = re.findall(r'\b\w+\.\s', content)

# Поиск дробных чисел
fractional_numbers = re.findall(r'\b\d+\.\d+\b', content)

# Вывод результатов
print("Слова, после которых стоит точка:")
print(words_with_dot)

print("\nДробные числа:")
print(fractional_numbers)