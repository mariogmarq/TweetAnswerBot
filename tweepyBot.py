############################################################################################################
#Made by mariogmarq
############################################################################################################


#Libraries for proper function of the bot
from FuncionesTweetbot import *
from time import sleep
#Array that store users
users = UserList("usuarios.txt")
    
#Array with text answers
posible_answers = AddAnswer("frases.txt")
while(True):
    DMAddPhrase("frases.txt", "1189652909316808705")
    posible_answers = AddAnswer("frases.txt")
    for user in users:
        try:
            if NewTweet(user):
                Answer(user, posible_answers)
        except:
            api.send_direct_message("1050514751242014721", "Error en User con nombre " + user.name)
    sleep(300)