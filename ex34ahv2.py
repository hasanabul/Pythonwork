animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
list(enumerate(animals))
print "Select 1 for ordinal or 2 for cardinal order. Which option would you like 1 or 2"

option = raw_input("> ")

if option == "1":
	print "Select ordinal animal position"

	Animal_position = raw_input("> ")
	for Animal_position , animals in enumerate(animals):
		if Animal_position  == 0:
			print animals
		elif Animal_position  == 1:
			print animals
		elif Animal_position == 2:
			print animals
		elif Animal_position == 3:
			print animals
		elif Animal_position == 4:
			print animals
		elif Animal_position == 5:
			print animals
		elif Animal_position == 6:
			print animals
elif	option =="2":
		print "Select cardinal animal position"


#for animal in animals: 
	##print "A animal of type: %s" % animal