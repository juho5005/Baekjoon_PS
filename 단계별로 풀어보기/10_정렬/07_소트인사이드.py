import sys 
n = int(sys.stdin.readline())

nums_lst = []
for elem in str(n) : 
    nums_lst.append(int(elem))

nums_lst.sort(reverse=True)

for elem in nums_lst :
    print(elem, end ='')