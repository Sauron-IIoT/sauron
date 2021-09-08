config:
	aws configure

install:
	pipenv install

run:
	docker-compose up --remove-orphans --build

stop:
	docker-compose down

clean:
	docker-compose down -v
	rm -rf captures/*.jpg
	touch captures/.gitkeep