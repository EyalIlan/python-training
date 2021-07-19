from flask import Blueprint

from extensions import mongo

main = Blueprint('main',__name__)


@main.route('/')
def index():
    # user_collection = mongo.db.users
    # user_collection.insert({'name':'eyal'})
    return '<h1>hello world </h1>'

# @main.route('/add_score',methods = ['POST'])
# def add_Score():
#     # score = request.from.get('score')
#     return  'hello'



# import requests

# oren =  requests.get('https://api.chucknorris.io/jokes/random')
# oren = oren.json()


# #oren2 = requests.post('https://api.chucknorris.io/jokes/random', data = payload)

#print(oren['value'])