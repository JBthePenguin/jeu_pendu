from fonctions import *
import pickle

# start game -> welcome to...
print("ATTENTION à la corde!!!")

# the player enter his name -> score
player_name = input("Qui es-tu?: ")
player_name = str(player_name)
	
while player_name == "":
	print("???? Oh! Un nom vide n'est pas possible ????")
	player_name = input("Qui es-tu? : ")
	player_name = str(player_name)

score = player_score(player_name)
print(" Ton score est de {} point(s).".format(score))

# le jeu commence
#game()
score += game()

print(" Ton score est de {} point(s).".format(score))


with open("scores", "rb") as fichier_score:
			score_depickler = pickle.Unpickler(fichier_score)
			names_scores = score_depickler.load()

names_scores[player_name] = int(score)
save_score(names_scores)

