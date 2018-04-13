import img2asciiart_mod
import os
import time

def kampf(player_one_input,player_two_input,player_one_won):

    os.system('cls')

    #convert input into asciiart
    if player_one_input == u'a':
        picture_one_file = "pics/schwert5_grafik_nach_rechts.jpg"
    if player_one_input == u'w':
        picture_one_file = "pics/lanze2_nach_rechts.jpg"
    if player_one_input == u'd':
        picture_one_file = "pics/schild2.png"
    if player_two_input == u'j':
        picture_two_file = "pics/schwert6_grafik_nach_links.png"
    if player_two_input == u'i':
        picture_two_file = "pics/lanze1_nach_links.jpg"
    if player_two_input == u'l':
        picture_two_file = "pics/schild2.png"
    picture_one = to_asciiart(picture_one_file)
    picture_two = to_asciiart(picture_two_file)
    
    abstand_links = display_fight_scene(picture_one,picture_two)
    
    display_result_scene(picture_one,picture_two,player_one_won,abstand_links)
        
def display_fight_scene(picture_one,picture_two):
    single_space = " "
    abstand_mitte = single_space*50
    abstand_links = single_space*2

    while len(abstand_mitte)>1:
        os.system('cls')
        for i in range(max(len(picture_one), len(picture_two))):
            print abstand_links,
            if i<len(picture_one):
                print picture_one[i],
                print abstand_mitte,
            if i<len(picture_two):   
                print picture_two[i]
        abstand_mitte = abstand_mitte[:-2]
        abstand_links = abstand_links + " "
        time.sleep(0.05)
    return abstand_links
        
def display_result_scene(picture_one,picture_two,player_one_won,abstand_links):
    
    picture_one_wins = to_asciiart("pics/picture_one_wins05.jpg")
    picture_two_wins = to_asciiart("pics/picture_two_wins04.jpg")
    tie = to_asciiart("pics/tie02.jpg")
    abstand_mitte = " "
    
    if player_one_won == False:
        print_two_asciiarts(picture_two_wins,picture_two,abstand_links,abstand_mitte)
    
    if player_one_won == True:
        print_two_asciiarts(picture_one,picture_one_wins,abstand_links,abstand_mitte)
        
    if player_one_won == None:
        print_two_asciiarts(tie,tie,abstand_links,abstand_mitte)

def print_two_asciiarts(ascii1,ascii2,abstand_links,abstand_mitte):
    os.system('cls')
    for i in range(max(len(ascii1),len(ascii2))):
        print abstand_links,
        if i<len(ascii1):
            print ascii1[i],
            print abstand_mitte,
            print "|",
        if i<len(ascii2):
            print ascii2[i]
            
def to_asciiart(file_name):
    return img2asciiart_mod.img2asciiart().create_ascii_art(file_name,50,38).split("\n")
