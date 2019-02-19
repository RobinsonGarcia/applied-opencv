#!/bin/bash
xhost +
docker run -ti --rm --runtime=nvidia \
	--net=host --ipc=host \
	--volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
	-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
	-v /home/robinson/Documents/opencv:/base \
	-p 8888:8888 \
	--rm \
	cyborgdalien/opencv:latest

#--entrypoint "/bin/bash" \

