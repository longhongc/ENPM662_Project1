# CAD Modelling & Simulation using Gazebo 

## Environment
Ubuntu 18.04  
ROS Melodic

## Dependencies
Clone the ROS Package and Gazebo Plugin at src folder in the ROS workspace
```
cd catkin_ws/src
```
### ROS Package
ros-control  
ros-controller
```
sudo apt-get install ros-melodic-ros-control ros-melodic-ros-controllers
```
joint_state_publisher (for rviz only)
```
git clone https://github.com/ros/joint_state_publisher.git
```
### Gazebo Plugin
roboticsgroup_upatras_gazebo_plugins
```
git clone https://github.com/roboticsgroup/roboticsgroup_upatras_gazebo_plugins.git
```
### Python Libraray
```
pip3 install getch
pip3 install rospkg
```
## Build
```
cd catkin_ws
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```
## Launch Simulation
### Gazebo+RVIZ
```
roslaunch newbot2 gazebo_rviz.launch
```
### Gazebo
```
roslaunch newbot2 gazebo.launch
```
### RVIZ
```
roslaunch newbot2 display.launch
```
## Run Scripts
cd to scripts folder
```
roscd newbot2/scripts
```
### Teleop
Use keys to control the robot.  
w is for forwarding, x is backward, a turns left, d turns right, s stop and reset  
```
  w  
a s d  
  x
```
```
python3 teleop.py
```
### Publisher and Subscriber
Command the robot to drive in a circle and receive the command from the topic. 
```
python3 talker.py
```
```
python3 listener.py
```

### License
BSD
