# convintask
Convin Task

# Installation process 

## Install the system dependencies
* **git** 
* **pip**

## Get the code
* Clone the repository

## Install the project dependencies

`pip install -r requirements.txt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## End Points

### Tasks
* `GET /apis/v1/{pk}`
* `POST /apis/v1/{pk}`

### TaskTrackers
* `GET /apis/v2/{pk}`
* `POST /apis/v2/{pk}`
