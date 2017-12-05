

FROM valian/docker-python-opencv-ffmpeg:py3


# source: https://github.com/ContinuumIO/docker-images/blob/master/miniconda/Dockerfile
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.27-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

# Set up project requirements
COPY environment.yml /usr/src/app/
RUN conda env create -f /usr/src/app/environment.yml
RUN /bin/bash -c "source activate object-detection"

# Set up project
COPY object_detection_app.py /usr/src/app/object_detection_app.py
COPY utils/ /usr/src/app/utils
##RUN ls -la /usr/src/app/utils/*
COPY object_detection/ /usr/src/app/object_detection
##RUN ls -la /usr/src/app/object_detection/*

EXPOSE 5000


CMD ["python", "/usr/src/app/object_detection_app.py", "--source=rtsp://52.39.224.108:1935/live/myStream"]