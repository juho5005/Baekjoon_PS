# 세 점이 주어질 때
# 축에 평행한 직사각형을 만들기 위한 네 번째 점을 찾는 프로그램

import sys 

coordinates = []
for _ in range(3) :
    coordinates.append(list(map(int, sys.stdin.readline().split())))
    

x_dic = {}
y_dic = {}

for coordinate in coordinates :
    
    if coordinate[0] not in x_dic :
        x_dic[coordinate[0]] = 1
    else :
        x_dic[coordinate[0]] += 1
    
    if coordinate[1] not in y_dic :
        y_dic[coordinate[1]] = 1
    else :
        y_dic[coordinate[1]] += 1

sorted_x_dic = sorted(x_dic.items(), key=lambda data:data[1])
sorted_y_dic = sorted(y_dic.items(), key=lambda data:data[1])

print(sorted_x_dic[0][0], sorted_y_dic[0][0])