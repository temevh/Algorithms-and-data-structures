def primes(N):
    
    laskuri = 0

    for numero in range(N):
        if numero <= 1:
            continue
        for i in range(2, numero):
            if (numero % i ) == 0:
                break
        else:
            laskuri +=1
    
    return laskuri

        


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15