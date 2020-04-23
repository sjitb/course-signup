# course-signup


## API Implementation

There are implemented Five models: Assistant, Student, Professor, Course and Department.

Main libraries used:
1. Flask-RESTful - restful API library.
2. Flask-Script - provides support for writing external scripts.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── app.py
├── endpoints
│   ├── __init__.py
│   ├── assistants
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   ├── courses
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   ├── departments
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   ├── professors
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   └── students
│       ├── __init__.py
│       ├── model.py
│       └── resource.py
├── manage.py
├── requirements.txt
└── settings.py
```

* endpoints - holds all endpoints.
* app.py - flask application initialization.
* settings.py - all global app settings.
* manage.py - script for managing application 

## Running 

1. Clone repository.
2. `pip install requirements.txt`
3. Create Virtual Environment:<br>
`python -m venv env`
4. Launch Python Virtual Environment by executing:<br>
`.\env\Scripts\activate`
5. Set up database: <br>
    `python manage.py db init` <br>
    `python manage.py db migrate` <br>
    `python manage.py db upgrade` <br>
6. Start server by running:<br> 
`python manage.py runserver`

## Usage
### Users endpoint
POST http://127.0.0.1:5000/api/courses

REQUEST
```json
{
	"Id": "CS101",
    "Name": "Operating System Concepts",
    "Department": "Computer Science",
    "Semester": "Fall",
    "Year": 2020,
    "Department_Id": 1
}
```
RESPONSE
```json
{
	"Id": "CS101",
    "Name": "Operating System Concepts",
    "Department": "Computer Science",
    "Semester": "Fall",
    "Year": 2020,
    "Is_Active": 1,
    "Department_Id": 1
}
```
PUT http://127.0.0.1:5000/api/courses/cs101

REQUEST
```json
{
	"Id": "CS101",
    "Name": "Operating System Concepts",
    "Department": "Computer Science",
    "Semester": "Spring",
    "Year": 2021,
    "Department_Id": 1
}

```
RESPONSE
```json
{
	"Id": "CS101",
    "Name": "Operating System Concepts",
    "Department": "Computer Science",
    "Semester": "Spring",
    "Year": 2021,
    "Is_Active": 1,
    "Department_Id": 1
}
```

GET http://127.0.0.1:5000/api/courses

RESPONSE
```json
{
    "count": 2,
    "courses": [
        {
            "Id": "CS101",
            "Name": "Operating System Concepts",
            "Department": "Computer Science",
            "Semester": "Spring",
            "Year": 2021,
            "Is_Active": 1,
            "Department_Id": 1
        },
        {
            "Id": "CS101",
            "Name": "Operating System Concepts",
            "Department": "Computer Science",
            "Semester": "Spring",
            "Year": 2021,
            "Is_Active": 1,
            "Department_Id": 1
        }        
    ]
}
```

# UI Implementation

## Running 

1. Clone repository.
2. Install [Node.js and npm](https://nodejs.org/en/) (v6.6.0 or newer) if they are not already installed on your computer.
`npm install`
3. ` npm start`
