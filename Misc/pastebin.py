for i in range(len(customers)):
        if cars[i] <= customers[i]:
            possible += 1
        elif cars[i+1] <= customers[i]:
            i += 1
        
        if cars[i] > maxCar:
            maxCar == cars[i]
        if cars[i] < minCar:
            minCar == cars[i]




for i in range(len(cars)):
    print("i:", i)
    customer = customers[i]
    car = cars[i]
    mincar = min(cars)
    if car <= customer:
        possible += 1
        cars.remove(car)
        customers.remove(customer)
    if car >= customer:
        if mincar <= customer:
            possible += 1
            cars.remove(mincar)
            customers.remove(customer)
        if mincar > customer:
            i += 1
    print("possible",possible)


for i in range(len(customers)):
        car = cars[i]
        customer = customers[i]
        if car <= customer:
            possible += 1
            customers.remove(customer)
            cars.remove(car)
        elif car > customer:
            i += 1