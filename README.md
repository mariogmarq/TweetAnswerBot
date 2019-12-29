# TweetAnswerBot

## Brief description

Twitter bot that answer people with random messages and people can add messages by DM.

## Requirement

The bot requires tweepy 3.8.0 to work, aside from a two text files of your choice and the FuncionesTweetbot.py file. **You need to put your twitter developer keys in the FuncionesTweetbot.py file in the tweepy dependencies part**

## How does it works

You will find further information in the tweepyBot.py file, but basically you will need a text file to store users, another one to store the answers that your bot will make, a developer twitter account with access to DMs, read and write (in case that you that have access to the DMs you can delete DMAddPhrase function from tweepyBot.py file).

## The User object

The code uses a class User in order to store the user information.

~~~python
class User:
    def __init__(self, name, screenname, Identificator):
        self.name = name
        self.screenname = screenname
        self.Identificator = Identificator
        self.lastId = ""
~~~

## The user textfile

The script will use a function called Userlist which is show beneath in order to store the users from a text file. This function returns an User object array which is used in the main script to answer all the users from the list.

~~~python
def UserList(textfile):
    userArray = []
    file = open(textfile, "r")
    for line in file:
        name = ""
        screenn = ""
        Ident = ""
        i = 0
        for x in line:
            if x != '\n':
                if x == " ":
                    i = i + 1
                elif i == 0:
                    name = name + x
                elif i == 1:
                    screenn = screenn + x
                elif i == 2:
                    Ident = Ident + x
        User = User(name, screenn, Ident) 
        userArray.append(User)
    file.close()
    return userArray
~~~

The text file must have this structure

~~~
User1Name User1Screenname User1Id
User2Name User2Screenname User2Id
Etc.
~~~

You can see someone's id in *https://tweeterid.com/*. Also is worth of mention that screenname is the username to the user, which is the name after the @.

## The answer file

Each phrase must be in a different line.
