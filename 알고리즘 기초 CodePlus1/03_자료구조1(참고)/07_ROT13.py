# 영어 알파벳을 13글자씩 밀어서 만드는 것
# 암호화한 문자열을 다시 원래대로 바꾸려면 
# 다시 ROT13을 진행하면 된다.

# 대문자, 소문자, 공백, 숫자로 이루어진 문자열 S
import sys 
s = sys.stdin.readline().rstrip() # s <= 100 
# O(N^4)

def ROT13(string) :
    if string == ' ' or string.isdigit() :
        return string

    elif string.isupper() : 
        changed = ord(string) + 13 
        if changed > ord('Z') :
            changed = ord(string) - 13
        
        return chr(changed)
    
    elif string.islower() :
        changed = ord(string) + 13 
        if changed > ord('z') :
            changed = ord(string) - 13
        
        return chr(changed)

for elem in s :
    print(ROT13(elem), end ='')