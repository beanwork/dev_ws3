import re

current_txt = "8.555*5"

numbers = re.findall(r'\d+', current_txt)
operators = re.findall(r'[+\-*/]', current_txt)

print(numbers)
print(operators)