import sys 
n = int(sys.stdin.readline()) # N의 개수, N은 홀수!!

# n <= 500,000, O(1), O(N), O(logN), O(NogN)
# 입력되는 정수의 절댓값은 4000을 넘지 않는다.

nums = []
for _ in range(n) :
    nums.append(int(sys.stdin.readline()))

# 우선, 정렬
nums.sort() # O(NlogN) 

# 1) 산술평균
def nums_avg(nums) :
    print(int(round(sum(nums)/len(nums), 0)))

# 2) 중앙값 
# N이 홀수이므로, 정렬된 값에서 개수 // 2해주면 된다
def nums_median(nums) :
    print(nums[len(nums)//2])

# 3) 최빈값 
# 최빈값을 출력하는데, 최빈값이 여러 개 존재 시 두 번째로 작은 값을 출력
def nums_mode(nums) :
    dic_nums = {}
    
    for num in nums :
        if num not in dic_nums :
            dic_nums[num] = 1
        else :
            dic_nums[num] += 1 # 각 숫자의 개수를 세어주기 위해 dictionary 사용
        
    sorted_dic_nums = sorted(dic_nums.items(), key=lambda x:(x[1],-x[0])) 

    if len(sorted_dic_nums) == 1 :
        print(sorted_dic_nums[0][0])
        return 
    
    if sorted_dic_nums[-2][1] == sorted_dic_nums[-1][1] : # 최빈값이 2개 이상일 때
        print(sorted_dic_nums[-2][0])
    else :
        print(sorted_dic_nums[-1][0])

# 4) 범위
def nums_range(nums) :
    print(max(nums)-min(nums))

# 함수 실행
nums_avg(nums)
nums_median(nums)
nums_mode(nums)
nums_range(nums)