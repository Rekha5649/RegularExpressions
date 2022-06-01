import re

pattern = r"<\s*(\w+)\s*.*?>"

N = int(input())
html_lines = list()
tags = set()
for _ in range(N):
    html_lines.append(input())
    
for line in html_lines:
    tags.update(set(re.findall(pattern, line)))
    
for i in ';'.join(sorted(list(tags))):
    print(i,end='')