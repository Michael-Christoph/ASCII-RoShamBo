import img2asciiart_mod
import os
import readchar
import time

heart = img2asciiart_mod.img2asciiart().create_ascii_art("pics/herz.png",20,10).split("\n")

single_space = " "
abstand_vorne = 38*single_space
abstand_mit_mittelstrich = 18*single_space + "|" + 20*single_space

def herzanzeige(lives_player_one,lives_player_two):

    os.system('cls')
    os.system('color 0c')
    
    for i in range(1,max(lives_player_one,lives_player_two)+1):
        for k in range (3):
            print abstand_vorne
        for j in range(len(heart)-1):
            
            print abstand_vorne,
            
            if i <= lives_player_one:
                print heart[j],  
            else:
                print single_space * len(heart[j]),
                
            print abstand_mit_mittelstrich,
            
            if i <= lives_player_two:
                print heart[j]
            else:
                print single_space * len(heart[j])
            
    key_pressed = None
    while key_pressed != u'c':
        print abstand_vorne
        print(abstand_vorne + "Press c to continue ... "),
        key_pressed = readchar.readchar()
    
    os.system('color 07')
    
