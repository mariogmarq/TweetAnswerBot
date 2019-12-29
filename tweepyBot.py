############################################################################################################
#Made by mariogmarq
############################################################################################################


#Libraries for proper function of the bot
from FuncionesTweetbot import *
from time import sleep
#Array that store users
users = UserList(UserTextfile)
    
#Array with text answers
posible_answers = AddAnswer(PhrasesTextFile)
while(True):
    DMAddPhrase(PhrasesTextFile, BotId)
    posible_answers = AddAnswer(PhrasesTextFile)
    for user in users:
        try:
            if NewTweet(user):
                Answer(user, posible_answers)
        except:
            api.send_direct_message(YourPersonalID, "Error en User con nombre " + user.name)
    sleep(300)
