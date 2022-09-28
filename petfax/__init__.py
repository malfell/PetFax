# This file lets you work in actual application factory.
# The __init__.py is where you initially configure Flask and write function
# to create the instance of your app.

# import Flask
from flask import Flask
# import flask_migrate
from flask_migrate import Migrate

# APPLICATION FACTORY
# define app factory
def create_app():
    # create new app instance of Flask
    app = Flask(__name__)

    # SQL Alchemy stuff
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    # set modifications on app's config object to false
    # if True, it tracks modifications of objects--feature isn't needed
    # if left unset, the value defaults to None, which takes extra memory--BAD
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # import models
    from . import models
    # got access to SQLAlchemy class methods through models.db now
    # call init_app method on it and pass it the app instance
    models.db.init_app(app)

    # migrate stuff
    migrate = Migrate(app, models.db)

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