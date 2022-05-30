# Enter your code here. Read input from STDIN. Print output to STDOUT 
import re

pattern = r"^[Hh][iI]\s[^Dd]"

n = int(input())
sen = list()
for i in range(n):
    sen.append(input())
    
for s in sen:
    if(re.findall(pattern, s)):
        print(s)
    
    