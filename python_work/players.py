players = ['charles','martina','michael','florence','eli']
print(players[0:4]) #prints a slice of a list
#print(players[:3])
#print(players[2:])
print("Here are the first names of our players:")
for player in players[0:4]: # dont indent the first line of for loop
	print(player.title())