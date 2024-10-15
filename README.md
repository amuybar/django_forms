# Django Forms Learning Project

### This is a simple Django project to explore and learn the basics of handling forms, customizing form fields, and applying CSS styling using Bootstrap.

## Project Overview
In this project, I created a form with fields for a user's name, email, and message. The form has been styled using Bootstrap's form-control class for better responsiveness and user experience. I also learned how to set placeholders and other HTML attributes to form fields dynamically through Django's form class.

## Features
#### *.A simple Contact Form with three fields: Name, Email, and Message.
#### *.Each field is styled with custom placeholders and Bootstrap's CSS classes.
#### *.CSRF protection is included in the form for security.
#### *.The form is rendered using Django’s template system.


## Folder Structure

```
project/  
├── learning_forms  
├── manage.py  
├── myforms/            
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── models.py  
│   ├── views.py              
│   ├── templates/             
│   │   └── home.html          
│   ├── static/                  
│   │   └── css/               
│   │       └── home.css       
│   └── forms.py   

```
## Installation
Clone the repository:

```
git clone https://github.com/amuybar/django_forms.git  

cd django_forms 
```

Run the Django development server:

```
python manage.py runserver
```
Access the app at 
`http://127.0.0.1:8000/.`