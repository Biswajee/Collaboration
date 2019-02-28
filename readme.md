## Collaboration

### Introduction
The release `v1.0` of the repository contains functionalities where users can upload multiple image files to the server and view them after upload.

### Prerequisites
+ Django 1.11
+ MySQL
+ Python 3.6

### Getting started
+ Clone the repository using
`git clone https://github.com/Biswajee/Collaboration.git`

+ `cd` into the directory `Collaboration` and create a `python` environment
      Using conda:
      conda create -n collabenv

      using python3:
      python3 -m venv collabenv

+ Activate the environment
      Using conda:
      source activate yourenvname

      Using python3:
      source tutorial-env/bin/activate

+ Type in `pip install requirements.txt` to install required packages

+ Run MySQL client at default port `(:3306)` and start the `MySQL Client`.
Now type in the following: `create database collab;`

+ Now, run the `django database migrations` using:
      python manage.py makemigrations
      python manage.py migrate

+ Now, start the django server using:
      python manage.py runserver

### Navigation and running

Visit the site on `127.0.0.1:8000` (or any other port you configured it to rum) and fill up the form. Click on `create` button to submit the form and visit a new link `/image_list/` to find a list of your uploaded images.

### Directory structure

The `dashboard` directory contains utility to upload images and display them.
Static files for website are stored inside `static` directory. The uploaded images are stored in the `media` directory present inside `dashboard` directory.

The Overall directory structure can be viewed as :
```
C:.
│   .gitignore
│   manage.py
│   readme.md
│   requirements.txt
│
├───collaboration
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           
│           
├───dashboard
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │       
│   ├───static
│   │   ├───css
│   │   └───js
│   │           essentials.js
│   │
│   ├───templates
│   │   └───dashboard
│   │       │   display.html
│   │       │   header.html
│   │       │   index.html
│   │       │   upload_error.html
│   │       │
│   │       └───includes
│   └───__pycache__
│           
└───media
```

### Release v1.0 demonstration:

![Release v1.0 - Django Image Gallery](https://user-images.githubusercontent.com/26689027/53584818-81d1cc00-3baa-11e9-86a4-3a3dffa8b148.gif)
