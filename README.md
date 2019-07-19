# Project Title

Rest-API for work with parsed apartment advertises.

## Getting started

1. `python3.6 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements/local.txt --user`
4. `./manage.py migrate` OR `make migrate`
5. `./manage.py createsuperuser` OR `make superuser`
6. `./manage.py runserver` OR `make server`

## Change default database

1) `touch .env`
2) Add to .env file `DATABASE_URL=postgres://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}`

## Running the tests
`pytest`

### Note
Currently database consists of advertises with invalid titles... 
Probably in 3-4 hours I'll  replace current database with advertises which have valid titles because of a bug. ria
.com provides only 1000 free requests per hour so it takes some time.

Also I waisted a lot of time for writing grabber as dom.ria swagger was not working. As API parsing is more 
predictable and more cleaner I decided to rewrite it to work with API. So I get useful params for parsing from XHR 
requests on dom.ria.com
