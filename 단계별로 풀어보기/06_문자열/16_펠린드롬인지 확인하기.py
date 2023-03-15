import sys 
string = sys.stdin.readline().rstrip()

def is_palindrome(s, e) :
    while s < e : 
        if string[s] != string[e] :
            return 0
        s += 1
        e -= 1
    return 1

print(is_palindrome(0, len(string)-1))