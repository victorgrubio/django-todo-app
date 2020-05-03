# Django Task Manager API
Todo backend API with project management capabilities to help SCRUM/Kanban methodologies.
With this API you could develop your own frontend, or you may use the one develop for the complete app (IN PROGRSS).

## Installation

### Docker (ON PROGRESS)
Pull the docker image
```bash
docker pull victorgrubio/django-todo-app
```
Create and run a new container with the 8000 port mapped to access it from your network.
```
docker run -p "8000:8000" --name django-todo-container django-todo-app
```

### Source code
Clone this repo
```bash
git clone https://github.com/victorgrubio/django-todo-app.git
```
Create a virtual environment (or not, as you wish). Use the virtualenv tool you prefer. Here is an example with venv.

```bash
cd django-todo-app
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

After that, just execute the  ```rebuild_project.sh``` script.

```bash
cd todoAPI
./rebuild_project.sh
```

This simple script contains the following commands, for you to know.
```bash
python3 manage.py collectstatic # To get all static (html, css, js) to access the API
python3 manage.py makemigrations # To import the db models
python3 manage.py migrate # To actually migrate to the db
python3 manage.py runserver # To create the server
```

## Quickstart 

The server is deployed at http://localhost:8000. 

To check the API Documentation please go to http://localhost:8000/swagger to obtain the [Swagger](https://swagger.io/) documentation or to http://localhost:8000/redoc to have it in [ReDoc](https://github.com/Redocly/redoc) style. 

The JSON/YAML files for the documentation are available at http://localhost:8000/swagger.json or http://localhost:8000/swagger.yaml

Administration page is available at http://localhost:8000/admin.
