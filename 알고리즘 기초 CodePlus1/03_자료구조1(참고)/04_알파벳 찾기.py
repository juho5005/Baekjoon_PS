import sys 
s = sys.stdin.readline().rstrip() 
# s <= 100, 알파벳은 소문자로 구성

# 단어에 포함된 경우, 첫 등장 위치 출력
# 단어에 포함되지 않은 경우, -1 출력

alphas = [
    chr(i)
    for i in range(ord('a'), ord('z') + 1)
]

for elem in alphas : 
    print(s.find(elem), end = ' ')