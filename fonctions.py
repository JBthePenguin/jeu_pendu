import pickle
import random
from donnees import *

def save_score(names_scores):
	"""Fonction qui sauvegarde le score dans scores"""
	with open("scores", "wb") as fichier_score:
		score_pickler = pickle.Pickler(fichier_score)
		score_pickler.dump(names_scores)


def player_score():
	"""Fonction qui demande au joueur de rentrer son nom,
	vérifie si il y a au moins 1 caractère,
	l'enregistre dans scores avec un score de 0 s'il est nouveau et renvoie le score
	si il est déjà enregistré, renvoie le score"""
	player_name = input("Qui es-tu? : ")
	player_name = str(player_name)
	
	while player_name == "":
		print("???? Oh! Un nom vide n'est pas possible ????")
		player_name = input("Qui es-tu? : ")
		player_name = str(player_name)

	else:
		try:
			open("scores", "r")
		except FileNotFoundError:
			names_scores = {}
			names_scores[player_name] = 0
			save_score(names_scores)
			return int(names_scores[player_name])
		else:
			with open("scores", "rb") as fichier_score:
				score_depickler = pickle.Unpickler(fichier_score)
				names_scores = score_depickler.load()
			if player_name in names_scores.keys():
				return int(names_scores[player_name])
			else:
				names_scores[player_name] = 0
				save_score(names_scores)
				return int(names_scores[player_name])


def affichage_jeu(mot, lettres_non_presentes, chances_restantes):
	print("{} \nLettres déjà utilisées : {} \nChances restantes : {}".format(mot, lettres_non_presentes, chances_restantes))

def game():
	"""Fonction qui lance le jeu avec 8 chances au départ
		choix du mot au hasard et affichage avec une * par lettre
		le joueur choisit une lettre: si la lettre est dans le mot, elle s'affiche, sinon enlever une chance
		Fin du jeu : si toute les lettres sont découvertes -> GAGNE score = score + chances restantes
					si chance < 0  PERDU score = score """
	
	for i, elt in enumerate(liste_mot): # choose a word in the list
		nb_mot = int(i) + 1
	indice_hasard = random.randrange(nb_mot)
	mot_choisi = liste_mot[indice_hasard].upper()
	print(mot_choisi)
	
	i = 0 # hide letter
	mot_cache = ""
	while i < len(mot_choisi):
		mot_cache += "*"
		i += 1
	
	chances_restantes = chances
	lettres_non_presentes = ""
	affichage_jeu(mot_cache, lettres_non_presentes, chances_restantes)

	list_lettre_mot = []
	i = 0
	while i < len(mot_choisi):
		list_lettre_mot += [mot_choisi[i]]
		i += 1
	print(list_lettre_mot)

	valid_lettre = False # valid letter
	while valid_lettre == False:
		lettre_choisi = input("Choisir une lettre : ")
		lettre_choisi = lettre_choisi.upper()
		for i, elt in enumerate(lettres):
			if lettre_choisi == elt:
				valid_lettre = True
				break
			else:
				valid_lettre = False
				if i == len(lettres) - 1:
					print("Ce n'est pas une lettre!!!")
	
	letter_in_word = False # letter in the word?
	for i, elt in enumerate(list_lettre_mot):
		if lettre_choisi == elt:
			letter_in_word = True
			print ( "Bien, la lettre ", lettre_choisi, "est présente dans le mot")
			break
		else:
			if i == len(list_lettre_mot) - 1:
				print("Désolé, la lettre ",lettre_choisi, " n'est pas dans le mot")
				lettres_non_presentes += str(lettre_choisi)
				chances_restantes -= 1
				affichage_jeu(mot_cache, lettres_non_presentes, chances_restantes)
				

		
	
		

