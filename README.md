# honours

honours is an attempt to clone [awwwards](https://www.awwwards.com/). This repository contains the API. The front-end can be found [here](https://github.com/ThukuWakogi/honours-face).

## author

Timothy Oliver [@ThukuWakogi](https://github.com/ThukuWakogi)

## features

1. login, register and sign out
2. view projects
3. add project

## SetUp

To view a demo of the application, click [here](https://thukuwakogi.github.io/honours-face/).

The source code for this application can be accessed.

a copy of the source code can be gotten through:

- downloading the zip from github.
- opening a terminal in the preferred directory then entering `git clone https://github.com/ThukuWakogi/honours.git`
- using a git client such as [Github desktop](https://desktop.github.com/) or [GitKraken](https://www.gitkraken.com/)

### installing

#### windows

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python -m venv virtual`
* Activating the virtual environment may change based on the terminal or shell being used.
* For command prompt, enter `virtual\Scripts\activate` or simply type in activate.
* For powershell, the execution policy should be bypassed for the script to run. This can be done by entering `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then proceeding on with entering .`.\virtual\Scripts\Activate.ps1`
* Install packages. `pip install -r requirements.txt`
* open a psql client and create a database called filtered_lenses `CREATE DATABASE filtered_lenses;`
* Setting environment variables differs with the terminal or shell being used
* make the migration files `python manage.py makemigrations gallery`
* migrate the database `python3.6 manage.py migrate`
* then start the server `python manage.py runserver`

#### unix

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python3.x -m venv --without-pip virtual` replace x with version in host machine, preferably version v3.6 for this project
* Activate the virtual environment `source virtual/bin/activate`
* Download pip into the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install packages. `pip install -r requirements.txt`
* open a psql client and create a database called filtered_lenses `CREATE DATABASE filtered_lenses;`
* make the migration files `python manage.py makemigrations gallery`
* migrate the database `python3.6 manage.py migrate`
* start the server `python3.x manage.py runserver`

## Development tools
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Angular](https://angular.io/)
* [Angular Material](https://material.angular.io/)
* [Postgresql](https://www.postgresql.org/)
* HTML
* CSS

## license
This project is under the MIT license. click [here](https://github.com/ThukuWakogi/honours/blob/master/LICENSE) for more details
