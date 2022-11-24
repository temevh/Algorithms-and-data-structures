import sys

tiedosto = sys.argv[1]
arr = []

with open(tiedosto) as f:
    lines = f.readlines()


for i in lines:
    arr.append(int(lines[i]))

avg = sum(arr)/len(arr)

print("Average:", avg)
