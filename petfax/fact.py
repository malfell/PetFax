# CONFIG
# import blueprint and render_template
# import request so you can access POST method
# need to import redirect for the redirect methods!!
from flask import ( Blueprint, render_template, request, redirect )
# import models so you can create instance of Fact model
from . import models

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
    return render_template('facts/new.html')

# POST ROUTE
# Need POST for sending info
# Need GET to redirect to main page
@bp.route('/', methods=['GET', 'POST'])
def index():
    # If there's multiple method requests, need to use if statements
    # But GET is the default, so don't worry about that one
    if request.method == 'POST':
        # variables
        submitter = request.form['submitter']
        fact = request.form['fact']

        # new instance of Fact model using previous variables
        new_fact = models.Fact(submitter=submitter, fact=fact)
        # add new_fact to Flask-SQLAlchemy database session
        models.db.session.add(new_fact)
        # commit database session to insert data into database
        models.db.session.commit()

        # print(request.form)
        # redirect to facts page
        return redirect('/facts')

    return render_template('facts/index.html')