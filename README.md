# helm_bookstore_api

This is a user-friendly API using Django Rest Framework (DRF) for a bookstore management system. The main idea is to offer a bunch of useful functions for handling book information effortlessly. Users can do everything from adding, viewing, and updating, to removing book details. Plus, it also offers a neat feature where users can neatly organize their booklists by creating categories.

## API Endpoints Available

| Http Verb    | ApiEndpoint              | Usage                        |
| :---         |     :---                 |          ---:                |
| POST         | /api/books/              | Add a new book               |
| GET          | /api/books/              | Get all available books      |
| GET          | /api/books/:id/          | Get a book and see details   |
| PUT          | /api/books/:id/          | Update a book                |
| DELETE       | /api/books/:id/          | Delete a book                |
| GET          | /api/categories/         | Get all available categories |
| GET          | /api/categoriess/:id/    | Get a category               |

## setup:

This application is containerized with Docker and has two services setup and configured to run on the same network for extra security.

Follow the following setup instructions to run this on your local environment:

<h4>Requirements:</h4>

- Docker/Docker Desktop <br />
- Python 3.12.0 <br />
- Django 4.2.6 <br />
- Django Rest Framework 3.14.0 <br />
- Postgresql 13.12
- Pip <br />


<h4>Setup Steps:</h4>

1. **Clone the project on your machine:** <br />
`git clone https://github.com/ClaytonSiby/helm_bookstore_api.git`

2. **Change directory to this project's root:** <br />
`cd helm_bookstore_api`

3. **To run the application on your local:**

- Run `pip install virtualenv` to install virtualenv an essential tool for creating a virtual environment for the project.
- Run `virtualenv .venv` to create the virtual environment (the name can be anything)
- Run `source ./.venv/bin/activate` to activate the environment (this ensures that all dependencies installed are only changed on your current environment, e.t.c)
- Run `pip install -r requirements.txt` to install all dependencies essential for this project <br />
- make sure the helm_bookstore/settings.py db configuration looks like this (the `localhost` is your db host) e.g:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'helm_admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Run `chmod +x ./build.sh && ./build.sh` to `makemigrations`, `migrate`, and start a gunicorn server on `http://0.0.0.0:8000`  <br />
- Run `python manage.py test` to run all available tests for the project

3. **To run in a container:**
- Setup docker stack: > this will setup two services (`api`, `db`, and `nginx`) on the same network (i.e helm_network): <br />
- `docker-compose build --no-cache` > install dependencies as descriped in the Dockerfile  </br>
- make sure the helm_bookstore/settings.py db configuration looks like this (the `db` is your host):
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'helm_admin',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```
- `docker-compose up` > **which does the following**:
- creates a `helm_bookstore_project` docker stack and establishes the `helm_network`
- creates a `helm_bookstore_api` container (the djangon/rest framework project)
- creates a `helm_bookstore_db` container (postgresql database container)
- creates a `nginx` container
- runs `./build.sh` to `makemigrations`, `migrate`, and bind a gunicorn server on `http://0.0.0.0:8000` <br />

<h4>Usage:</h4>

- Access available resources on the API via the above endpoints (provided in the table)
- **NB** - if you get a 404 No Content View, make sure you are using the right endpoint and try again!
