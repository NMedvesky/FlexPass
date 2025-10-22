# Project: PCHS FlexPass App

A system for managing students during flex times, and coordinating hall passes for students.

## Running The Project
### Run the database
Install `docker` [https://docs.docker.com/compose/install/]

Navigate the project directory in a terminal, and run:
```sh
docker compose up
```

### Run the website
Install `uv` [https://docs.astral.sh/uv/getting-started/installation/]

In new a terminal, while navigated to the project directory, run:
```sh
uv run manage.py runserver
```

Then in your browser navigate to the url provided from the program output.
