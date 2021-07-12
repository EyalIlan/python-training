from math import log
import eel
from pymongo import MongoClient
import random


words = ["oren", "eyal", "chen"] 

def mongo_init():  # Local function
    global user

    client = MongoClient('localhost', 27017)
    db = client.eel_database
    user = db.users
# C:\Users\97250\AppData\Local\Programs\Python\Python39-32


# return callback function

@eel.expose  # Eel function  
def get_word():  # Example to send data for javascript/html
    global words

    word = None

    if len(words) > 0:
        word = words[random.randint(0, len(words)-1)] 
        filtered_list = Filter(word, words)
        words  = filtered_list

    if(len(words) == 0 and word == None):
        eel.SuccessAllWords(len(words))
    else:
        eel.get_word_python(word,len(words)+1)
         

def Filter(word,words):
    arr = []
    for element in words:
        if word != element:
            arr.append(element)
    return arr


@eel.expose  # Eel function
def save_user(email, password):
    dict_user = {"email": email, "password": password}
    user.insert_one(dict_user).inserted_id


@eel.expose  # Eel function
def drop_database():
    client = MongoClient('localhost', 27017)
    client.drop_database('eel_database')


@eel.expose  # Eel function
def get_users():
    all_users = []
    cursor = user.find({})
    for x in cursor:
        x.pop("_id")  # Remove objects id
        all_users.append(x)
    return all_users



# -----------------------------------------------------------

    # list of letters


# ------------------------------------------------------------



if __name__ == '__main__':
    eel.init('client/web')  # Give folder containing web files
    mongo_init()  # Init mongodb
    eel.start('index.html', mode='chrome', size=(1200, 600),
              cmdline_args=['--start-fullscreen'])




