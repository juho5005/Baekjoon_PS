# 팰린드롬 = 앞에서 읽었을 때와 뒤에서 읽었을 때가 같은 문자열
# ex) AAA ABBA ABABA

# 팰린드롬을 판별하는 문제는 재귀함수를 이용해 쉽게 해결 가능
# isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환

# 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

import sys 
t = int(sys.stdin.readline()) # 1 <= T <= 1,000
# O(N^2), O(N^2logN)

# recursion 함수의 호출 횟
cnt = 0 

def recursion(s, l, r) :
    global cnt 
    cnt += 1

    if l >= r :
        return 1
    elif s[l] != s[r] :
        return 0
    else :
        return recursion(s, l+1, r-1) 

def isPalindrome(s) :
    return recursion(s, 0, len(s)-1)

for _ in range(t) :
    s = sys.stdin.readline().rstrip() # 1 <= S <= 1000
    
    # 팰린드롬인지 아닌지 판별 
    print(isPalindrome(s), cnt)
    
    # cnt 초기화
    cnt = 0 

