# This file lets you work in actual application factory.
# The __init__.py is where you initially configure Flask and write function
# to create the instance of your app.

# import Flask
from flask import Flask

# APPLICATION FACTORY
# define app factory
def create_app():
    # create new app instance of Flask
    app = Flask(__name__)

    # INDEX ROUTE
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # return app instance at the end of the factory
    return app