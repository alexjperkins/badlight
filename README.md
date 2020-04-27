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

## Run Test

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
