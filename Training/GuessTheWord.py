import requests
import json


def load_word():
    api = "https://random-word-api.herokuapp.com/word?key=O6NVW0BE&number=1"
    response = requests.get(api)
    o = json.loads(response.content.decode('utf-8'))
    return o[0]

if __name__ == '__main__':
    print("Welcome to hangman!!")
    word = load_word().upper()
    api_word = word
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = ' '
    tries = 0
    while True:
        
        if letter.upper() in lstGuessed:
            print("Already guessed!!")
            tries = tries - 1
        elif letter.upper() in word:
            indexes = [i for i, l in enumerate(word) if l == letter.upper()]
            for index in indexes:
                guessed[index] = letter.upper()
                word[index] = '_'
        print(' '.join(guessed))
        
        if '_' not in guessed:
            print("You won!!")
            break

        if letter is not '':
            lstGuessed.append(letter.upper())
            letter = input("guess a letter: ")
        
        tries = tries+1
        if tries > 21:
            print("You lose...")
            print("the word was: "+ ' '.join(api_word))
            break


        