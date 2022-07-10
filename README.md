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
 * [run.py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/run.py)
   is the entry point to the service
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

It's as simple as adding routers to the [routers](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/routers)
package, and registering them in [routers/\_\_init\_\_py](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/routers/__init__.py).
