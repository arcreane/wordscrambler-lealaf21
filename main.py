# import = Permet d'importer un fichier dans celui ci. (Lier les fichiers)
import niveaux

# Définition de la fonction du menu principal
def menu():
    user_choice = input("""Choisissez votre option
    1 - Jouer
    2 - Quitter
    """)
    if user_choice == "1":
        niveaux.choix_du_niveau()
    elif user_choice == "2":
        exit()

# Permet d'afficher le menu principal
if __name__ == "__main__":
    while True:
        menu()