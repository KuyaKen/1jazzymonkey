alien_0 = {'x_position':0,'y_position':25,'speed':'slow'}
print(f"Orignal position:{alien_0['x_position']}")
#Move the alien to the right. 
	#Determine how far to move the alien based on its current speed,
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#this must be a fast alien
	x_increment = 5
#The new position is the old position plus the incrament
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new postion:{alien_0['x_position']}")
