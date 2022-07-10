# FastAPI Project Template with a Database and Docker Compose

This is a template used by [create_app](https://github.com/application-creators/create_app) to create a 
new FastAPI project with a PostgreSQL database and Docker Compose.

To create your new project from this template, simply run:

```shell
pip install create_app
python -m create_app python_fastapi_with_database
```


## What's in this template

 * Project structure
 * A [FastAPI](https://fastapi.tiangolo.com/) API:
   * Configurable through environment variables and environment file
   * With CORS
   * And Base models for endpoints with pagination
 * Virtualenv
 * Unit tests
 * Docker Compose containerization
 * Pre-commit GIT hooks
   * [Black](https://github.com/psf/black)
   * [Isort](https://pycqa.github.io/isort/)
   * [Flake8](https://flake8.pycqa.org/en/latest/)
 * Makefile with useful commands


## Git hooks

This template uses [pre-commit](https://pre-commit.com/) to run GIT hooks in your repo:
 * [Black](https://github.com/psf/black)
 * [Isort](https://pycqa.github.io/isort/)
 * [Flake8](https://flake8.pycqa.org/en/latest/)

This helps developers to keep the same code styling in the project.

To install the hooks in your repo, first [install pre-commit](https://pre-commit.com/#install) in your system. Then run:
```shell
make install_git_hooks
```


## Project structure

The project structure has been designed keeping in mind that you start with an API and a database, but may also need to 
add other services to your project. 

By default, you get a [FastAPI service](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D), 
named the same as you project package name, and a [database service](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/database) 
(a PostgreSQL instance). You can add as many services you want to the
[docker-compose.yml](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/docker-compose.yml) file. If you need to build
a new service, create a new folder at the [root](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D) of the repo and
put all its files in there. This will keep your repo organized and all your services decoupled from each other.

Say you have a project named "my_project", and want to add a Redis service:

```
my_project/        (repo root)
│   ...
│
└───my_project/    (FastAPI service, included in this template)
│
└───database/      (PostgreSQL database, included in this template)
│
└───redis_cache/   (A new service you added)
│   │   ...
│   │   Dockerfile
│
│   docker-compose.yml
│   
│   ...
```

Each Python service (although you may have services using other technologies) has the following structure:

```
service_a/    (service folder)
│
└───service_a/    (contains sources)
│   │
│   └───tests/
│   │
│   │run.py
│
│   Dockerfile
│   Makefile
│   requirements.frozen
│   requirements.test.frozen
```

 * The [Dockerfile](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/Dockerfile)
provides instructions to build the image
 * [Makefile](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/Makefile)
   is not required, but it's useful to keep some everyday commands in there
 * Declare your dependencies in 
   [requirements.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.frozen)
   and 
   [requirements.test.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.test.frozen)
   (refer to [requirements](#requirements))
 * _run.py_ (or _main.py_) is the entry point to the service
 * Put the unit tests in the [tests](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/tests) 
   package (refer to [unit tests](#unit-tests))


## Docker compose

To build the images, go into the project repo and run:
```shell
docker compose build
```

And to run the containers:
```shell
docker compose up
```


### Take a look at your running API

After starting the container, you can hit the API root with any browser or HTTP client. For example, with CURL:
```shell
curl localhost:{api_port}
```

Check the API docs! http://localhost:{api_port}/docs

And the alternative API docs! http://localhost:{api_port}/redoc


## Virtualenv

It is recommended to keep your system's Python interpreter clean, and install your project's dependencies in a virtual 
environment (_venv_). Doing this has advantages like preventing dependencies conflicts between different projects
you may have in your system.

### Create the virtualenv

After you've installed [venv](https://docs.python.org/3/library/venv.html) in your system, go to the 
[service folder](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D)
and run the following to create the venv:

```shell
make create_virtualenv
```

### Requirements

Use the [requirements.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.frozen) 
file to declare the project's dependencies, and [requirements.test.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.test.frozen) 
to declare dependencies that are only required to run tests. As indicated in the filenames, it is advised to declare 
the dependencies with explicit versions (example: _requests==2.28.1_). This will allow you to control when to upgrade
dependencies versions, and will save you headaches when a new dependency version is released right when you were 
running a deployment pipeline.

To install the requirements in the venv, go to the [service folder](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D) 
and run:
```shell
make install_requirements
```

To install the test requirements in the venv, run:
```shell
make install_test_requirements
```

To install requirements and test requirements with a single, command, run:
```shell
make install_all_requirements
```


## Unit tests

Add your unit tests to the 
[tests package](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/tests).

To run all unit tests, go to the [service folder](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D) 
and run:
```shell
make run_unit_tests
```


## Build your API

Say we want to add a few endpoints to manage a TODO list, which we'll store in a table in our database.


#### Adding database models

One way to create the new table in the DB is to declare our ORM model first, and from there generate a DB migration
to get that table created in the database. Let's choose this path, as it's the simplest and most practical.

Add the SQLAlchemy model in 
[database/models.py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/database/models.py).
This is the mapping for our new "todo" table.


```python
from sqlalchemy import Column, Integer, Text
from database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)

    name = Column(Text)
```


#### Adding database migrations

Now is time to generate the database migrations from the model we've just added. With the services running, do the 
following:

```shell
cd {project_package_name}
make generate_database_migration MESSAGE="Add 'todo' table"
```

This will create a new file in 
[alembic/versions](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/alembic/versions),
named *{migration_id}_add_todo_table.py*. That's the Alembic migration to create the "todo" table.


#### Applying migrations to the database

Simply run the following to upgrade the database to it's latest version. In our case, it runs the migration we've just 
generated to create the "todo" table:
```shell
cd {project_package_name}
make migrate_database
```


#### Adding serialization models

We'll create a couple of models so that we can serialize our data, and document its structure so that
people can check our docs and know what to expect when they use our endpoints.

Add a _todo_models.py_ in the 
[serialization](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/serialization)
package, with a couple of models:

```python
from typing import List
from pydantic import BaseModel
from serialization.base_models import BasePaginatedList


class TodoModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TodoCreateOrEdit(BaseModel):
    name: str


class TodoPaginatedList(BasePaginatedList):
    results: List[TodoModel]
```


#### Add a new router

It's probably convenient to make our URI paths configurable in our API. You could just hardcode them, but say we want 
to be able to change them in our settings file 
([settings.env](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/settings.env)), 
with absolutely no impact in our code. Then on 
([settings.py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/settings.py)) 
we'll add two new settings. One for the URI path (_todos_route_), and another to give the route a human-readable name for the API documentation 
(_todos_tag_). These are default values, meaning that if you change them in _settings.env_, the values in that file will be used instead.

```python
from pydantic import BaseSettings


class Settings(BaseSettings):
    ...
    todos_route: str = "/todos"
    todos_tag: str = "Todos"
    ...
```

Then we'll add a new _todos.py_ module in 
[routers](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/routers), 
and add our new router with configurable path and tag:

```python
from fastapi import APIRouter
from settings import settings


router = APIRouter(prefix=settings.todos_route, tags=[settings.todos_tag])
```

And then all that's left is register our router in the API, which is done by adding it to a list in 
[routers/\_\_init\_\_.py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/routers/__init__.py):

```python
from typing import List
from fastapi import APIRouter
from .todos import router as todos_router


# Add your APIRouters to this list
ALL_ROUTERS: List[APIRouter] = [todos_router]
```


#### Adding endpoints

Before adding endpoints, you'll need to [add a new router](#add-a-new-router) first.

Let's add a few endpoints to the router, in _routers/todos.py_.


##### List

This endpoint returns a paginated list of TODOs.

```python
from fastapi import Depends
from settings import settings, ROOT_ROUTE
from database import Session, session_scope
from database.models import Todo
from serialization.model_serialization import paginate_list
from serialization.todo_models import TodoPaginatedList


@router.get(ROOT_ROUTE, response_model=TodoPaginatedList)
def list_todos(
    limit: int = settings.default_limit,
    offset: int = settings.default_offset,
    session: Session = Depends(session_scope),
):
    return paginate_list(session, Todo, offset, limit)
```


##### Create

This endpoint is to create a new TODO.

```python
from fastapi import Depends, status
from settings import ROOT_ROUTE
from database import Session, session_scope
from database.models import Todo
from serialization.todo_models import TodoModel, TodoCreateOrEdit


@router.post(
    ROOT_ROUTE, response_model=TodoModel, status_code=status.HTTP_201_CREATED
)
def create_todo(
    todo: TodoCreateOrEdit, session: Session = Depends(session_scope)
):
    todo_orm = Todo(**todo.dict())
    session.add(todo_orm)
    session.flush()

    return todo_orm
```


##### Get

This endpoint is to get an existing TODO. Returns 404 (Not found) if it does not exist.

```python
from fastapi import Depends
from settings import IDENTIFIER_ROUTE
from database import Session, session_scope
from database.models import Todo
from serialization.model_serialization import get_or_raise
from serialization.models import TodoModel


@router.get(IDENTIFIER_ROUTE, response_model=TodoModel)
def read_todo(identifier: int, session: Session = Depends(session_scope)):
    return get_or_raise(session, Todo, id=identifier)
```


##### Update

This endpoint is to update an existing TODO. Returns 404 (Not found) if it does not exist.

```python
from fastapi import Depends
from settings import IDENTIFIER_ROUTE
from database import Session, session_scope
from database.models import Todo
from serialization.model_serialization import get_or_raise
from serialization.models import TodoModel, TodoCreateOrEdit


@router.put(IDENTIFIER_ROUTE, response_model=TodoModel)
def update_todo(
    identifier: int,
    todo: TodoCreateOrEdit,
    session: Session = Depends(session_scope),
):
    instance = get_or_raise(session, Todo, id=identifier)

    instance.name = todo.name

    session.add(instance)

    return instance
```


##### Delete

This endpoint is to delete an existing TODO. Returns 404 (Not found) if it does not exist.

```python
from fastapi import Depends, status, Response
from settings import IDENTIFIER_ROUTE
from database import Session, session_scope
from database.models import Todo
from serialization.model_serialization import get_or_raise


@router.delete(IDENTIFIER_ROUTE, status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(identifier: int, session: Session = Depends(session_scope)):
    instance = get_or_raise(session, Todo, id=identifier)
    session.delete(instance)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
```


### Configuring the API service

You can add as many settings you need to 
[settings.py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/settings.py).

When adding settings, you can specify default values. 

You can change the value of these settings in 
[settings.env](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/settings.env). 
If, for a setting, you set a value in this file, it overwrites the default one (if any).
