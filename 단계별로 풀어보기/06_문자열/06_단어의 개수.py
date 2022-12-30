import sys 

sentence = sys.stdin.readline().strip() # sentence < 1,000,000

if len(sentence) == 0 : 
    print(0)
    sys.exit()

# 단어의 개수 (공백 + 1)
cnt = 1

for elem in sentence : 
    if elem == ' ' :
        cnt += 1

print(cnt)