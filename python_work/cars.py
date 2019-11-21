cars = ['bmw','audi','toyota','subaru']
#cars.sort()
#print (cars)
#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars))
#print(cars)
#print(len(cars))
for car in cars: # dont forget the colon after For, If and else statements.
	if car == 'audi':
		print(car.upper(),"is the correct car we are looking for")
	else:
		print(car.title(),"...is not an audi")