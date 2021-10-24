from teleop import *

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node("circle_talker", anonymous=True)
    rospy.loginfo("Initializing circle_talker")
    steering_pub = SteeringTalker()
    driving_pub = DrivingTalker()
    while not rospy.is_shutdown():
        driving_pub.update_value([10, 10])
        driving_pub.send_msg()
        steering_pub.update_value(-0.4)
        steering_pub.send_msg()
        time.sleep(0.5)
