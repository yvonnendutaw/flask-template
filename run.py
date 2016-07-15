from flask import Flask
from my_app import app

#initializes the app and the database
if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)
