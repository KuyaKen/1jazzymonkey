motorcycles = ['Honda', 'Yamaha','Triumph']
motorcycles[0] = 'suzuki' # overrights the first postion.
print (motorcycles)
motorcycles.append('Honda')
print (motorcycles)
motorcycles.insert(0,'ducati')
print (motorcycles)
del motorcycles[-1]
print (motorcycles)
popped_motorcycle = motorcycles.pop()  # this one removes the last motorcycle
# You can use pop() to remove an item from any position in a list by including the index of the item.
print (popped_motorcycle) #prints what was removed.
print (motorcycles) #full list minus the popped motorcycle
print (f"\n{popped_motorcycle.title()} is my favorite motorcycle.")