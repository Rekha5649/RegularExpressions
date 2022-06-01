import re

n = int(input())

sentence = ' '.join(input() for _ in range(n))

q=int(input())
query = list()
for i in range(q):
    query.append(input().strip())
    
for i in query:
    pattern = r"(?<=\w)"+'('+i+')'+"(?=\w)"
    print(len(re.findall(pattern, sentence)))
    