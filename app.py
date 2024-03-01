
from flask import Flask, render_template, request,flash
import requests

app = Flask(__name__)

# Replace with your actual Edamam API key
EDAMAM_API_KEY = "02c16f1b8b87d31df6d2852098b8d1cd"



from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


import os



app = Flask(__name__)
app.config["SECRET_KEY"] = "db24c608640f5034b30b8e1e1eb5618ed0ffdbf5"
# Set up Flask-PyMongo
app.config["MONGO_URI"] = f"mongodb+srv://kaushalcoder:.BDLP$v6ucsi5yB@saces.vv0oomh.mongodb.net/?retryWrites=true&w=majority&appName=saces"


from pymongo import MongoClient
password=os.environ.get("MONGO_PWD")
Connectionstr=f"mongodb+srv://kaushalcoder:.BDLP$v6ucsi5yB@saces.vv0oomh.mongodb.net/?retryWrites=true&w=majority&appName=saces"
client =MongoClient(Connectionstr)



# Create a MongoClient instance
client = MongoClient(Connectionstr)

# Access the desired database and collection
db = client.reviews  # Replace 'mydatabase' with your actual database name
collection = db.saces_data  # Replace 'mycollection' with your actual collection name
# Assuming you have already connected to the MongoDB server
# ...

# F

# Define a simple form
class MyForm(FlaskForm):
    name = StringField('Enter your name')
    review = StringField('Enter your review')
    submit = SubmitField('Submit')



#routes-section
@app.route('/',methods=['GET','POST'])
def HomePage():
    return render_template('main-page.html')

@app.route('/games-index',methods=['GET','POST'])
def Gamesection():
       return render_template('games-index.html')

@app.route('/snake-game',methods=['GET','POST'])
def SnakeGame():
     return render_template('snake-html.html')

@app.route('/Rock-Paper-Scissors',methods=['GET','POST'])
def RPSGame():
     return render_template('index-rps.html')

@app.route('/tic-tac-toe',methods=['GET','POST'])
def XOGame():
     return render_template('index-tictac.html')




@app.route('/recipe',methods=['GET','POST'])
def RecipeSearch():

    if request.method == 'POST':
        query = request.form.get('query')
        recipes = search_recipes(query)
        return render_template('display.html', recipes=recipes)
    return render_template('home.html')

def search_recipes(query):
    url = f"https://api.edamam.com/search?q={query}&app_id=07ee312a&app_key={EDAMAM_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get('hits', [])

    
if __name__ == '__main__':
    app.run(debug=True)
