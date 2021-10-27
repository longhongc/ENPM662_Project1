# CAD Modelling & Simulation using Gazebo 
This project is to use SolidWorks to model a simple steerable car and control it in gazebo simulator. 

The CAD model is exported into urdf files by using the sw_urdf tool. The urdf files is parsible by gazebo. After adding the transmission properties and controller configurations for the interface of ros-controller. The robot can be simulated in gazebo and be controlled through several joints and velocity commands.  

<img src="https://user-images.githubusercontent.com/28807825/138623072-489baee1-1031-4a70-8476-721563c88c61.png" width="500" height="350" />  
<img src="https://user-images.githubusercontent.com/28807825/138623135-522eeb27-d8a6-4c4d-8f6f-006cc12867a8.png" width="500" height="350" />  

## Directory Structure
```
├── config (controllers setting)
├── launch 
├── meshes 
├── rviz (rviz setting)
├── scripts (executable python scripts)
├── textures
├── urdf 
└── worlds
```
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
source devel/setup.bash
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
