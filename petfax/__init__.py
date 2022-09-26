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

    # REGISTER PET BLUEPRINT
    # above return in create_app, import pet file
    from . import pet
    # call register_blueprint method and pass in pet blueprint
    app.register_blueprint(pet.bp)

    # REGISTER NEW FACT BLUEPRINT
    from . import fact
    app.register_blueprint(fact.bp)
    
    # return app instance at the end of the factory
    return app