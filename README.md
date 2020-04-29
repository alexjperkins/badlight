### Badlight Backend

This is the backend to the Badlight Personal Management tool, it is built upon the flask framework
with GraphQL APIs - written in python 3.8 of course.

The frontend to the backend is located at: `https://github.com/alexjperkins/badlight-frontend`



## Requirements

- Python 3.8
- Git
- Docker	

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

	or 

	$ PYTHONPATH=./badlight pytest ./tests/
```

## Test Coverage
```
	$ make coverage

	or 

	$ PYTHONPATH=./badlight pytest --cov=badlight --cov-report term-missing ./tests/
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
