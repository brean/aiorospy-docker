include .env
export


up:
	docker-compose up -d

down:
	docker-compose down

logs:
	terminator -g terminator.conf -l aiorospy &

build:
	docker build -t ros-python3 \
		--build-arg ROS_DISTRO=$(ROS_DISTRO) \
		ros-python3/

publish:
	make build
	# you might want to login using "docker login" first
	docker image tag $(TAG_NAME) $(DOCKERHUB_ACCOUNT)/$(TAG_NAME)
	docker image push $(DOCKERHUB_ACCOUNT)/ros-python3
