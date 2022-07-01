from flask_app import app
# This is to import application

from flask_app.controllers import users
# This is to import routes
# always have controllers in server.py

if __name__ == "__main__":
  app.run(debug=True)
# This is just to run the server.py 