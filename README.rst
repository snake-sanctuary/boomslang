    Liripype
==================

A conda/pypi repository with enhanced permissions.

:License: MIT


Getting started
----------------

* I use Python 3.6 compiled from source. The first step is to create a virtual environment preferable outside of the project::

    $ cd ~/your-path/virtual/
    $ python -m venv name_of_virtual
    $ source name_of_virtual/bin/activate

* Then, cd to the root folder of the project. Note that I've set the database to sqlite in local and test. This is strongly discouraged when using PostgreSQL in production (as it should be) but that way you don't need to set up a PostgreSQL server::

    $ cd path/to/project
    $ pip install -r requirements/local.txt
    $ pip install -r requirements/test.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py test --settings=config.settings.test

* To create a **superuser account**, use this command::

    $ python manage.py createsuperuser

The admin panel is accessible at http://localhost:8000/admin after you start the developement server. To do so::

    $ python manage.py runserver --settings=config.settings.local



Testing
---------

The system has been unittested quite thoroughly, using factory_boy as a fixture replacement

To run the tests::
    $ python manage.py test --settings=config.settings.test


To check the coverage and generate an HTML coverage report::

    $ coverage run manage.py test --settings=config.settings.test
    $ coverage html

Then open htmlcov/index.html
