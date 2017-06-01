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


def affichage_jeu(mot, lettres_non_presentes, chances):
	print("{} \n Lettres déjà utilisées : {} \n Chances restantes : {}".format(mot, lettres_non_presentes, chances))

def game():
	"""Fonction qui lance le jeu avec 8 chances au départ
		choix du mot au hasard et affichage avec une * par lettre
		le joueur choisit une lettre: si la lettre est dans le mot, elle s'affiche, sinon enlever une chance
		Fin du jeu : si toute les lettres sont découvertes -> GAGNE score = score + chances restantes
					si chance < 0  PERDU score = score """
	for i, elt in enumerate(liste_mot):
		nb_mot = int(i) + 1
	indice_hasard = random.randrange(nb_mot)
	mot_choisi = liste_mot[indice_hasard].upper()
	print(mot_choisi)
	i = 0
	mot_cache = ""
	while i < len(mot_choisi):
		mot_cache += "*"
		i += 1
	print(mot_cache)