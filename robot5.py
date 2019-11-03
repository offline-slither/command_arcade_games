
#Def zone 
import os

from cartes import *



rejouer = True
while rejouer == True:

	level_container = {}

	# -----------
	level_index = 1

	# def Loader("nom de fichier"):
		# interpret ndf , en un pytem utiliseable et ajout "lvlXX" XX etant le niveau crée ainsi 
		# initialise une player_pos (x, y)
		# initialise une win_pos (x, y)

	all_cartes = []
	for each_map in os.listdir("cartes"):
		# l'indexation des niveau se produit une fois
		if each_map.endswith(".txt"):
			chemin = os.path.join("cartes", each_map)
			nom_carte = each_map[:-3].lower()
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				all_cartes.append(contenu)
			level_container[level_index] = nom_carte
			print(f"{(level_index)}:{nom_carte}")
			level_index += 1

		if each_map.endswith("sauvegarde.txt"):
			print("vous avez un fichier de sauvegarde, vous pouvez le choisir dans le selection de niveau \nou commencer une nouvelle partie")


	# testeurs
	# 	print("premier level \n")        
	# 	print(all_cartes[0])
	# 	print("second level \n")
	# 	print(all_cartes[1])
	# 	print(list(all_cartes))
	print("Selcetionez un niveau")



	try:
		level_selected = int(input())
		print(all_cartes[(level_selected-1)])
	except:#IndexError,ValueError:
		print("niveau indisponible, voila le premier niveau")
		level_selected = 1
		print(all_cartes[(level_selected-1)])
	base_ref = all_cartes[(level_selected-1)]
	# base_ref = list(base_ref)
	fond = base_ref


	# obtenir la hauteur et longueur horisontale de la map
	hor_lenght = 0
	height = 1
	for each_char in base_ref:
		if each_char == "\n":
			height += 1
		# else:
		# 	print(f"longueur horizontale : {hor_lenght}")
		# 	break

	for each_char in base_ref:
		if each_char != "\n":
			hor_lenght += 1
		else:
			print(f"longueur horizontale : {hor_lenght}")
			print(f"hauteur : {height}")
			break
	# ------------------------------------------------------


	# obtenir les coordonée du U au début d'un niveau choisi, afin d'avoir la position de victoire 
	u_xpos = 0
	u_ypos = 1
	for each_char in base_ref:
		if each_char != "U" and each_char !="\n":
			u_xpos += 1
		elif each_char == "\n":
			u_ypos += 1
		else:
			u_xpos += 1
			# print(f"position totale x {xpos}")

			# print(f"position x {xpos%hor_lenght}")
			# print(f"position y {ypos}")
			if u_xpos % hor_lenght == 0:
				# print(f"U se trouve en {hor_lenght},{u_ypos}")
				win_pos = [hor_lenght,u_ypos]
			else:
				# print(f"U se trouve en {u_xpos%hor_lenght},{u_ypos}")
				win_pos = [u_xpos%hor_lenght,u_ypos]
			break
	# ---------------------------------------------------


	# obtenir les coordonée du X au début d'un niveau choisi  
	xpos = 0
	ypos = 1
	for each_char in base_ref:
		if each_char != "X" and each_char !="\n":
			xpos += 1
		elif each_char == "\n":
			ypos += 1
		else:
			xpos += 1
			# print(f"position totale x {xpos}")

			# print(f"position x {xpos%hor_lenght}")
			# print(f"position y {ypos}")
			print(f"X se trouve en {xpos%hor_lenght},{ypos}")
			break
	# xpos represente la position totale et doit dont etre reduit par les multiples de la longeur
	# ---------------------------------------------------

	start_pos = [(xpos%hor_lenght)-1,(ypos-1)] 
	# print(start_pos)

	fond = fond.replace("X","_")
	# Map displayerer:
	 # 		, cree affiche une version de la map temporaire, ou seul la position du joueur est differente de sa map reference 
	level_clear = False
	current_pos = start_pos 
	while level_clear == False:
		mov_cycle = 1
		p_input = input("").lower()
		print(p_input)
		if p_input[0] == "n":
			# print("plus haut")
			direction = "haut"
			# print(current_pos)
			if len(p_input) > 1:
				try: 
					mov_cycle = int(p_input[1:])
				except ValueError:
					mov_cycle = 2
				# print("longueur n detected")
				# print(mov_cycle)
			proj_pos = current_pos[0],current_pos[1]-1
			# print(f" position projetée {proj_pos}")
		elif p_input[0] == "e":
			# print("a droite")
			direction = "droite"
			if len(p_input) > 1:
				try: 
					mov_cycle = int(p_input[1:])
				except ValueError:
					mov_cycle = 2
				# print("longueur n detected")
				# print(mov_cycle)
			proj_pos = current_pos[0]+1,current_pos[1]
			# print(f" position projetée {proj_pos}")
		elif p_input[0] == "s":
			# print("plus bas")
			direction = "bas"
			if len(p_input) > 1:
				try: 
					mov_cycle = int(p_input[1:])
				except ValueError:
					mov_cycle = 2
				# print("longueur n detected")
				# print(mov_cycle)
			proj_pos = current_pos[0],current_pos[1]+1
			# print(f" position projetée {proj_pos}")
		elif p_input[0] == "o":
			# print("a gauche")
			direction = "gauche"
			if len(p_input) > 1:
				try: 
					mov_cycle = int(p_input[1:])
				except ValueError:
					mov_cycle = 2
			proj_pos = current_pos[0]-1,current_pos[1]
			# print(f" position projetée {proj_pos}")
				# print("longueur n detected")
				# print(mov_cycle)
		elif p_input[0] == "q":
			print("sauvegarder ? y/n")
			do_save = input().lower()
			if do_save in ["y","oui","o","yes"]:
				print("......sauvegarde")
				with open("cartes/_sauvegarde.txt","w") as file:
					file.write(base_ref)
				print("au revoir")
				break
			else:
				print("au revoir")
				break
			break
		else:
			continue
		# availbilitychecker
		if mov_cycle >20:
			mov_cycle = 20
		for fois in range(0,mov_cycle):
			isx = 0
			isy = 0
			isxoverall = 0
			for each_char in base_ref:
				if isx == (hor_lenght+1):
					isy += 1
					isx = 0
					# isx -= 1
				if (isx,isy) == proj_pos:
					# print(f"la position lue est {(isx,isy)}")
					# if level_clear == False: ????????????????????????????????????
						# print(f"la position actuele est {current_pos}")
						# print(f"la position projectée est {(isx,isy)}")
						#ces testeurs evalue l'avancee du robot
					# if each_char != " " :
					# 	print(f"sur cette case se trouvais le symbole {each_char}")
						#ce testeur donne la case en lecture, elle est comparée
					if each_char == "U" :#ou toute autre condition blockante
						if fois == (mov_cycle-1):
							print("Sortie atteinte, vous avez gagne (ce lvl) ")
							level_clear = True
						break
					elif each_char == "O" :#ou toute autre condition blockante
						if fois == (mov_cycle-1): print("ll s'agit d'un mur")
						break
					else:
						base_ref = list(fond)
						base_ref[(isxoverall)] = "X"
						base_ref = "".join(base_ref)
						old_pos = current_pos
						current_pos = proj_pos
						if mov_cycle > 1:
							if direction == "haut":
								proj_pos = current_pos[0],current_pos[1]-1
							elif direction == "bas":
								proj_pos = current_pos[0],current_pos[1]+1
							elif direction == "droite":
								proj_pos = current_pos[0]+1,current_pos[1]
							elif direction == "gauche":
								proj_pos = current_pos[0]-1,current_pos[1]
							else:
								pass
						break
				isx += 1
				isxoverall += 1
		if level_clear != True: 
			print(base_ref)
			print(current_pos)
			print(f"atteindre {win_pos}pour gagner")
	print("envie de rejouer y/n ?")
	reponce = input("").lower()
	if reponce not in ["y","oui","o","yes"]:
		rejouer = False