FROM ros:melodic-ros-base as ros-python3

# install python 3
RUN apt-get -y update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get -y update && \
    apt-get install -y ros-melodic-roslint && \
    apt-get install -y python3.7 && \
    rm -rf /var/lib/apt/lists/

SHELL ["/bin/bash", "-c"]

# create catkin workspace
RUN mkdir -p /catkin_ws/src && \
    cd /catkin_ws/ && \
    source /opt/ros/melodic/setup.bash && \
    catkin_make

RUN source /catkin_ws/devel/setup.bash && \
    cd /catkin_ws/src && \
    git clone https://github.com/locusrobotics/catkin_virtualenv.git && \
    git clone https://github.com/locusrobotics/aiorospy.git && \
    cd /catkin_ws/src/aiorospy/aiorospy && \
    cd /catkin_ws/ && \
    catkin_make

RUN touch .bashrc && echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
