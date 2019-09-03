ARG ROS_DISTRO

FROM ros:${ROS_DISTRO}-ros-base as ros-python3


# workaround to be able to use python 3
RUN apt-get update && apt-get install -q -y \
    python3.7 python3-pip git \
    python3-virtualenv \
    ros-${ROS_DISTRO}-roslint \
    && rm -rf /var/lib/apt/lists/

RUN mkdir /catkin_ws
RUN git clone https://github.com/locusrobotics/catkin_virtualenv.git /catkin_ws/catkin_virtualenv

RUN python3.7 -m pip install -U catkin-pkg catkin_tools

SHELL [ "/bin/bash", "-c" ]
RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    && cd /catkin_ws/catkin_virtualenv/catkin_virtualenv \
    && python3.7 -m pip install .  --upgrade \
    && cmake CMakeLists.txt \
    && make
