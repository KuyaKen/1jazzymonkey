requested_toppings = ['Extra Cheese','Pepperoni','Onion','sausage']
outofstock_toppings = 'sausage'
for requested_topping in requested_toppings:
	if requested_topping == outofstock_toppings:
 		print(f"We are out of {outofstock_toppings}")
	else:
		print(f"Adding {requested_topping}")

print("\nYour pizzia is ready")