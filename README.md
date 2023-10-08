# helm_bookstore_api

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
>> A terminal <br />
>> A code Editor (optional) <br />

<h4>Setup Steps:</h4>

1. Clone the project on your machine: <br />
`git clone https://github.com/ClaytonSiby/helm_bookstore_api.git`

2. Change directory to this project's root: <br />
`cd helm_bookstore_api`

3. Setup docker stack: > this will setup two services (`api` and `db`) on the same network: <br />
`docker-compose build --no-cache` > this installs all your dependencies with compatible versions for the environment. </br>
`docker-compose up` > this spins up the docker stack & start a local server on 0.0.0.0/api/books

4. Test some endpoints on your local machine: <br />
`0.0.0.0/api/books/`: > some of the API endpoints you can test are all on the table above.
