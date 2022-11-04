import time


arr = []

file = open("sanatPieni.txt", "r")
for line in file:
    arr.append(line.strip())

st = time.time()
print(arr.index("aakkostus"))
et = time.time()

print("Execution time", et-st, "seconds")
