# 택시 기하학
# T1(x1, y1), T2(x2, y2) 사이의 거리는
# |x1-x2| + |y1-y2|

# 반지름 R이 주어질 때 
# 유클리드 기하학에서의 원의 넓이와
# 택시 기하학에서 원의 넓이를 구하기

import sys 
import math 
r = int(sys.stdin.readline()) # r <= 10,000 

# uclid's area of circle
print(r*r*math.pi) 

# taxi's area of circle 
print(r*r*2)