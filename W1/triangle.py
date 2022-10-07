def triangle(a, b, c):
    longest = a
    if (b > longest):
        longest = b
        b = 0
    if (c > longest):
        longest = c
        c = 0
    if (longest - a - b - c > 0):
        return False
    else:
        return True
    
    
    


if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True