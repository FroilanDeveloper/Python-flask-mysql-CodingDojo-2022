from flask import Flask
# Import flask object from flask module

DATABASE ="login_registration_schema"
# This is for models 

app = Flask(__name__)

app.secret_key = "ItsSoHardToUnderstandMustNEEDTOUNDERSTAND"