# CONFIG
# import blueprint and render_template
from flask import ( Blueprint, render_template )

# create new blueprint

bp = Blueprint(
    "fact",
    __name__,
    url_prefix="/facts"
)

# NEW FACT ROUTE
@bp.route('/new')
def new():
    # you'll have to render the template to get the new route
    # make sure to do that for future stub testing
        # because just adding a return string here and then the link to index.html
        # takes you to /pets/facts/new and that won't work :(
    return render_template('new.html')