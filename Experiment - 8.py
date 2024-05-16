import re
s = input("Enter a string: ")
p = input("Enter a pattern: ")
print(re.findall(re.compile(p), s))
