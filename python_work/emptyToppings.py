requested_toppings = []
requested_toppings.append('Extra Cheese')
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"adding {requested_topping}")
	print("\nFinished with your pizza")
else:
	print("Are you sure you want just a plain pizza?")