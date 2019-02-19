#!/bin/bash
xhost +local:docker
docker run -ti --rm        -e DISPLAY=$DISPLAY        -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/Documents/opencv/:/tmp cv2py

