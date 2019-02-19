FROM cyborgdalien/opencv:latest

RUN apt-get update && apt-get install -y \
	python3 \
	python3-dev \
	python3-pip &&\
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN git clone https://github.com/thtrieu/darkflow.git

WORKDIR darkflow

RUN pip3 install cython tensorflow-gpu==1.8.0
RUN pip3 install -e .

RUN wget https://pjreddie.com/media/files/yolo.weights

ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0","--allow-root"]
