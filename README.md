### Badlight Backend

This is the backend to the Badlight Personal Management tool, it is built upon the flask framework
with GraphQL APIs and PostgreSQL database - written in python 3.8 of course, linted using black:

```
	black: https://github.com/psf/black
```

The frontend to the backend is located at: `https://github.com/alexjperkins/badlight-frontend`


## Requirements

- Python 3.8 (https://www.python.org/downloads/)
- Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Docker (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Docker-Compose (https://docs.docker.com/compose/install/)

NOTE: This project was build using Arch Linux. Any Linux distribution should be fine
	as long as it's up to date with security patches & common libraries.
	Likewise with MacOS, however this isn't built with Windows in mind and you
	will likely find bugs.
	Its also recommended to use the package manager associated with your machine.
		eg. 
		Arch: pacman
		Debian (based): apt
		MacOS: brew
	This is just recommendation, and is left at the users discretion


Enjoy!


```
	$ python --version && git --version && docker -- version

```

## Project Setup
```
	$ git clone git@github.com:alexjperkins/badlight.git && \
	    cd ~/backlight &&
	    python -m venv venv &&
	    . ./venv/bin/activate &&
	    ./venv/bin/pip install -r ./requirements/development.txt
```

This is only a demonstration, it's probably easy to setup up via docker-compose
commands as this will give you a setup postgres instance for free

## Build Flask Only
```
	$ make build_flask_local

	or

	$ docker-compose -f local.yml build flask
```

## Run Flask Only
```
	$ make run_flask_local 

	or

	$ docker-compose -f local.yml up --build flask
```

## Run App
```
	$ make run_local

	or

	$ docker-compose -f local.yml up
```

## Run App and Build
```
	$ make run_and_build_local

	or

	$ docker-compose -f local.yml up --build
```

## Database Migration
For the first migration run the following command:
```
	$ make migrate

	or 

	$ docker-compose -f local.yml run --rm flask flask db upgrade
```	

After any code changes please run the following to create a new migration file
```
	$ make makemigration

	or

	$ docker-compose -f local.yml run --rm flask flask db migrate
```

Followed by the above comman to perfrom a migration (`make migrate`)

NOTE: This project has scripts to automatically bootstrap models.
The script iterates through the project and finds `models.py` files,
it will then import then into the application factory method `create_app`, in 
just before `flask_migrate.Migrate` is instantiated

Therefore, please if creating new models include a `__all__` as the top of the
`model.py` file, and be sure to include all models you would like to be registered:

```
# Example/models.py


__all__ = [
	"ModelA",
]


class ModelA:
	# pass
```

Furthermore, in the test `<project_root>/tests/config/test_bootstrap.py` : 
be sure to add the new model to the `expected_registered_models` fixture.

Final words on this, this is an experimental pattern and I'm unsure whether it's
going to stay, but the key rationale was to allow for the splitting of models over
multiple files, without the need to import them individually into the
application factory method

## Shell
To use a shell with the correct application context use:
```
	$ make shell

	or 

	$ docker-compose -f local.yml run --rm flask flask shell
```


## Tests
Since tests aren't copied over the local Dockerfile, located at `~/badlight/compose/local/flask/Dockerfile`
please setup a virtualenv as shown above and activate,
otherwise run the following commands to setup:
```
	$ . ./venv/bin/activate
```

The test runner for this project is `pytest`, run the tests as follows:
```
	$ make test
```

Another thing to note with this project is the use of `snapshot`:

```
	https://github.com/syrusakbary/snapshottest
```

## Test Snapshots
This is useful library to test against graphql endpoints. The first time a test is ran
it creates a `snapshot` and stores to the directory most local to where the test is located.
Repeating the test, will check the outpoint from the endpoint against this.
Therefore it's advisable to run the test at least twice.

Any changes to the endpoint definition will require the updating of the snapshots. This can be
done with the following command:

```
	make update_test_snapshots
```
Make sure ALL snapshots are committed to source control

## Debug Tests
Sometimes you would like to debug tests, with a debugger such as `ipdb`
This requires capturing the stdout from pytest. This is managed with the following command:
```
	make debug-tests
```

## Test Coverage
```
	$ make coverage
```

## Linting

The linter for this project is `black`
```
	$ make lint

	or 

	$ black ./badlight --diff
```

## Format 

```
	$ make format

	or

	$ black ./badlight
```
