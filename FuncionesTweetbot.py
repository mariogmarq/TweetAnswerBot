import random
import tweepy
import re

#TWEEPY DEPENDENCIES
############################################################################################################
# Authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)

# Api object
api = tweepy.API(auth)
############################################################################################################
#TWEEPY DEPENDENCIES


#Class to store users
#Takes 4 params, name, screenname(@<screenname>), the id and the id of user's last tweet, no need to put lasID
#See someone's id in https://tweeterid.com/
class User:
    def __init__(self, name, screenname, Identificator):
        self.name = name
        self.screenname = screenname
        self.Identificator = Identificator
        self.lastId = ""

#Add users from a textfile
#It reads the text file, each line is an user, it contains name, screenname and the Id, all separated by a whitespace
#The function finally creates a User object array and return it
def UserList(textfile):
    userArray = []
    file = open(textfile, "r")
    for line in file:
        fields = line.split(" ")
        name = fields[0]
        screenn = fields[1]
        Ident = fields[2]
        User = User(name, screenn, Ident) 
        userArray.append(User)
    file.close()
    return userArray

#It reads the answer from a textfile of your choice
def AddAnswer(textfile):
    f = open(textfile, "r")
    array = []
    for line in f:
        phrase = line.split('\n')[0] + " "
        array.append(phrase)
    f.close()
    return array

#It answer the last tweet from a user(is lastID)
def Answer(User, posible_answers):
    num = random.randint(0, len(posible_answers) - 1)
    phrase = posible_answers[num] + "@" + User.screenname
    api.update_status(status = phrase, in_reply_to_status_id = User.lastId)

#Check if there is a new tweet from a user
def NewTweet(User):
    timeline = api.user_timeline(User.Identificator, User.screenname)
    i = 0
    while(timeline[i].is_quote_status==True or timeline[i].in_reply_to_status_id!=None):
        i = i + 1
    if(User.lastId != timeline[i].id_str):
        User.lastId = timeline[i].id_str
        return True
    else:
        return False

#Check if a string is in a textfile
def InFile(text, textfile):
    lecture = open(textfile, "r")
    for line in lecture:
        if line == text:
            return True
    return False

#Check your DMs and if a DM starts with newPhrase it will add it to your text file
def DMAddPhrase(textfile, yourID):
    textfile = open(textfile, "a+")
    DMlist = api.list_direct_messages()
    for DM in DMlist:
        i = 0
        message = ""
        if DM.message_create['target']['recipient_id'] == yourID:
            if re.findall("^newPhrase", DM.message_create['message_data']['text']):
                for x in DM.message_create['message_data']['text']:
                    if i > 0:
                        message = message + x
                    if x == " ":
                        i = i + 1
                if not InFile(message, textfile):
                    textfile.write("\n" + message + " ")
    textfile.close()
