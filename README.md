<h1 align="center">theFoodLibrary</h1>

<h2 align="center"> MS3 - Data Centric Development - Code Institute </h2>

This project is a recipes dictionary. The main goal is to make it possible for the users to find, add, update/edit and delete recipes. 

## User Experience (UX)

-   ### User stories
    
    -   #### User Goals
        
        1. As a User, I want to easily understand the purpose of the website.
        2. As a User, I want to be able to have access to all the recipes.
        3. As a User, I want to be able to add a new recipe.
        4. As a User, I want to be able to update/edit a recipe.
        5. As a User, I want to be able to delete a recipe.
        6. As a User, I want to be able to search for any recipe by name.
        
        #### Frequent User Goals
        
        1. As a Frequent User, I want to be able to check if there are any new recipes added.
        2. As a Frequent User, I want to be able to check which recipes are the most viewed/popular.
       
        
-   ### Design

    -   #### Colour Scheme
        -   The colour used in this project is green - specifically #269014. I picked this colour because it is often used in food related websites and it is also a warm and very friendly colour to look at. 
        
    -   #### Typography
        -   The font-family "Josefine Sans" is the one used for the logo. For the website content the font-family used is "Open Sans". Sans Serif is the fallback font used in case  'Josefin Sans' and/or "Open Sans" are not being imported into the project correctly.

    -   #### Imagery
        -   All the images are food related. The user can add an image for each and every added recipe by adding a URL to the image field. As adding an URL for the image is not a requirement, a default image (website logo) will be displayed instead.
        
## Features

-   Responsive on all device sizes

-   The user has access to all the recipes by clicking on the "Recipes" button on the navigation bar. The recipes are displayed on cards that include a recipe image(or default image), recipe name and preparation time. 

-   There are 6 recipe cards displayed per page, at the bottom of the "Recipes" page the user can use the arrows to move the previous or next page of recipes.

-   The user can add a new recipe by clicking on the "Add Recipe" button on the navigation bar.

-   The user can edit/update or delete a recipe by clicking on the "edit" or "delete" buttons, respectively. The buttons can be found at the bottom of each recipe page.

-   The user can use a search bar to look for a recipe by name. The search bar is located in the "Recipes" page, above the recipe cards.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the "Josefin Sans" and "Open Sans" fonts into the style.css file, which are the fonts used in this project.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Figma:](https://figma.com/)
    - Figma was used to create the wireframes for this project.
1. [Pymongo:](https://pymongo.readthedocs.io/en/stable/#)
    - The PyMongo library was used for interaction with the MongoDB database through Python.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask was the framework used to build the application.

## Deployment

### GitHub Pages

I used the following procedure to deploy my project to GitHub pages: 

-  Logged in to Github and opened the repository pages.
-  Accessed the "Settings" and scrolled down to the source field. Then, changed the "Branch" to Master instead of "None". 
-  The page was automatically reloaded and by scrolling down to the "GitHub Pages" section I could verify that the project was published.

### Forking the GitHub Repository

Forking the GitHub repository allows other developers to make a copy and work on it without changing the original. As a developer, you can fork a repository as follows:

-  Access the repository and click on the "Fork" button(located at the top right corner of the page), and a copy of the original repository will be created in your own account.

### Making a Local Clone

To make a local Clone, do the following:

-  Open the repository and click on the green button saying "Code". By clicking on it a dropdown menu reveals the "Clone with HTTPS" link, which can then be copied.
-  Open Git Bash and change the directory to the desired working location for the clone. After that, use the `git clone` command and paste the link that was copied ealier. 

Below is an example of what is seen on screen when the clone is being created:


```
$ git clone https://github.com/USERNAME/REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Credits

### Media

-   The hero image is from the free stock image library [Jooinn](https://jooinn.com/).

### Acknowledgements

-   My Mentor for continuous helpful feedback.
