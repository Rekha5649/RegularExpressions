import re

N = int(input())

html_doc = ' '.join(input() for _ in range(N))
domains = set()

pattern = r'https?:\/\/(?:ww[w2]\.)?(([A-Za-z0-9-]+\.)+([A-Za-z-]+))'


matches = re.findall(pattern, html_doc)
domain = ';'.join(sorted(list({d[0].strip() for d in matches})))
print(domain)
