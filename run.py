from flask import Flask
from app import app
from app import models
#initializes the app and the database
if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)
