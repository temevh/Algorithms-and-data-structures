def sales(cars, customers) -> int:
    possible = 0
    customers.sort()
    cars.sort()
    print(customers)
    print(cars)
    for i in range(len(customers)):
        customer = customers[i]
        car = cars[i]
        if car <= customer:
            i += 1

    return i


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5
