import math

arr =[27 , 32, 15, 77, 6, 11, 22, 45, 99, 40]
M = 10
numarr = []

for i in arr:
    x = math.floor(i / M)
    numarr.append(x)

numarr.sort()
print(numarr)