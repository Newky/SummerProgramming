#python -i "$(FULL_CURRENT_PATH)"
def option():
	
	users_input = raw_input("y or n?")
	print "\n"
	while users_input not in ['y','n']:
		print "INVALID CHOICE"
		print "\n"
		users_input = raw_input("y or n?")
		print "\n"
	if users_input == 'y':
		return True
	elif users_input == 'n':
		return False
def start():
	raw_input("") 	
	print "WELCOME TO MY ADVENTURE \n \nThe objective is to make it through the forest"
	raw_input("")
	print "Do you want to enter the forest?"
	y = option()
	if y:
		bear()
	else:
		return None

def bear():
	print"Do you want to go along the path or turn into the trees?\n\nIf path..type y \nIf tress...type n"

	y=option()

	if y == True:
		print "Nice and safe..bit muddy though"
		house()
	else:
		print "BEAR!!"
		raw_input("")
		return None

def house():
	print "Theres a house..looks haunted though\n\nWant to go in...type y\nJust keep walking...type n"
	
	y=option()
	
	if y == True:
		print "The door opens by itself...Want to enter?"
		y=option()
		if y == True:
			print "A hand grabs your arm...you get eaten by a monster!!!"
			raw_input("")
			return None
		else:
			print "Good choice..looks a bit scary....back to the road!!"
	else:
		print "The road looks dark but at least theres no ghosts or witchs"		

# Stack trace...
start()
