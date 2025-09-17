**Question 1: Explain how you implemented the checklist above step-by-step!**



CHECKLIST 1: Create a new Django project.

First, I created the Django project by making a local directory named "football-shop" on my laptop, then I created a public GitHub repository with the same name as the local directory. I then opened cmd to start making the Django project by first going to that local directory and entering virtual environment. After that, I created a requirements.txt file inside the directory, filled it with the same thing as what was provided in Tutorial 0 and installed it using "pip install -r requirements.txt". From here until the end, I followed the guide written on Tutorial 0 until I got my Django project initialized. The final look should display the rocket image.



CHECKLIST 2: Create an application named main within the project.

I run the "python manage.py startapp main" after entering virtual environment in the football-shop directory again. I continue setting everything as shown in Tutorial 1.



CHECKLIST 3:Configure routing in the project to run the main application.

I created urls.py in the football\_shop directory and filled it with the necessary code.



from django.contrib import admin

from django.urls import path, include



urlpatterns = \[

&nbsp;   path('admin/', admin.site.urls),

&nbsp;   path('', include('main.urls')),  # Main app routing

]



CHECKLIST 4: Create a model in the main application named Product with the following mandatory attributes:

name as the item name with type CharField.

price as the item price with type IntegerField.

description as the item description with type TextField.

thumbnail as the item image with type URLField.

category as the item category with type CharField.

is\_featured as the featured status of the item with type BooleanField



I opened models.py from the main application in Python and used the model provided in Tutorial 1 and changed some parts to match the context of Football Shop.



CHECKLIST 5: Create a function in views.py to be returned to an HTML template that displays the application name, your name, and your class.

I add the show\_main function from Tutorial 1 and changed the context to fit what was asked in the Assignment 2 url. Then, in main.html which I had previously made, I changed the content to the necessary Django code to display the data. (ex. from PBD KKI to {{ class }})



CHECKLIST 6: Create routing in urls.py of the main application to map the function created in views.py.

I added the necessary code to urls.py in main application which is



from django.urls import path

from main.views import show\_main



app\_name = 'main'



urlpatterns = \[

&nbsp;   path('', show\_main, name='show\_main'),

]





CHECKLIST 7: Deploy the application to PWS so that it can be accessed by your peers via the Internet.



git add .

git commit -m "Complete Assignment 2: Football Shop"

git push origin master

git push pws master





**Question 2: Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.**





https://ibb.co.com/8L4rZ80C (diagram link)



urls.py: Acts as the traffic controller, directing HTTP requests to appropriate views

views.py: Contains business logic, processes requests, and prepares data for templates

models.py: Defines database structure and handles data operations

HTML templates: Render the final presentation layer using data from views





**Question 3: Explain the role of settings.py in a Django project!**



settings.py is the configuration hub of Django project that defines installed applications and middleware, configures database connections, sets up template engines and statis file handling, and configures installed apps and project-specific stuff.





**Question 4: How does database migration work in Django?**



1. Modify models.py for new database structure

2\. generate migration file with python manage.py makemigrations

3\. review migrations, migration file contain SQL operations to apply changes

4\. execute the SQL against database with python manage.py migrate

5\. version tracking, Django tracks applied migrations in django\_migrations table.





**ASSIGNMENT 3**





**Question 1: Why do we need data delivery in implementing a platform?**



Data delivery is important in implementing a platform because it enables dynamic updates and synchronization across distributed systems, efficient data transfer helps with handling and increasing loads and users, facilitates connection with third-party services or external systems and APIs, ensures all components have access to the same latest info, enables responsive applications.



**Question 2: In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?**



In my opinion, JSON is mostly better due to its readability and simplicity. JSON is more popular than XML because it has less verbose syntax with no closing tags which makes the size smaller. It is also easier to read and write. Another is that JSON parses in JavaScript which makes it ideal for web applications.



**Question 3: What is the purpose of the is\_valid() method in Django forms, and why do we need it?**



is\_valid() serves to validate form data and checks if all data conforms to the form's field definitions and constraints. It also converts form dtaa to appropriate Python data types, validates against potential security risks, and gathers all validation errors to display.



**Question 4: Why do we need a csrf\_token when making forms in Django? What can happen if we don't include a csrf\_token in a Django form? How can this be exploited by an attacker?**



We need csrf\_token because CSRF tokens protect against attacks where malicious webs trick users into submitting unwanted requests to your Django app.











