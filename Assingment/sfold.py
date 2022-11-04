def sfold(key, size):
    sum = 0
    mul = 1
    for i in range(len(str(key))):
        if (i % 4 == 0):
            mul = 1
        else:
            mul = mul * 256
        sum += ord(key[i]) * mul
    return sum % size


print(sfold("aaltoilu", 100))
