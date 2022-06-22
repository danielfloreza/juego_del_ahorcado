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


def verified(letter_recevied,dict_word, dict_screen,attempts):
    counter=0
    for key in dict_word:
        if dict_word[key]==letter_recevied:
            dict_screen[key]=letter_recevied
            counter+=1
    if counter==0:
        attempts=attempts-1
            
    return [dict_screen,attempts]


def screen(dicts,words,level,lifes, attempts):
    os.system("cls")
    dict_word=dicts[0]
    dict_screen=dicts[1]
    
    print("Nivel: "+str(level))
    print("Vidas restantes: "+str(lifes))
    print("Intentos por palabra: "+str(attempts)+"\n")
    win=True
    
    for value in dict_screen.values():
        if value=="__":
            win=False
    
    if win is False:
        if attempts<=0:
            lifes=lifes-1
            attempts=10
            print("Te quedaste sin intentos para esta palabra y has perdido una vida.\n")
            answer=input("Oprime una tecla para continuar")
            start(words,level,lifes,attempts)
        if lifes <=0:
            print("¡Te has quedado sin vidas! :(\n")
            level=1
            lifes=3
            attempts=10
            answer=input("Oprime una tecla para continuar")
            os.system("cls")
            run(words, level, lifes, attempts)
        else:
            print("Adivina la palabra que estoy pensando: ")
            print("La palabra es:\n")
            for value in dict_screen.values():
                print(value,end=" ")
        
            dict_screen=verified(recevied(),dict_word,dict_screen,attempts)
            dicts=[dict_word,dict_screen[0]]
            attempts=dict_screen[1]
            screen(dicts,words,level,lifes,attempts)
    else:
        for value in dict_screen.values():
            print(value,end=" ")
        print("\n")
        print("¡¡You Win!!")
        print("Has pasado al siguiente nivel\n")
        answer=input("Oprime una tecla para continuar")
        level+=1
        attempts=10
        start(words,level,lifes,attempts)
    
    
        
def start(words,level,lifes,attempts):
    dicts=generate_dict(words)
    screen(dicts,words,level,lifes,attempts)


def run(words,level,lifes,attempts):
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
        run(words,level, lifes, attempts)
    else:
        if answer.strip()==str(1):
            start(words,level, lifes,attempts)
        else:
            print("Escogió: "+answer)
            print("Hasta la próxima!")


    
if __name__ == '__main__':
    words=read()
    level=1
    lifes=3
    attempts=10
    run(words,level,lifes,attempts)