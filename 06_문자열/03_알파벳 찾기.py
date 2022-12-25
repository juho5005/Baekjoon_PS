import sys 

sentences = sys.stdin.readline().rstrip() # 단어 S

# a ~ z가 "처음" 등장하는 위치를 공백으로 구분하여 출력
# 단어에 포함돼 있지 않다면 -1 출력
# 단어의 첫 번째 글자는 0번째 위치, 두 번째 글짜는 1번째 위치 

alps = []

# a~z 알파벳의 배열 생성
for i in range(97, 123) :
    alps.append(chr(i))

res = []
for elem in alps : 
    finish = False 
    for (pos,sentence) in enumerate(sentences) : 
        if elem == sentence :
            res.append(pos)
            finish = True
            break 
    
    if not finish : 
        res.append(-1)

print(*res)

