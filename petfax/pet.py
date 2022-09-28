# CONFIG
# import Blueprint, render_template
from flask import ( Blueprint, render_template)
# needed for displaying data (at least when data is in a JSON file format)
import json

# open pets.json file, though it still won't be readable for Python yet
# needs to be passed through json.load() for python to read it
pets = json.load(open('pets.json'))
# test to make sure data loads correctly!
# print(pets)

# create new instance of Blueprint
# then need: blueprint's name, location of blueprint, and blueprint's url prefix
bp = Blueprint(
    'pet',
    __name__,
    url_prefix="/pets"
)

# INDEX ROUTE
@bp.route('/')
def index():
    # to get the pet data info, must pass pets as a second arg
    return render_template('pets/index.html', pets=pets)


# SHOW PET ROUTE
# the id is an int, so need to have int before id
# probably best to search pet by id in case two pets have same name
@bp.route('/<int:id>')
def show_pet(id):
    # return f"The pet id is: {id}"
    # need to seek out specific pet's idea
    # and subtract 1 from the id since python index starts at 0
    pet = pets[id-1]
    return render_template('pets/show.html', pet=pet)