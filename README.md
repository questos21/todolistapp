To create a django project

django-admin startproject
how to run a django project

python manage.py runserver
DJANGO PROJECT FILES

    manage.py :: command line utility allowing us to access the django project : entry file
    todolist/ : this directory is the actual python django project
    init.py : this is an empty file that indicates above directory is a python project
    asgi.py : an entry file for ASGI compatible web servers to serve your project
    wsgi.py : an entry file for WSGI compatible web servers to serve your project
    settings.py : settings/configuration file for the django project
    urls.py : these url declarations that map to our django app.

HOW TO CREATE AN APP INSIDE A DJANGO PROJECT

python manage.py startapp
DJANGO APP FILES

    migrations/ : database migration files (empty initially)
    init.py : indicates the app is a python application
    admin.py : used to register models for the django admin panel
    apps.py : contains the app configurations
    models.py : defines the database models (tables)
    tests.py : contains test cases for the app
    views.py : handle request-response logic (functional/controller)
    urls.py (manually created on app level) : define url patterns for the app

JINJA TEMPLATING

This is a syntax used to create django interfaces

    To create templates a. Inside the templates you can create .html files , .css , .js b. To consolidate the templating for our project , modify the following
        set a global templates directory for referencing our templates i.e. move the todolist templates folder to the global perspective i.e. root directory level
    register this change in settings.py for the project under the templates directory settings 'DIRS': [BASE_DIR / 'templates'], # Add this line

STEPS TO INCLUDE DB PERSISTENCY FOR PROJECTS IN DJANGO

models.py : converted to db tables by django After defining our models.py 1/ python manage.py makemigrations appname 2/ python manage.py migrate
STEPS TO ADD A DATA SOURCE

    Double click on the db.sqlite3 file
    Or simply from pycharm select the database icon
    click the + sign or the prompt to create the data source (for development use sqlite3)

RELATION DATABASES : DATABASE RELATIONSHIPS

    One to Many Relationship
        Taskers table (Contain the users who will perform the tasks)
        Task table (Contains the tasks) To establish a one to many relationship establish a ForiengKey
        a unique key pointing to a unique reference in another db table
    many to many relationship

HOW TO ADD IMAGES (STATIC )

    Django uses static directory project-root directory/ => static/ => images/
    Add {% load static %} at the top of the html file
    Add this to the settings.py STATIC_URL = "/static/"

Ensure Django knows where to find static files

STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ] remember to import OS ''
DJANGO ADMIN

Create a super user for content management purposes

    Register your models in admin.py
    Creating a super admin user for the project

python manage.py createsuperuser 3. Visit the link appurl/admin - use the superuser credentials to login
DJANGO APIS (APPLICATION PROGRAMMING INTERFACE)

Is a set of rules that allows different software apps to communicate with each other
Think of an API as a waiter in a restaurant

    You(Frontend/client) make an order(request)
    The waiter(API) takes the request to the kitchen(server/backend)
    The kitchen(server) prepares the food(process the request)
    The waiter(API) brings back the meal(response) to you

TYPES OF APIS

    REST API => Uses HTTP methods ::

    GET :: use this to request data from servers (default)
    POST :: use this to save or send data to servers
    PUT :: use this to update on data on servers
    PATCH :: use this to update only a section of your data
    DELETE :: use this to remove data from your servers

    GraphQL API => Allows clients/frontend to access data only when needed
    SOAP API => Uses XML methods / older (secure)
    WebSocket API => Enable real time data transfer (chat applications)

Steps to create an API project in DJANGO

    Install djangorestframework :: pip install djangorestframework
    Add djangorestframework as part of the installed apps
    Have views return data as .json files
    Create serializers (picking the data to showcase from the API) In the app's api project create a serializers.py file

JSON (JavaScript object notation)

This is an interchangeable data format that can be used across any application

python manage.py startapp todolistappapi pip install djangorestframework : python pipx install djangorestframework --include-deps : python3

FrontEnd(HTML <CSS (web) , Android(Jetpack compose) , React Native , Reactjs) => middleware => backend (server scripting(python->django), database)
AUTHENTICATION AND AUTHORIZATION

    Authentication :: IDENTITY MANAGEMENT :: WHO IS USING THE APP
    Authorization :: USER PRIVILEDGES :: WHAT USER CAN DO ONCE AUTHENTICATED

STEPS IN CREATING AN AUTHENTICATION MODULE

    Within settings.py of the project modify the authentication settings a. LOGIN_URL :: ## redirect unauthenticated users back to the login screen b. LOGIN_REDIRECT_URL :: ## After login what page will the user see c. LOGOUT_REDIRECT_URL :: ## After logout , redirect user back to login screen
    Create views function for the register, login and logout processes
    Create the rendered/redirected templates
    Register the urls to map to the authentication functions in views
    Do migrations :: python manage.py migrate

EXTENDING THE DJANGO AUTH USER MODEL

    Import the class AbstractUser in our models.py

    Create the custom user class , name should be CustomUser

    Tell django to use the custom model for the user : settings.py

    Update our forms to also use the custom model a. create a forms.py in the app folder , write out our custom user form

    Update the views function to use the custom model / form

    Updating the templates to reflect the new inputs :: register.html

    Ensure that our django can handle media a. inside settings.py media_url , media_root b. urls.py include the media reference as part of the urlpatterns

    reset the database and make new migrations
        delete the migration.py file in the migrations folder
        delete db.sqlite file
        python manage.py migrate todolistapp zero
        python manage.py makemigrations appname
        python manage.py migrate

    http://127.0.0.1:8000/ :: web app

    http://127.0.0.1:8000/api/tasks/ :: API project

    http://127.0.0.1:8000/admin :: Admin project

    http://127.0.0.1:8000/register :: Sign Up page for the auth process

