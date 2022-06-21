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
        
    dict_screen={}
    for key in dict_word:
        dict_screen[key]="__"
        
    return [dict_word,dict_screen]


def recevied():
    letter_recevied=str(input("\nEscribe una letra: "))
    letter_recevied=letter_recevied.strip()
    return letter_recevied


def verified(letter_recevied,dict_word, dict_screen):
    for key in dict_word:
        if dict_word[key]==letter_recevied:
            dict_screen[key]=letter_recevied
            
    return dict_screen


def screen(dicts,words):
    dict_word=dicts[0]
    dict_screen=dicts[1]
    win=True
    
    for value in dict_screen.values():
        if value=="__":
            win=False
            
    if win is False:
        print("Adivina la palabra que estoy pensando: ")
        print("La palabra es:\n")
        for value in dict_screen.values():
            print(value,end=" ")
    
        dict_screen=verified(recevied(),dict_word,dict_screen)
        dicts=[dict_word,dict_screen]
        os.system("cls")
        screen(dicts,words)
    else:
        for value in dict_screen.values():
            print(value,end=" ")
        print("\n")
        print("¡¡You Win!!")
        run(words)
    
    
        
def start(words):
    dicts=generate_dict(words)
    screen(dicts,words)


def run(words):
    print("=====================================\n")
    print("|| Bienvenido al juego del ahorcado.||\n")
    print("=====================================\n")
    answer=input("""Quieres continuar con el juego?
                 1: SÍ
                 2: NO\n:""")
    
    os.system("cls")
    
    if answer.strip() != str(1) and  answer.strip()!=str(2):
        print("Escogió "+answer)
        print("Escriba un opción válida.")
        run(words)
    else:
        if answer.strip()==str(1):
            start(words)
        else:
            print("Escogió: "+answer)
            print("Hasta la próxima!")


    
if __name__ == '__main__':
    words=read()
    run(words)