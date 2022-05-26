import re
import sys

line = list()
UK_words = list()
N = int(input())
for _ in range(N): 
    line.append(input())
T = int(input())
for _ in range(T): 
    UK_words.append(r'\b'+input().replace('our', 'ou?r')+r'\b')
    
for i in range(T):
    num = 0
    for j in range(N):
        num += len(re.findall(UK_words[i], line[j]))
    print(num)