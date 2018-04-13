import readchar
import os
import time
import ritterkampf_spiellogik_03 as logik
import animation03 as anim
import lebensanzeige

single_space = " "
#globaler Standard-Abstand
abstand = 11*single_space

############## FUNCTIONS (MAIN PROGRAM PLEASE SEE BELOW) ###########################

def start_screen():
    os.system('cls')
    move_cursor_downwards(4)
    for i in range(1,15):
        welcome_message = "Willkommen zum Ritterkampf! "
        print abstand + welcome_message*3
    move_cursor_downwards(4)
    
    key_pressed = None
    while key_pressed != u's':
        print abstand
        print(abstand + "Press 's' to enter the arena ..."),
        key_pressed = readchar.readchar()

def eine_runde():
    os.system('cls')
    move_cursor_downwards(4)
    
    print(abstand + "Spieler 1, waehle deine Waffe! (a = Schwert, w = Lanze, d = Schild)")
    player_one_input = enforce_valid_input(u'a',u'w',u'd')
    
    print abstand
    print(abstand + "Spieler 2, waehle deine Waffe! (j = Schwert, i = Lanze, l = Schild)")
    player_two_input = enforce_valid_input(u'j',u'i',u'l')
    
    time.sleep(0.1)
    count_down(5)
    os.system('cls')

    fight_result = logik.start_fight(player_one_input,player_two_input)
    anim.kampf(player_one_input,player_two_input,fight_result)
    time.sleep(1.5)
    return fight_result

def count_down(num):
    print abstand
    print(abstand +"Vielen Dank, der Countdown beginnt:")
    print abstand
    num = 5
    while num>0:
        print abstand + abstand + str(num)
        time.sleep(0.5)
        num -= 1
    
def enforce_valid_input(a,b,c):
    print abstand,
    player_input = readchar.readchar()
    while player_input not in (a,b,c):
        print "Please enter one of the characters above!"
        print abstand,
        player_input = readchar.readchar()
    print("[Waffe gewaehlt]")
    return player_input
    
def final_screen(lifes_player_one):
    if lifes_player_one == 0:
        picture = anim.to_asciiart("pics/picture_two_wins04.jpg") 
    if lifes_player_one != 0:
        picture = anim.to_asciiart("pics/picture_one_wins05.jpg")    
    anim.display_fight_scene(picture, picture)
    
    print abstand
    print(abstand + "Press 'e' key to exit the program, or any other key for a restart ..."),
    return readchar.readchar()
    
def life_screen(lifes_player_one,lifes_player_two):
    os.system('cls')
    
def play_the_game():
    lifes_player_one = 3
    lifes_player_two = 3
    
    while lifes_player_one > 0 and lifes_player_two > 0:
        eine_runde_result = eine_runde()
        if eine_runde_result == True:
            lifes_player_two = lifes_player_two - 1
        if eine_runde_result == False:
            lifes_player_one = lifes_player_one - 1
    
        lebensanzeige.herzanzeige(lifes_player_one,lifes_player_two)
    
    return lifes_player_one
    
def move_cursor_downwards(lines):
    for i in range (4):
        print abstand
    
############# MAIN PROGRAM ######################################

os.system('MODE 1000,1000')

restart_choice = None
while restart_choice != u'e':
    start_screen()
    lifes_player_one = play_the_game()
    restart_choice = final_screen(lifes_player_one)