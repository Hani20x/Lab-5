import re
import csv

id_pattern = re.compile(r"\b\d+\b")
surname_pattern = re.compile(r"\b[A-Z][a-z]+\b")
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
date_pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
website_pattern = re.compile(r"https?://[^\s]+")

with open('task3.txt', 'r', encoding='utf-8') as file:
    content = file.read()

ids = id_pattern.findall(content)
surnames = surname_pattern.findall(content)
emails = email_pattern.findall(content)
dates = date_pattern.findall(content)
websites = website_pattern.findall(content)

rows = zip(ids, surnames, emails, dates, websites)

output_file = 'result.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ID", "Фамилия", "Электронная почта", "Дата регистрации", "Сайт"])
    csvwriter.writerows(rows)

print(f"Данные успешно сохранены в {output_file}.")
