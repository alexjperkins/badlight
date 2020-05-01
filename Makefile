### --- Flask --- ###
lint:
	black ./badlight --diff

format:
	black ./badlight 

shell:
	docker-compose -f local.yml run --rm flask flask shell


### --- Testing --- ###
test:
	docker-compose -f local.yml run --rm -e BADLIGHT_ENVIRONMENT=testing flask pytest /tests/

update_test_snapshots:
	docker-compose -f local.yml run --rm -e BADLIGHT_ENVIRONMENT=testing flask pytest \
	       	--snapshot-update /tests/

debug_tests:
	docker-compose -f local.yml run --rm -e BADLIGHT_ENVIRONMENT=testing flask pytest -s /tests/

coverage:
	docker-compose -f local.yml run --rm -e BADLIGHT_ENVIRONMENT=testing flask pytest \
	       	--cov=badlight --cov-report term-missing /tests/


### --- Docker Compose --- ###
build_flask_local:
	docker-compose -f local.yml build flask

run_flask_local:
	docker-compose -f local.yml up flask

run_local:
	docker-compose -f local.yml up

build_and_run_local:
	docker-compose -f local.yml up --build


### --- Migrations --- ###
init_migrations:
	docker-compose -f local.yml run --rm flask flask db init

makemigrations:
	docker-compose -f local.yml run --rm flask flask db migrate 

migrate:
	docker-compose -f local.yml run --rm flask flask db upgrade


### --- PostgreSQL --- ###
psql:
	docker-compose -f local.yml up --build postgres
