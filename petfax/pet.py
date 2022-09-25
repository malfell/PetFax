# CONFIG
# import Blueprint and render_template
from flask import ( Blueprint, render_template)

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
    return render_template('index.html')