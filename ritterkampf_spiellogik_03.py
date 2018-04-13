def start_fight (player_one_input, player_two_input):
    if (player_one_input == u'w' and player_two_input == u'i' or player_one_input == u'a' and player_two_input == u'j' or player_one_input == u'd' and player_two_input == u'l'):
        return None
    if (player_one_input == u'a' and player_two_input == u'i'):
        return True		
    if (player_one_input == u'a' and player_two_input == u'l'):
        return False
    if (player_one_input == u'w' and player_two_input == u'j'):
        return False
    if (player_one_input == u'w' and player_two_input == u'l'):	
        return True
    if (player_one_input == u'd' and player_two_input == u'i'):
        return False
    if (player_one_input == u'd' and player_two_input == u'j'):
        return True