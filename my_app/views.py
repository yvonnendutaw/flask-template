from my_app import app

@app.route('/')
def home():
	return "Hello welcome"
