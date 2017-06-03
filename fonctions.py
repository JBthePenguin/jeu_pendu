import pickle
import random
from donnees import *


def save_score(names_scores):
	"""Fonction qui sauvegarde le score dans scores"""
	with open("scores", "wb") as fichier_score:
		score_pickler = pickle.Pickler(fichier_score)
		score_pickler.dump(names_scores)


def player_score(player_name):
	"""Fonction qui demande au joueur de rentrer son nom,
	vérifie si il y a au moins 1 caractère,
	l'enregistre dans scores avec un score de 0 s'il est nouveau et renvoie le score
	si il est déjà enregistré, renvoie le score"""
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


def choose_word():
	"""Function that choose a word in the liste_mot"""
	for i, elt in enumerate(liste_mot): # choose a word in the list
		nb_mot = int(i) + 1
	indice_hasard = random.randrange(nb_mot)
	mot_choisi = liste_mot[indice_hasard].upper()
	return mot_choisi


def choose_lettre():
	""" Function that verify the letter's format""" 
	valid_lettre = False # valid letter
	while valid_lettre == False:
		lettre_choisi = input("Choisir une lettre : ")
		lettre_choisi = lettre_choisi.upper()
		for i, elt in enumerate(lettres):
			if lettre_choisi == elt:
				valid_lettre = True
				return lettre_choisi
				break
			else:
				valid_lettre = False
				if i == len(lettres) - 1:
					print("Ce n'est pas une lettre!!!")


def letter_is_or_not_in_word(lettre_choisi,list_lettre_mot):
	"""Function to know if the letter is in the word or not"""
	for i, elt in enumerate(list_lettre_mot):
		if lettre_choisi == elt:
			print ( "Bien, la lettre ", lettre_choisi, "est présente dans le mot")
			return True
			break
		else:
			if i == len(list_lettre_mot) - 1:
				print("Désolé, la lettre ",lettre_choisi, " n'est pas dans le mot")
				return False


def affichage_jeu(mot_cache, lettres_non_presentes, chances_restantes):
	"""Function for screen game : chances, word with * and letter found, list of letters that's not in the word""" 
	print("\n Chances restantes : {}\n\n Lettres déjà utilisées qui ne sont pas dans le mot : {}\n\n {}\n".format(chances_restantes, lettres_non_presentes, mot_cache))


def game():
	"""Fonction qui lance le jeu avec 8 chances au départ
		choix du mot au hasard et affichage avec une * par lettre
		le joueur choisit une lettre: si la lettre est dans le mot, elle s'affiche, sinon enlever une chance
		Fin du jeu : si toute les lettres sont découvertes -> GAGNE score = score + chances restantes
					si chance < 0  PERDU score = score """
	mot_choisi = choose_word() # choose a word in the list
	
	list_lettre_mot = [] #list word's letters
	i = 0
	while i < len(mot_choisi):
		list_lettre_mot += [mot_choisi[i]]
		i += 1

	list_lettre_mot_cachee = [] # list word's letter with *
	for i, elt in enumerate(list_lettre_mot):
		list_lettre_mot_cachee += ["*"]

	mot_cache = "".join(list_lettre_mot_cachee) # word with hide letter
	lettres_non_presentes = ""
	chances_restantes = 8
	
	while chances_restantes > 0:
		affichage_jeu(mot_cache, lettres_non_presentes, chances_restantes)
		lettre_choisi=choose_lettre()
		
		if letter_is_or_not_in_word(lettre_choisi,list_lettre_mot) == False:
			lettres_non_presentes += ("  " +str(lettre_choisi))
			chances_restantes -= 1
		else:
			for i, elt in enumerate(list_lettre_mot):
				if lettre_choisi == elt:
					ind = i
					list_lettre_mot_cachee[ind] = str(lettre_choisi)
			mot_cache = "".join(list_lettre_mot_cachee)
		
		if list_lettre_mot_cachee == list_lettre_mot:
			gain = int(chances_restantes)
			print("\n {} \n GAGNE!!!! Tu as gagné {} point(s)!".format(mot_choisi.upper(), gain))
			return gain
			break
	
	else:
		gain = 0
		print("\nPERDU!!! Le mot était {} .".format(mot_choisi.upper()))
		return gain
 
 