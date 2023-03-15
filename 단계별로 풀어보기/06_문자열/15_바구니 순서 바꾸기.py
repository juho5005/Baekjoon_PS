import sys, copy

n, m = tuple(map(int, sys.stdin.readline().split()))

basket = [
    i
    for i in range(n+1)
]

for _ in range(m) :
    i, j, k = tuple(map(int, sys.stdin.readline().split()))
    

    # i번째 바구니부터 j번째 바구니까찌
    # 기준은 k번째 바구니

    l = j-i+1  # i~j까지의 총 개수 
    
    q = j-k+1 # j-k까지 바뀌는 개수 

    b = basket[i:i+(l-q)].copy()
    c = basket[k:k+q].copy()

    basket[i:i+q] = c
    basket[i+q:j+1] = b  

for i in range(1, n+1) :
    print(basket[i], end = ' ')