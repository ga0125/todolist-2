# My Tasks
Hey bro! This is a simple web app ToDo List using Django. Here we go!


# Project Structure

	|-- todolist                        // base PATH
	    |-- templates                   // template of the application
		|-- base.html               // base template HTML
		|-- todolist.html           // base template HTML
	    |-- todoapp                     // App PATH of Django, here you can find all created scripts for this application 
		|-- migrations              // migrations from DB
		|-- static                  // Frontend libs. You'll find (boostrap, js and css libs)
		|-- tests                   // template of the application
		    |-- __init__.py         // init file
		    |-- test_urls.py        // unit test for urls
		    |-- test_views.py       // unit test for views
		|-- admin.py                // We can register the models created to the Django admin
		|-- apps.py                 // Register our application
		|-- models.py               // Our model created, we create a link between DB and the viwes.py
		|-- serializers.py          // Created to serialize the API's calls
		|-- urls.py                 // This file is linked with the urls.py from the TodoWeb PATH. We setup our urls calls here
		|-- views.py                // Every request generated of the application (including the API construction)    
	    |-- todolist                // setup files 
	        |-- __init__.py             // generated config Django file
		|-- urls.py                 // generated config Django file. We've set up our urls calls to the urls.py from todoApp
		|-- wgsi.py                 // generated config Django file
	    |-- __init__.py                 // generated config Django file
	    |-- db.sqlite3                  // Our database of the application
	    |-- .gitignore                  // I've set up some files that isn't necessary to clone our project (config from GitHub)
	    |-- readme.md                   // This file
    
# Requirements
To run this applcation you'll need install these guys below:

* Python 3 installed

* Django framework

# Installation

1. Please clone our application running the following command on a terminal: 
```
git clone https://github.com/ga0125/todolist.git
```
2. Setup your Machine:

```
pip install -r requirements.txt
```

# Execution
1. To execute My Tasks, please run the following command on a terminal:
```
python manage.py migrate
python manage.py runserver
```

2. Now you can access the application from your browser here [My Tasks](http://127.0.0.1:8000)


# Test
To execute the unit test, please run the following command on a terminal:
```
python manage.py test todoapp
```

# Application accesses

## User Django-admin

**user:** admin | password: admin

## Pages

**Web application:** [My Tasks](http://127.0.0.1:8000)

**Admin Page:** [My Tasks - Admin](http://127.0.0.1:8000/admin)

**APIs:** [My Tasks - API](http://127.0.0.1:8000/api)

# Archicteture

### •	Frontend

**Used Technologies -** For this project I’ve used HTML 5 (DHTML), CSS3, JS and bootstrap 4 framework. 

**Application’s description -** Please check below the My Task’s description to make the usability clearer for the end user:

## •	Adding a Task:

	o Add a Tile (obligatory field) - You can insert any char value with till 55 characters;

	o Add a Description  - You can add any char value with till 100 characters;
	
	o Choose a Deadline (obligatory field) - On the “Datefield” you can choose a deadline for this task to be inserted;
	
## • Task Filters:

	o "À Fazer" button - Shows only todo tasks;
	
	o "Completas" button - Shows only complete tasks;
	
	o "Arquivadas" button - Shows all filed tasks;
	
## • Controlling a Task:

	o Task line added - Every task, after added on the system, will be showed for the end user like a single line showing only the task Title and some action buttons;

	o Description and deadline task – You can find the “Description button ( ˅ )” on the right div side, when you click the description and deadline task will be  appear on the screen;
	
	o Archive a task – Now, if you need archive a task, you can find a “download box icon” besides of the “Description button”.
	
	o Exclude a task – Now, if you need exclude a task, you can find a “trash icon” besides of the “Archive button”. So, be careful, because every task excluded will not be recovered!
	
	o Complete a Task – When you finish your task (congrats bro!) you just need check the checkbox button and finish it. Off course, every task checked as completed you cannot come back, so make sure that you finish that task at all hehehe;

### •	Backend

**Used Technologies -** For the backend I’ve used Python, Django and Django rest framework.

**DB Structure -** check below the DB structure adopted for this app:

Column | Type | Description
--------- | ------------- | ---------
id |integer |This value is generated automatically by the DB
title |varchar(55)| Char value with till 55 characters
description |varchar(100)|  Char value with till 100 characters
deadline |date| Date value for the deadline date (I got this value using input type date)
complete |Boolean| Boolean value 
filed |Boolean| Boolean value
complete_at |datetime| When the task is checked as complete this field will be inserted with the current datetime

**APIs –** The APIs of this web application was designed using Django rest framework. To have access to these APIs, firstly, you need log in as ‘admin’ on the page [Admin](http://127.0.0.1:8000/admin). After logged, you can access the page [API](http://127.0.0.1:8000/api) and check/test/filter the APIs (Feel free to use it bro!).
*PS: I’ve chose the user permission authentication method to use the APIs for this test.*

# Conclusion

I hope you enjoy the My Tasks, and regardless of the completion of this test, I appreciate the opportunity where I could learn even more.
