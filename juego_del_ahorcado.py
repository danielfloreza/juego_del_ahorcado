import os
import random


def read():
    with open("./archivos/data.txt","r") as data:
         words = [line.replace("\n","") for line in data]
    return words


def replace_words(actual_word):
    actual_word=actual_word.lower()
    replacements=[
        ("á","a"),
        ("é","e"),
        ("í","i"),
        ("ó","o"),
        ("ú","u"),
        ("ü","u")
        ]
    for a,b in replacements:
        actual_word=actual_word.replace(a,b)
    
    return actual_word

def generate_dict(words):
    actual_word=random.choice(words)
    actual_word=replace_words(actual_word)
    dict_word={}
    for i in range(len(actual_word)):
        dict_word[i]=actual_word[i]    
    return dict_word


def recevied():
    letter_recevied=str(input("\nEscribe una letra: "))
    letter_recevied=letter_recevied.strip()
    return letter_recevied


def verified(letter_recevied,dict_word, dict_screen):
    for key in dict_word:
        if dict_word[key]==letter_recevied:
            dict_screen[key]=letter_recevied
            
    return dict_screen


def screen(dict_word,dict_screen):
    win=True
    for value in dict_screen.values():
        if value=="__":
            win=False
    if win is False:
        print("La valabra es:\n")
        for value in dict_screen.values():
            print(value,end=" ")
    
        dict_screen=verified(recevied(),dict_word,dict_screen)
        os.system("cls")
        screen(dict_word,dict_screen)
    else:
        for value in dict_screen.values():
            print(value,end=" ")
        print("\n")
        print("¡¡You Win!!")
        answer=input("\nQuieres seguir jugando? 1:Si o 2:No\n")
        if answer==str(1):
            run()
        else:
            print("Hasta la próxima!!")
    
    
    
    
def run():
    print("He seleccionado una palabra al azar, puedes adivinarla?")
    dict_word=generate_dict(read())
    dict_screen={}
    for key in dict_word:
        dict_screen[key]="__"
    screen(dict_word, dict_screen)

    


if __name__ == '__main__':
    run()