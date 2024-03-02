import random

def choose_word():
    """
    Escolhe uma palavra aleatória para o jogo.
    """
    words = ["python", "banana", "computador", "elefante", "girafa", "programação"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Exibe a palavra com letras não adivinhadas substituídas por '_'.
    """
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    """
    Função principal para o jogo da Forca.
    """
    print("Bem-vindo ao jogo da Forca!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nPalavra:", display_word(word, guessed_letters))
        guess = input("Tente adivinhar uma letra: ").lower()

        if guess in guessed_letters:
            print("Você já tentou essa letra.")
        elif guess in word:
            print("Letra correta!")
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print("Parabéns! Você ganhou!")
                break
        else:
            print("Letra errada.")
            attempts -= 1
            print("Tentativas restantes:", attempts)
        
    else:
        print("Você perdeu! A palavra era:", word)

if __name__ == "__main__":
    hangman()
