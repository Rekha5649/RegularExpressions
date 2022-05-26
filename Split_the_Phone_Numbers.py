import re
N = int(input())

phoneNum = list()
for _ in range(N):
    phoneNum.append(input())

for i in phoneNum:
    CountryCode, LocalAreaCode, Number = re.split('[- ]', i)
    print(f'CountryCode={CountryCode},LocalAreaCode={LocalAreaCode},Number={Number}')