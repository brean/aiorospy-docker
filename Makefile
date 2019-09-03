export DOCKERHUB_ACCOUNT=brean

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	terminator -g terminator.conf -l aiorospy &

build:
	docker build -t ros-python3 ros-python3/

publish:
	make build
	# you might want to login using "docker login" first
	docker image tag ros-python3:latest $(DOCKERHUB_ACCOUNT)/ros-python3:latest
	docker image push $(DOCKERHUB_ACCOUNT)/ros-python3
