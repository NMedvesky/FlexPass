# Project: PCHS FlexPass App

A system for managing students during flex times, and coordinating hall passes for students.

## Running The Project
### Run the database
Install `docker` [https://docs.docker.com/compose/install/]

Navigate to the project directory in a terminal, and run:
```sh
docker compose up
```

### Run the website
Install `uv` [https://docs.astral.sh/uv/getting-started/installation/]

In new a terminal, while navigated to the project directory, run:
```sh
uv run manage.py tailwind dev
```

Then in your browser navigate to the url provided from the program output.

### Database Migrations
If there are database changes you may need to migrate your local database. To do so make sure the database is running and then run the following command in the project directory:
```sh
uv run manage.py migrate
```
