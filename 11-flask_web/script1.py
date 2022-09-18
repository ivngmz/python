from flask import Flask

# Instanciate Class,
# Name is a special variable. 
# When script is runned takes name: main. If the script is called by another script take its name: script1
app = Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here"

@app.route('/about/')
def about():
    return "Hello, this web is designed by Ivan"

if __name__=="__main__":
    app.run(debug=True)
