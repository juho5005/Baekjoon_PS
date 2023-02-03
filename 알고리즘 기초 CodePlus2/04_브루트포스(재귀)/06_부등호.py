# 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재
# 제시된 k개의 부등호 순서를 만족하는 (k+1)자리 정수 중에서 최댓값과 최솟값을 찾으시오

# 선택된 숫자는 모두 달라야 함
import sys 
# 부등호의 개수
k = int(sys.stdin.readline()) 

equation = [' '] + sys.stdin.readline().rstrip().split()


# k+1개만큼의 숫자가 들어갈 수 있음
# nums : 0 ~ 10
nums = [
    i
    for i in range(10)
]

visited = [
    False 
    for _ in range(11)
]

ans = []

# maked_nums
maked_nums = []

def make_num() :
    str_num = ''
    for elem in ans :
        str_num += str(elem)
    maked_nums.append(str_num)

def choose(curr_jarisu) :
    if curr_jarisu == k+2 :
        make_num()
        return 
    
    for num in nums :
        if not visited[num] :
            if curr_jarisu != 1 and equation[curr_jarisu-1] == '>' :
                if num > ans[-1] :
                    continue
            if curr_jarisu != 1 and equation[curr_jarisu-1] == '<' :
                if num < ans[-1] :
                    continue 
            visited[num] = True 
            ans.append(num)
            choose(curr_jarisu+1)
            ans.pop()
            visited[num] = False 

choose(1)
print(str(max(maked_nums)))
print(str(min(maked_nums)))