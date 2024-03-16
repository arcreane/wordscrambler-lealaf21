
niveau = [("facile", 0, 4, 10, 5, 5), ("moyen", 4, 6, 15, 7, 10), ("difficile", 6, 9, 30, 15, 15)]

def choix_du_niveau():
    difficulty = -1
    while not (0 <= difficulty < len(niveau)):
        input_player = "Sélectionnez un niveau : \n"
        for i in range(len(niveau)):
            input_player += f" {i + 1} - Niveau {niveau[i][0]} "
            input_player += f"(mot de {niveau[i][1]}"
            input_player += f" à {niveau[i][2]} lettres, "
            input_player += f"vous aurez {niveau[i][5]} mots à trouver.)\n"

        if input_player == "1":
            jeu.nouvelle_partie()
        elif input_player == "2":
            jeu.nouvelle_partie()
        elif input_player == "3":
            jeu.nouvelle_partie()

        if __name__ == "__main__":
            print(input_player)
            difficulty = 1
        else:
            try:
                difficulty = int(input(input_player))
            except ValueError:
                print("Uniquement des valeurs entières s'il vous plaît")

    return difficulty

##############################################################################################################