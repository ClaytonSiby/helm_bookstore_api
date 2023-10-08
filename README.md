# helm_bookstore_api

## API Endpoints Available

| Http Verb    | ApiEndpoint          | Usage                        |
| :---         |     :---             |          ---:                |
| POST         | /books/add_book/     | Add a new book               |
| GET          | /books/              | Get all available books      |
| GET          | /books/:id/          | Get a book and see details   |
| PUT          | /books/:id/update/   | Update a book                |
| DELETE       | /books/:id/delete/   | Delete a book                |
| GET          | /categories/         | Get all available categories |
| GET          | /categoriess/:id/    | Get a category               |
| GET          | /admin/              | Admin Panel                  |

## setup:

This application is containerized with Docker and has two services setup and configured to run on the same network for extra security.

Follow the following setup instructions to run this on your local environment:

<h4>Requirements:</h4>

>> Docker/Docker Deskstop <br />
>> Python 3.12.0 <br />
>> Django 4.2.6 <br />
>> Django Rest Framework 3.14.0 <br />


<h4>Setup Steps:</h4>

1. Clone the project on your machine: <br />
`git clone https://github.com/ClaytonSiby/helm_bookstore_api.git`

2. Change directory to this project's root: <br />
`cd helm_bookstore_api`

- **To run the application on your local:**
> Makes sure you have `Postgresql 13.11` installed <br />
> Run `pip install -r requirements.txt` to install all dependencies essential for this project <br />
> Run `chmod +x ./build.sh && ./build.sh` to `makemigrations`, `migrate`, and run `test` <br />
> Run `python manage.py runserver` to run a local python server <br />

- **To run in a container:**
3. Setup docker stack: > this will setup two services (`api` and `db`) on the same network: <br />
>> `docker-compose build --no-cache` > install dependencies as descriped in the Dockerfile  </br>
>> `docker-compose up` > this spins up the docker stack, runs `./build.sh` to `makemigrations`, `migrate`, and `test` the project <br />
>> `docker-compose exec api python manage.py runserver` > to spin up a local server from the api container <br />
>> `docker-compose exec api python manage.py makemigration` > makemigrations seperately <br />
>> `docker-compose exec api python manage.py test` > run all tests separately <br />
>> `docker-compose exec api python manage.py migrate` > migrate the database <br />

<h4>Usage:</h4>

- Access available resources on the API via the above endpoints (provided in the table)
