# 문자열 S 중에서 단어만 뒤집으려 함
# 문자열 S는 
# 'a'~'z', '0'~'9', ' ', '<', '>' 로만 이루어짐
# 문자열의 시작과 끝은 공백 x
# '<'와 '>'가 문자열에 있는 경우에는 번갈아가면서 등장 (두 문자의 개수도 같다.)

# 태그 '<'와 '>' 사이에는 알파벳 소문자와 공백만 존재
# 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열
# 연속하는 두 단어는 공백 하나로 구분
# 태그는 단어가 아니고 태그와 단어 사이에는 공백 X

from collections import deque 
import sys 
s = sys.stdin.readline().rstrip() # s <= 100,000
# O(1), O(logN), O(N), O(NlogN)

l = len(s)

string_dq = deque()
tag_dq = deque()

i = 0

while i < l : 
    # tag
    if s[i] == '<' :
        if len(string_dq) != 0 :
            for elm in string_dq : 
                print(elm, end = '')
            string_dq.clear()

        j = i+1
        tag_dq.append(s[i]) 
        
        while s[j] != '>' :
            tag_dq.append(s[j])
            j += 1
        
        tag_dq.append(s[j]) # append '>'
        i = j+1 

        for elem in tag_dq : 
            print(elem, end ='')
        tag_dq.clear()
    
    elif s[i] == ' ' :
        for elem in string_dq : 
            print(elem, end='')
        string_dq.clear()
        print(' ', end = '')
        i += 1
    
    else :
        string_dq.appendleft(s[i])
        i += 1 

if len(string_dq) != 0 :
    for elem in string_dq : 
        print(elem, end ='')