# todo_application

Learning Path

Each section ends with a variation of an exercise that involves building a Todo application. You can start a Github repo and use git to express the evolution of the exercises.

Back-end - Initiate the project

1- Install vitual environment
    -> python3 -m pip install --user virtualenv

2- Create virtual environment
    -> python3 -m venv env

3- Activate virtual environment
 -> source env/bin/activate
    Desactivate virtual environment:
    -> deactivate

4- Install packages
    -> python3 -m pip install requests

5- Install FastAPI
    -> pip install fastapi

6- Install server Uvicorn
    -> pip install uvicorn

7- Launch server
    -> uvicorn main:app --reload
    -> Stop server: Ctrl-C

8- Open browser & you will see the JSON response
    http://127.0.0.1:8000/

9- Test the routes of the app:
    http://127.0.0.1:8000/docs
