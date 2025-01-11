import re

# Load the file
file_path = "task_add.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Regular expressions
date_pattern = r' (?:(?:\d{1,2}[-/\.]){2}\d{2,4}|\d{4}[-/\.]\d{1,2}[-/\.]\d{1,2})'
email_pattern = r' [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r' https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'

# Find matches
dates = re.findall(date_pattern, content)
emails = re.findall(email_pattern, content)
urls = re.findall(url_pattern, content)

# Extract first 5 matches for each
dates = dates[:5]
emails = emails[:5]
urls = urls[:5]

# Print results
print("Dates:", dates)
print("Emails:", emails)
print("URLs:", urls)
