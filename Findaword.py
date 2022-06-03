import re

N = int(input())

sentences = ' '.join(input() for _ in range(N))

words = [input() for _ in range(int(input()))]


for word in words:
    pattern = rf'\b{word}\b'
    print(len(re.findall(pattern, sentences)))