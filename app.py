import os, datetime, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'FoodLibrary'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
page_limit = 6
initial_page = 1

@app.route('/')
def home():
    recently_added=mongo.db.recipes.find().sort([("date",-1)]).limit(3)
    top_four=mongo.db.recipes.find().sort([("clicks",-1)]).limit(3)
    return render_template("home.html", recently_added=recently_added, top_four=top_four)
    

@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {"$inc":{"clicks": 1}})
    return render_template('recipe.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/recipes')
def get_recipes():
    search=request.args.get('search')
    page = request.args.get('page')
    if not page:
        return redirect('/recipes?page=1')
    try:
        page = int(page)
    except (TypeError, ValueError):
        return redirect('/recipes?page=1')
    query={} if not search else {'name':re.compile(rf'{search}',re.I)}
    count=mongo.db.recipes.count(query)
    recipes=mongo.db.recipes.find(query)
    previous_url=url_for('get_recipes', page=page-1, search=search) if page > initial_page else None
    next_url=url_for('get_recipes', page=page+1, search=search) if page*page_limit < count else None

    return render_template('recipes.html', recipes=recipes.sort([("date",-1)]).skip((page-initial_page)*page_limit if page > initial_page else 0).limit(page_limit), page=(page if count > page_limit else None) if page > 0 else initial_page,  previous=previous_url, next=next_url)   


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', cuisines=mongo.db.cuisines.find().sort([("name", 1)]))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipe=request.form.to_dict()
    recipe["date"]=datetime.datetime.now()
    mongo.db.recipes.insert_one(recipe)
    return redirect(url_for("get_recipes"))

@app.route('/recipes/<recipe_id>/delete', methods=["POST"])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}), cuisines=mongo.db.cuisines.find().sort([("name", 1)]))

@app.route('/recipes/<recipe_id>/update', methods=["POST"])
def update_recipe(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, request.form.to_dict())
    return redirect(url_for('get_recipe', recipe_id=recipe_id))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)