from flask import Flask

from .extensions import mongo
from .main import main


def create_app(config_object = 'pymongoexample.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    app.register_blueprint(main)
    return app



# if __name__ == "__main__":
#     app.run()



    
# app.config['MONGO_URI'] = 'mongodb+srv://Oren:9TbD0es5v4fbDrYt@cluster0.4n65p.mongodb.net/Cluster0?retryWrites=true&w=majority'    
# mongo.init_app(app)
# return app

# mongodb+srv://Oren:9TbD0es5v4fbDrYt@cluster0.4n65p.mongodb.net/Cluster0?retryWrites=true&w=majority

# name: Oren
# password 9TbD0es5v4fbDrYt