# CONFIG
# import Blueprint
from flask import Blueprint

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
    return "This is the pets index"