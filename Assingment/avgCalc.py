import sys

tiedosto = sys.argv[1]
arr = []

i = 8
with open(tiedosto) as f:
    lines = f.readlines()
    # print(lines[8:81:8])
while i < 82:
    arr.append(lines[i])
    i += 8

arr2 = []
for elem in arr:
    # print((elem.strip()).split())
    arr2.append(float(((elem.strip()).split()[2])))

# print(arr2)

avg = sum(arr2)/len(arr2)

print("Average:", avg)
