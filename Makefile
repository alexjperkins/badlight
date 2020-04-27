### --- Flask --- ###
test:
	PYTHONPATH=./badlight pytest ./tests/

coverage:
	PYTHONPATH=./badlight pytest --cov=badlight --cov-report term-missing ./tests/

lint:
	black ./badlight --diff

format:
	black ./badlight 


### --- Docker Compose --- ###
build_flask_local:
	docker-compose -f local.yml build flask

run_flask_local:
	docker-compose -f local.yml up flask

run_local:
	docker-compose -f local.yml up

run_and_build_local:
	docker-compose -f local.yml up --build
