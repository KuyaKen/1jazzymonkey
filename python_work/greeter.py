prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
prompt_age = "How old are you?: "
age = input(prompt_age)
age = int(age)
print (f"\nHello, {name}!")
print (f"\n{name} you are {age} years old.")