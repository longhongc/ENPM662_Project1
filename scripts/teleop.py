##
# @file teleop.py
# @Brief Control the bot with wasdx key  
# @author Chang-Hong Chen
# @email longhongc@gmail.com
# @version 1.0.0
# @date 2021-10-23

import time
import signal
import sys
import getch
import rospy
from std_msgs.msg import Float64, Float64MultiArray

class steering_talker:

    def __init__(self):
        self.pub = rospy.Publisher("/newbot2/steering_controller/command", Float64, queue_size=10)
        self.rate = rospy.Rate(10)
        self.steering_angle = 0
    def send_msg(self, key):
        # Left
        if(key=='A' or key=='a'):
            self.steering_angle += 0.2
        # Right
        elif(key=='D' or key=='d'):
            self.steering_angle -= 0.2
        # Reset
        elif(key=='S' or key=='s'):
            self.steering_angle = 0.0
        self.pub.publish(self.steering_angle)

class driving_talker:

    def __init__(self):
        self.pub = rospy.Publisher("/newbot2/driving_controller_rear/command", Float64MultiArray, queue_size=10)
        self.rate = rospy.Rate(10)
        self.left_vel = 0
        self.right_vel = 0
        self.wheels_velocity = [self.left_vel, self.right_vel]
    def send_msg(self, key):
        msg = Float64MultiArray()
        # Forward
        if(key=='W' or key=='w'):
            self.left_vel += 0.1
            self.right_vel += 0.1
        # Backward
        elif(key=='X' or key=='x'):
            self.left_vel -= 0.1
            self.right_vel -= 0.1
        # Stop
        elif(key=='S' or key=='s'):
            self.left_vel = 0.0
            self.right_vel = 0.0
        self.wheels_velocity = [self.left_vel, self.right_vel] 
        msg.data = self.wheels_velocity
        self.pub.publish(msg)
        
def parse_input(input_key, steering_pub, driving_pub):
    steering_keys=['A', 'a', 'D', 'd', 'S', 's']
    driving_keys=['W', 'w', 'X', 'x', 'S', 's']

    if(input_key in steering_keys):
        steering_pub.send_msg(input_key)

    if(input_key in driving_keys):
        driving_pub.send_msg(input_key)

def signal_handler(sig, frame):
    print("")
    print("bye bye!")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node("teleop_talker", anonymous=True)
    steering_pub = steering_talker()
    driving_pub = driving_talker()
    while not rospy.is_shutdown():
        # get user key input with enter
        val = getch.getch() 
        parse_input(val, steering_pub, driving_pub)
        time.sleep(0.1)


