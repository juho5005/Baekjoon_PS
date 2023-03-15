import sys 

grades = []

scores = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0, 
    'F' : 0.0
}

d = 0

for _ in range(20) :
    content = sys.stdin.readline().rstrip().split()

    if content[2] == 'P' :
        continue

    grades.append(float(content[1]) * scores[content[2]])
    d += float(content[1])

print(sum(grades)/d)