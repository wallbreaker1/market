network:
	docker network create market-network

postgres:
	docker run --name postgres14 --network market-network -p 5432:5432 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -d postgres:14-alpine

connectdb:
	docker exec -it postgres14 psql -U admin -d market

.PHONY: network postgres connectdb