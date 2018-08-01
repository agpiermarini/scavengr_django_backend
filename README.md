# Scavengr Backend API (Django)
This API serves as the backend to the [Scavengr](https://scavengr-rails.herokuapp.com/) application.

Local setup instructions and information regarding each of the available endpoints is below.

___
### Setup
To run this application locally, first clone the repository:

```
$ git clone https://github.com/agpiermarini/scavengr_django_backend
```

Start a virtual environment at the root directory, then run the following commands to install and update all dependencies:

```
$ pip install -r requirements.txt
```

Next, initialize the database:

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Then, spin up a server on port 3000:

```
$ python3 manage.py runserver 3000
```

___
### Contribute

Fork the [repository](https://github.com/agpiermarini/scavengr_django_backend) if you would like to contribute to this project. Pull requests will be considered in kind, but please note that contributions must adhere to a test-driven, rebase workflow.

This project uses Django's built-in test framework. Run tests using the standard `$ python3.7 manage.py test` command.


#### Current Contributors
[Evan Wheeler](https://github.com/anon0mys)  
[Andrew Piermarini](http://www.github.com/agpiermarini)

### Versions
Python 3.7  
Django 2.0  
Django Rest Framework  


### Token Authentication

All requests (with the exception of POST requests to `/api/v1/users/`) require a user token to be passed in an Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings, as follows:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Instructions for retrieving a user's token are included in the endpoint details below.


___
### Endpoints

Production Base URL:  https://scavengr-django.herokuapp.com/
Local Base URL:       http://localhost:3000


#### Authentication Endpoint

**POST /api/v1/authenticate/**  
Returns user record, which includes authentication token that should be passed in subsequent requests in an Authorization HTTP header

Request URL
```
/api/v1/authenticate/
```

Required parameters
```
{
  "username": "username",
  "password": "password"
}
```

Response body
```
{
  "id": 1,
  "username": "user",
  "email": "user@email.com"
  "token": <unique token>
}
```

Status code
```
200
```


#### User Endpoints

**POST /api/v1/users/**  
Creates a user record

Request URL
```
/api/v1/users/
```

Required parameters
```
{
  "username": "user",
  "email": "user@email.com",
  "password": "password"
}
```

Response Body
```
{
  "id": 1,
  "username": "user",
  "email": "user@email.com"
  "token": <unique token>
}
```

Response Code
```
201
```

**GET /api/v1/users/:username/scavenger_hunts/**  
Returns all scavenger hunt records for user corresponding to :username

Request URL
```
/api/v1/users/:username/scavenger_hunts/
```

Response Body
```
[
  {
    "id": 1,
    "name": "Scavenger Hunt 1",
    "description": "Scavenger Hunt 1 description",
    "user_id": 1,
    "username": "username1"
  },
  {
    "id": 2,
    "name": "Scavenger Hunt 2",
    "description": "Scavenger Hunt 2 description"
    "user_id": 1,
    "username": "username1"
  },
  {...}
]
```

Response code
```
200
```


#### ScavengerHunt Endpoints

**GET /api/v1/scavenger_hunts/**  
Returns all scavenger hunt records

Request URL
```
/api/v1/scavenger_hunts/
```

Response Body
```
[
  {
    "id": 1,
    "name": "Scavenger Hunt 1",
    "description": "Scavenger Hunt 1 description",
    "user_id": 1,
    "username": "username1"
  },
  {
    "id": 2,
    "name": "Scavenger Hunt 2",
    "description": "Scavenger Hunt 2 description"
    "user_id": 2,
    "username": "username2"
  },
  {...}
]
```

Response code
```
200
```

**GET /api/v1/scavenger_hunts/:id**  
Returns scavenger hunt record corresponding to :id

Request URL
```
/api/v1/scavenger_hunts/:id
```

Response Body
```
{
  "id": 1,
  "name": "Scavenger Hunt 1",
  "description": "Scavenger Hunt 1 description"
}
```

Response code
```
200
```

**POST /api/v1/scavenger_hunts/**  
Creates a scavenger hunt record associated with the authenticated user

Request URL
```
/api/v1/scavenger_hunts/
```

Required parameters
```
{
  "name": "Scavenger Hunt",
  "description": "Scavenger Hunt description"
}
```

Response Body
```
{
  "id": 1,
  "name": "Scavenger Hunt",
  "description": "Scavenger Hunt description",
  "user_id": 1,
  "username": "username"
}
```

Response code
```
200
```

**PUT/PATCH /api/v1/scavenger_hunts/:id**  
Updates scavenger hunt record corresponding to :id

Request URL
```
/api/v1/scavenger_hunts/
```

Required parameters
```
{
  "name": "Updated Scavenger Hunt name",
  "description": "Updated Scavenger Hunt description"
}
```

Response Body
```
{
  "id": 1,
  "name": "Updated Scavenger Hunt name",
  "description": "Updated Scavenger Hunt description",
  "user_id": 1,
  "username": "username"
}
```

Response code
```
200
```

**DELETE /api/v1/scavenger_hunts/:id**  
Deletes scavenger hunt record corresponding to :id

Request URL
```
/api/v1/scavenger_hunts/:id
```

Response code
```
204
```

#### CurrentScavengerHunt Endpoints

**POST /api/v1/current_scavenger_hunts/**  
Creates a joins record for the authorized user and a scavenger hunt that they have started

Request URL
```
/api/v1/current_scavenger_hunts/
```

Required parameters
```
{
  "scavenger_hunt_id": 1
}
```

Response Body
```
None
```

Response code
```
200
```

**GET /api/v1/current_scavenger_hunts/**  
Returns all current scavenger hunts associated with the authorized user

Request URL
```
/api/v1/current_scavenger_hunts/
```

Response Body
```
[
  {
    "scavenger_hunt_id": 1,
    "user_id": 1,
    "created_at": '2018-07-30'
  },
  {
    "scavenger_hunt_id": 2,
    "user_id": 1,
    "created_at": '2018-07-30'
  },
  {...}
]
```

Response code
```
200
```
