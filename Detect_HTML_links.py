# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

N = int(input())
html_page = list()

for _ in range(N):
    html_page.append(input())
    
for html in html_page:
    
    # group matches will be returned here
    gr = re.findall(pattern, html)
    
    for link, text in gr:
        print(f'{link},{text.strip()}')