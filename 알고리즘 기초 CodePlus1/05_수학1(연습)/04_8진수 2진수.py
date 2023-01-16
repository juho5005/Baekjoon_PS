
# ---------- 하드코딩으로 구현할 시 시간초과 발생!!!!!! ----------
# import sys 
# oct_num = sys.stdin.readline().rstrip()

# # 소인수 분해
# def bin_cal(n) :
#     nums = ''
    
#     while n != 0 :
#         nums = str(n%2) + nums # 뒤로 더해줌
#         n //= 2 
    
#     if len(nums) == 1 : 
#         nums = '00' + nums
#     elif len(nums) == 2 :
#         nums = '0' + nums
#     else :
#         pass

#     return nums 

# # 결과
# res = ''

# for elem in oct_num : 
#     res += str(bin_cal(int(elem)))

# for i in range(len(res)) :
#     if res[i] == '1' :
#         print(res[i:])
#         sys.exit()

# ----- 파이썬 내장함수 이용 -----
import sys 

# 수를 8진수로 받아준다.
num = int(sys.stdin.readline(), 8)

# 받은 수를 2진수로 변환 후 앞에 접두사를 제거
print(bin(num)[2:])