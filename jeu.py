from niveaux import choix_du_niveau

def nouvelle_partie():
    with open("mots.txt", "r", encoding='utf-8') as words_file:
        words = words_file.read().splitlines()

    dif = choix_du_niveau()
    random_word = init_grid(dif, words)
    play(random_word)

def init_grid(dif, words):
    print()

def play(random_word):
    print(random_word)
    word_displayed = len(random_word) * [""]
    while len(random_word) != 0:
        print("".join(word_displayed))
        letter = input("Donner une lettre : ")
        if letter in random_word:
            for index, ch in enumerate(random_word):
                if ch == letter:
                    word_displayed[index] = letter
        else:
            nb_mots -= 1
        print(f'Nombre de mots restant : {nb_mots}')


def get_longest_word(words):
    max_char = 0
    longest_word = ""
    for word in words:
        if len(word) > max_char:
            max_char = len(word)
            longest_word = word

    print(longest_word, ":", max_char)


if __name__ == "__main__":
    nouvelle_partie()