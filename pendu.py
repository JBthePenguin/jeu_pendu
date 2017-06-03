from fonctions import *
import pickle

# start game -> welcome to...
print("\n ATTENTION à la corde!!!")

# the player enter his name -> score
player_name = input("\nQui es-tu? ")
player_name = str(player_name)

while player_name == "":
	print("\n???? Oh! Un nom vide n'est pas possible ????")
	player_name = input("\n Qui es-tu? : ")
	player_name = str(player_name)

score = player_score(player_name)
print("\n Ton score est de {} point(s).".format(score))

# play
score += game()
print("\n Ton score est de {} point(s).".format(score))

with open("scores", "rb") as fichier_score:
			score_depickler = pickle.Unpickler(fichier_score)
			names_scores = score_depickler.load()

names_scores[player_name] = int(score)
save_score(names_scores)

quit_or_not = input("\nTape 'q' pour quitter ou ailleur que sur le mur pour rejouer: ")
quit_or_not = str(quit_or_not)
while quit_or_not != "q" and quit_or_not != "Q":
	score += game()
	print("\n Ton score est de {} point(s).".format(score))
	with open("scores", "rb") as fichier_score:
		score_depickler = pickle.Unpickler(fichier_score)
		names_scores = score_depickler.load()

	names_scores[player_name] = int(score)
	save_score(names_scores)

	quit_or_not = input("\nTape 'q' pour quitter ou ailleur que sur le mur pour rejouer: ")
	quit_or_not = str(quit_or_not)
	continue
else:
	print("A BIENTOT")