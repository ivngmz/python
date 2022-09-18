from flask import Flask, render_template

# Instanciate Class,
# Name is a special variable. 
# When script is runned takes name: main. If the script is called by another script take its name: script1
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)
