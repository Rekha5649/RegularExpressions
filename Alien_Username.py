import re

pattern = r'^[_.]\d+[a-zA-Z]*_?$'

n = int(input())

strings = [input() for _ in range(n)]

for string in strings:
    if re.search(pattern, string):
        print('VALID')
    else:
        print('INVALID')