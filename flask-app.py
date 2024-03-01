
from flask import Flask, render_template, request,flash
import requests

app = Flask(__name__)

# Replace with your actual Edamam API key
EDAMAM_API_KEY = "02c16f1b8b87d31df6d2852098b8d1cd"



from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os



load_dotenv()  # Load environment variables
password = os.environ.get("MONGO_PWD")

app = Flask(__name__)
app.config["SECRET_KEY"] = "db24c608640f5034b30b8e1e1eb5618ed0ffdbf5"
# Set up Flask-PyMongo
app.config["MONGO_URI"] = f"mongodb+srv://kaushalcoder:.BDLP$v6ucsi5yB@saces.vv0oomh.mongodb.net/?retryWrites=true&w=majority&appName=saces"
mongodb_client = PyMongo(app)

from pymongo import MongoClient
password=os.environ.get("MONGO_PWD")
Connectionstr=f"mongodb+srv://kaushalcoder:.BDLP$v6ucsi5yB@saces.vv0oomh.mongodb.net/?retryWrites=true&w=majority&appName=saces"
client =MongoClient(Connectionstr)

# Assuming you have already connected to the MongoDB server
from pymongo import MongoClient

# Create a MongoClient instance
client = MongoClient(Connectionstr)

# Access the desired database and collection
db = client.reviews  # Replace 'mydatabase' with your actual database name
collection = db.saces_data  # Replace 'mycollection' with your actual collection name
# Assuming you have already connected to the MongoDB server
# ...

# Fetch all documents from the collection
all_documents = collection.find()
data_cursor = db.saces_data.find()

    # Convert the cursor to a list of dictionaries
data_list = list(data_cursor)

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


@app.route('/feedback', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process form data
        name = form.name.data
        review = form.review.data

        # Save the review to MongoDB
        review_data = {
            'name': name,
            'review': review
        }
        try:
            db.saces_data.insert_one(review_data) 
             # Use the correct collection name
            return f"Thank you, {name}, for your review: {review}"
        except Exception as e:
            return "Error saving review: {str(e)}"
    return render_template('index.html',form = form)    
@app.route('/display_data')
def display_data():
    # Fetch data from MongoDB collection (e.g., 'saces_data')
    data_cursor = db.saces_data.find()

    # Convert the cursor to a list of dictionaries
    data_list = list(data_cursor)

    # Render an HTML template and pass the data to it
    # (You'll need to create an HTML template for displaying the data)
    return render_template('display_data.html', data=data_list)



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
