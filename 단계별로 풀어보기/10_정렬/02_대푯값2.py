# 중앙값 : 주어진 수를 크기 순서대로 늘여 놓았을 때
# 가장 중앙에 놓인 값 

import sys 

nums = []
for _ in range(5) :
    nums.append(int(
        sys.stdin.readline()
    ))

print(sum(nums)//len(nums)) # 평균

nums.sort() # 중앙값을 구하기 위한 정렬
print(nums[len(nums)//2])
