
from random import choice,randint
from termcolor import *
from colorama import init
init()
# ------------------------------------------
# 
from time import sleep
def Map_maker(lenght=20,height=20,echelles=0):
	lvl=""
	count = int(height)
	wall = "O"
	for etage in range(1,height+1):
		for each in range(1,lenght+1):
			if each == count:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			elif each == 1:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			else:
				case = choice([" "," "," ","/","O"])
				lvl=list(lvl)
				lvl.append(case)
				lvl ="".join(lvl)
		lvl=list(lvl)
		lvl.append("\n")
		lvl ="".join(lvl)
	# print(lvl)
	return(lvl)

def Duster_full(cmap):
	cmap = cmap.replace(" ",".")
	return cmap

def Duster_rand(cmap):
	count = 0 
	for char in cmap:
		if char == " ":
			val = randint(1,11)
			if val <= 6:
				cmap = list(cmap)
				cmap[count] = choice([".",":","¨"])
				cmap = "".join(cmap)
		count += 1
	return cmap

def Supply_cheese(cmap):
	count = 0 
	count2 = 0
	for char in cmap:
		if count2 >5:
			break
		if char == " ":
			val = randint(1,99)
			if val == 1 :
				cmap = list(cmap)
				cmap[count] = choice(["°","o"])
				cmap = "".join(cmap)
				count2 += 1
		count += 1
	return cmap


def Pool_maker_old(lenght=15,height=15,echelles=0):
	while True:
		lvl=""
		count = int(height)
		wall = "O"
		for etage in range(1,height+1):
			for each in range(1,lenght+1):
				if each == count:
					lvl=list(lvl)
					lvl.append(wall)
					lvl ="".join(lvl)
				elif each == 1:
					lvl=list(lvl)
					lvl.append(wall)
					lvl ="".join(lvl)
				else:
					case = choice(["'","-","^","v"])
					# print("un tour")
					# print(case)
					lvl=list(lvl)
					lvl.append(colored(case, color="cyan"))
					lvl ="".join(lvl)
					# lvl="".join(case)
			lvl=list(lvl)
			lvl.append("\n")
			lvl ="".join(lvl)
		print(lvl)
		# return(lvl)
		sleep(0.5)
def Pool_maker_3(lenght=15,height=15,echelles=0):
	lvl=""
	count = int(height)
	wall = "O"
	for etage in range(1,height+1):
		for each in range(1,lenght+1):
			if each == count:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			elif each == 1:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			else:
				case = choice(["_","-","^","-"])
				# print("un tour")
				# print(case)
				lvl=list(lvl)
				lvl.append(colored(case, color="cyan"))
				lvl ="".join(lvl)
				# lvl="".join(case)
		lvl=list(lvl)
		lvl.append("\n")
		lvl ="".join(lvl)
	return(lvl)

def Pool_maker(lenght=15,height=15,echelles=0):
	"""make a basic pool, wave should 'animate' on client"""
	lvl=""
	count = int(height)
	wall = "O"
	for etage in range(1,height+1):
		for each in range(1,lenght+1):
			if each == count:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			elif each == 1:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			else:
				case = choice(["_","-","^","-"])
				# print("un tour")
				# print(case)
				lvl=list(lvl)
				lvl.append(case)
				lvl ="".join(lvl)
				# lvl="".join(case)
		lvl=list(lvl)
		lvl.append("\n")
		lvl ="".join(lvl)
	# print(lvl)
	return(lvl)

def Animate_water(char_chain):
	char_chain = char_chain.replace("_","1")
	char_chain = char_chain.replace("/","2")
	char_chain = char_chain.replace("^","3")
	char_chain = char_chain.replace("-","4")
	char_chain = char_chain.replace("1","/")
	char_chain = char_chain.replace("2","^")
	char_chain = char_chain.replace("3","-")
	char_chain = char_chain.replace("4","_")
	return char_chain

# Pool_maker()
# def Dust_maker
def Wall_maker(lenght=15,height=15,echelles=0):
	lvl=""
	count = int(height)
	wall = "I"
	for etage in range(1,height+1):
		for each in range(1,lenght+1):
			if each == count:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			elif each == 1:
				lvl=list(lvl)
				lvl.append(wall)
				lvl ="".join(lvl)
			else:
				case = choice([" "," "," ","/","O"])
				# print("un tour")
				# print(case)
				lvl=list(lvl)
				lvl.append(case)
				lvl ="".join(lvl)
				# lvl="".join(case)
		lvl=list(lvl)
		lvl.append("\n")
		lvl ="".join(lvl)
	# print(lvl)
	return(lvl)
	
def Stair_maker(n):
	"""n is an int determining the lenght and height of the stair"""
	for eCh in range(1,n+1):
		rslt = ""
		rslt = str(" "* (n-eCh))+ rslt
		rslt = rslt + str("#"* eCh)
		print(rslt)