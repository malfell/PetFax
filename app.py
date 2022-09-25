# CONFIG
# Import Flask
from flask import Flask
# create app instance from Flask
app = Flask(__name__)

# INDEX ROUTE
# call .route() on app instance
# need one argument for endpoint: '/'
# to tell route what to do, define a method directly underneath it
@app.route('/')
def index():
    return 'Hello, this is PetFaxxxx!'


# PETS INDEX ROUTE
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'