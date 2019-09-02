FROM ros:melodic-ros-base as ros-python3


# workaround to be able to use python 3
RUN apt-get update && apt-get install -q -y \
    python3.7 python3-pip \
    && rm -rf /var/lib/apt/lists/

RUN python3.7 -m pip install -U \
    pip

RUN python3.7 -m pip install -U \
    numpy pyyaml rosdep rosinstall_generator wstool rosinstall rospkg catkin-pkg

RUN touch .bashrc && echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
