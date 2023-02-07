import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers


# setup APIs
from api.user import user_api # Blueprint import api definition
<<<<<<< HEAD
from api.search import search_api
from api.users import users_api






=======
from api.item import item_api
>>>>>>> 312719134342955e94ddc4103d2cec980c46d3f6

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(user_api) # register api routes
app.register_blueprint(app_projects) # register app pages
<<<<<<< HEAD
app.register_blueprint(search_api)
app.register_blueprint(users_api)
=======
app.register_blueprint(item_api)

>>>>>>> 312719134342955e94ddc4103d2cec980c46d3f6

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.before_first_request
def activate_job():
    initJokes()
    initUsers()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
    app.run(debug=True, host="0.0.0.0", port="8086")
