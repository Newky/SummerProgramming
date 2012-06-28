#python -i "$(FULL_CURRENT_PATH)"
	
def random(yes ,no):
	import random
	i = random.randint(yes,no)  
	return i
	

i = random(1,2)

for j in range(1, 11):
	
	if i == 1:
		print "player %d scored"%j
	else: 
		print"player %d missed "%j	