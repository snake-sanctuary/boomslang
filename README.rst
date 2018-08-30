    Boomslang Repository
=========================

A conda/pypi repository with an enhanced permission system tailored for large organisations.

:License: MIT

Features
---------

Coming soon


Getting started
----------------

* Boomslang has been developed for Python 3.7 with PostgreSQL as a database, other configurations are not officially supported.

The first step is to activate the virtual environment with pipenv::

    $ cd /path/to/boomslang/root/folder
    $ pipenv shell

Create a config.yaml in the root directory (use config-template for guidance), these will be loaded by the settings.
You can then run::

    $ python manage.py makemigrations
    $ python manage.py migrate

* To create a **superuser account**, use this command::

    $ python manage.py createsuperuser

The admin panel is accessible at http://localhost:8000/admin after you start the developement server. To do so::

    $ python manage.py runserver --settings=config.settings.settings_local



Testing
---------

Unit-tests rely on pytest, to run them::
    $ pytest --ds=boomslang.settings.settings_test

To check the coverage and generate an HTML coverage report::

    $ coverage run manage.py test --settings=config.settings.test
    $ coverage html

Then open htmlcov/index.html
