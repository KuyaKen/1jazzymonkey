magicians = ['alice','david','carolina']
for magician in magicians: # make sure to put the : after the for loop. Magician is a new variable. 
	print(f"{magician.title()}, that was a great trick.") # variable magician is printed in the list of magicians. 
	#indented lines are considered inside the loop.
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone that was a great magic show. ")	