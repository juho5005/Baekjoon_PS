# 알파벳 dictionary 생성 
alphabet_dict = {}
for i in range(65, 91) :
    alphabet_dict[chr(i)] = 0

for val in alphabet_dict.items() :
    alpha, number = val # unpacking
    print(alpha, number)