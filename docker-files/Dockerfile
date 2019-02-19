FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 CUDA_ROOT="/usr/local/cuda/bin"

#ENV TZ=Brazil/East
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update --fix-missing && \
    apt-get install -y \
	build-essential \
	unzip \ 
        checkinstall \
        libreadline-gplv2-dev \
        libncursesw5-dev \
        libssl-dev \
        libsqlite3-dev \
        tk-dev \
        libgdbm-dev \
        libc6-dev \
        libbz2-dev \
        openssl \
        libffi-dev \
        zlib1g-dev \
	python3 \
	python3-pip \
        python3-dev \
        python3-setuptools  \
        wget \
        cmake \
        git \
        gcc \
        gfortran \
        libgtk2.0-dev \
        pkg-config \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libatlas-base-dev \
        libblas-dev \
        liblapack3 \
        liblapack-dev \
        libopenblas-base \
        libopenblas-dev \
        liblapacke-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libdc1394-22-dev \
	libcanberra-gtk-module \
	libcanberra-gtk3-module \
	libopencv-dev \
	vim \ 
        && \
   apt-get clean && \
   apt-get autoremove && \
   rm -rf /var/lib/apt/lists/* 	

RUN pip3 install numpy pillow matplotlib jupyterlab

WORKDIR /usr/src
RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git

#RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.0.zip
#RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip
#RUN unzip opencv.zip &&\
#	unzip opencv_contrib.zip

#RUN mv opencv-3.4.0 opencv
#RUN mv opencv_contrib-3.4.0 opencv_contrib

RUN mkdir /usr/src/opencv/build

WORKDIR /usr/src/opencv/build

RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=/usr/src/opencv_contrib/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python3 \
    -D WITH_CUDA=ON \
    -D BUILD_EXAMPLES=OFF ..

RUN make -j12 &&\
        make install &&\
        ldconfig

RUN mkdir /base

WORKDIR /base

RUN rm -rf /usr/src/opencv /usr/src/opencv_contrib

ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0","--allow-root"]
