import os
import random


def read():
    words = []
    with open("./archivos/data.txt","r") as data:
        for line in data:
            line = line.replace("\n","")
            words.append(line)    
    return words


def generate_dict(words):
    actual_word=random.choice(words)
    dict_word={}
    for i in range(len(actual_word)):
        dict_word[i]=actual_word[i]    
    return dict_word


def recevied():
    letter=str(input("\nEscribe una letra: "))
    letter=letter.strip()
    return letter


def verified(received,dict_word, dict_screen):
    for key in dict_word:
        if dict_word[key]==received:
            dict_screen[key]=received
            
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