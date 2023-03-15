import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

basket = [
    i
    for i in range(n+1)
]

for _ in range(m) :
    i, j, k = tuple(map(int,sys.stdin.readline().split()))
    
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]

for i in range(1, n+1) :
    print(basket[i], end = ' ')