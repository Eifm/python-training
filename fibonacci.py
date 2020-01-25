cars = [1,1]
for num in range(0,98):
    cars.append(cars[-1]+cars[-2])
print(cars[-1])
