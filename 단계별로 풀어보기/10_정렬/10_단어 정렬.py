import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 20,000

# 주어지는 문자열의 길이는 50을 넘지 않는다.
# +) 중복 제거 
# 1) 짧은 것 부터
# 2) 길이가 같으면 사전 순으로


word_lst = []
for _ in range(n) :
    word_lst.append(sys.stdin.readline().rstrip())

word_lst = list(set(word_lst))
word_lst.sort(key=lambda data:(len(data), data)) 

for elem in word_lst :
    print(elem)