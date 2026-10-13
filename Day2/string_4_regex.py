
import re

text = input("Enter a string: ")

digits = re.findall(r'\d', text)

if digits:
    print("Digits found in the string:", digits)
else:
    print("No digits found in the string.")
