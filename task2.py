import re

file_path = 'task2.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'\b\d+px\b'

matches = re.findall(pattern, content)

print("Все значения в пикселях:")
for match in matches:
    print(match)


