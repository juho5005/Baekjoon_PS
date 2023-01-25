from collections import Counter
import sys

alphas = [
    chr(i)
    for i in range(ord('a'), ord('z')+1)
]

# s(알파벳) <= 100
s = sys.stdin.readline()

s_count = Counter(s)

for alpha in alphas :
    if alpha not in s_count :
        print(0, end = ' ')
    else :
        print(s_count[alpha], end = ' ')