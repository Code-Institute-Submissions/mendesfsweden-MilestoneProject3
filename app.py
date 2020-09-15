import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'FoodLibrary'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def home():
    recently_added=mongo.db.recipes.find().sort([("date",-1)]).limit(4)
    top_four=mongo.db.recipes.find().sort([("clicks",-1)]).limit(4)
    return render_template("home.html", recently_added=recently_added, top_four=top_four)
    #calculate top 4 and 4 recently added

@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {"$inc":{"clicks": 1}})
    return render_template('recipe.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)