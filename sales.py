def sales(cars, customers) -> int:
    customers.sort()
    cars.sort()
    customerIndex = 0
    carIndex = 0
    while customerIndex < len(customers):
        customer = customers[customerIndex]
        if carIndex >= len(cars):
            break
        car = cars[carIndex]
        if car <= customer:
            customerIndex += 1
            carIndex += 1
        else:
            customerIndex += 1
    return carIndex


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5
    print(sales([0, 1, 2], [10, 10, 10, 10, 10, 10]))
