import os, datetime, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Global Variables
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'FoodLibrary'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
page_limit = 6
initial_page = 1
home_page_limit = 3

@app.route('/')
def home():
    """
    Renders the web application home page

    Returns:
        render_template("home.html",...): The home page template
    """
    recently_added_recipes=mongo.db.recipes.find().sort([("date",-1)]).limit(home_page_limit)
    most_viewed_recipes=mongo.db.recipes.find().sort([("clicks",-1)]).limit(home_page_limit)
    return render_template("home.html", recently_added_recipes=recently_added_recipes, most_viewed_recipes=most_viewed_recipes)
    

@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    """
    Renders the web application recipe page for the specified recipe

    Parameters:
        recipe_id (str): The id of the recipe to be rendered

    Returns:
        render_template("recipe.html",...): The recipe page template
    """
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {"$inc":{"clicks": 1}})
    return render_template('recipe.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/recipes')
def get_recipes():
    """
    Renders the web application recipe list page

    Returns:
        render_template("recipes.html",...): The recipe list page template
    """
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

    return render_template('recipes.html', recipes=recipes.sort([("date",-1)]).skip((page-initial_page)*page_limit if page > initial_page else 0).limit(page_limit), page=(page if count > page_limit else None) if page > 0 else initial_page,  previous=previous_url, next=next_url, count=count)   


@app.route('/add_recipe')
def add_recipe():
    """
    Renders the web application page to add a new recipe

    Returns:
        render_template("add_recipe.html",...): The add recipe page template
    """
    return render_template('add_recipe.html', cuisines=mongo.db.cuisines.find().sort([("name", 1)]))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    """
    Inserts a new recipe into the database and redirects 
    the web application to the recipe list page

    Returns:
        redirect(url_for("get_recipes")): Redirects to the recipe list page
    """
    recipe=request.form.to_dict()
    recipe["date"]=datetime.datetime.now()
    mongo.db.recipes.insert_one(recipe)
    return redirect(url_for("get_recipes"))

@app.route('/recipes/<recipe_id>/delete', methods=["POST"])
def delete_recipe(recipe_id):
    """
    Deletes the specified recipe from the database and redirects
    the web application to the recipe list page

    Parameters:
        recipe_id (str): The id of the recipe to be rendered

    Returns:
        redirect(url_for("get_recipes")): Redirects to the recipe list page
    """
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
    Renders the web application edit recipe page for the specified recipe

    Parameters:
        recipe_id (str): The id of the recipe to be rendered

    Returns:
        render_template("edit_recipe.html", ...): Renders the edit recipe page 
    """
    return render_template('edit_recipe.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}), cuisines=mongo.db.cuisines.find().sort([("name", 1)]))

@app.route('/recipes/<recipe_id>/update', methods=["POST"])
def update_recipe(recipe_id):
    """
    Updates the specified recipe in the database and 
    redirects the web application to the specified recipe page

    Parameters:
        recipe_id (str): The id of the recipe to be rendered

    Returns:
        redirect(url_for('get_recipe', recipe_id=recipe_id)): Redirects to the specified recipe page
    """
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, request.form.to_dict())
    return redirect(url_for('get_recipe', recipe_id=recipe_id))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)