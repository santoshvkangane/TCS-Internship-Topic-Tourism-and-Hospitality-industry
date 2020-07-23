# Tourism-and-Hospitality-industry
Follow the given steps to view my project:
step-1: install pycharm IDE for 64-bit system and install django framework .
step-2: In RUN promt create new project where you want in your system (django-admin startproject Project-name) and new app (django-admin startapp Application-name) for project..[ type "pip" command for help]
step-3: after these, create static and templates folder in your app by just right clicking on Application name.
step-4: set path for these static and templates in settings.py file.
step-5: after these,copy the static files and images in static folder and HTML files in templates folder
step-6: copy the views.py ,models.py, forms.py in your app and urls.py in project folder.
step-7: install XAMPP server for running Apache and MySql server for 64-bit system and set the port number and database type as Mysql in database section of settings.py 
step-8: Now, start the Apache and Mysql server by starting xampp server..In terminal of pycharm IDE type command "python manage.py makemigrations app-name" for creating models , then type "python manage.py    migrate app-name" for applying them, then type "python manage.py migrate" and start the localhost server by typing :"python manage.py runserver".  after these localhost server address will be shown in terminal,simply click on that and you will be getting on localhost server.
step-9: type " http://127.0.0.1:8000/mainpage" on Google chrome or Edge browser and that's it,you are on portal of my project.
