# CONFIG
# import Blueprint
from flask import Blueprint

# create new instance of Blueprint
bp = Blueprint(
    # blueprint's name
    'pet',
    # location of blueprint
    __name__,
    # blueprint's url prefix
    url_prefix="/pets"
)