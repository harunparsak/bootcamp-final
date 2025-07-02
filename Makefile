up:
	docker-compose up -d
down:
	docker-compose down
build:
	docker-compose up --build -d
logs:
	docker-compose logs -f
restart:
	docker-comğpse down && docker-compose up -d
ps:
	docker-compose ps
