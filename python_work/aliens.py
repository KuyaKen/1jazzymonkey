alien_0 = {'color':'green','points':5,'speed':'slow'}
alien_1 = {'color':'yellow','points':10,'speed':'medium'}
alien_2 = {'color':'Red','points':15,'speed':'fast'}

aliens = []

#Make 30 new aliens
for alien_number in range(10):
	new_alien_0 = alien_0
	new_alien_1 = alien_1
	new_alien_2 = alien_2
	aliens.append(new_alien_0)
	aliens.append(new_alien_1)
	aliens.append(new_alien_2)

for alien in aliens[:3]:
	if alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'medium'
		alien['points'] = 16

for alien in aliens[0:5]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

#show the first 5 aliens
for alien in aliens[0:21]:
	print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")