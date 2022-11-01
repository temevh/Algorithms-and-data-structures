from turtle import pos


def sales(cars, customers) -> int:
    possible = 0
    customers.sort()
    cars.sort()
    maxCar = 0
    minCar = 15415152515
    print(customers)
    print(cars)
    for i in range(len(customers)):
        if cars[i] <= customers[i]:
            possible += 1
        elif cars[i+1] <= customers[i]:
            i += 1
        
        if cars[i] > maxCar:
            maxCar == cars[i]
        if cars[i] < minCar:
            minCar == cars[i]
        

    return possible


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5   