import signal
import sys
import rospy
from std_msgs.msg import Float64, Float64MultiArray

def steering_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "received: %s", data.data)

def driving_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "received: %s", data.data)

def signal_handler(sig, frame):
    print("")
    print("bye bye!")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('circle_listener', anonymous=True)
    rospy.Subscriber("/newbot2/steering_controller/command", Float64, steering_callback)
    rospy.Subscriber("/newbot2/driving_controller_rear/command", Float64MultiArray, driving_callback)

    rospy.spin()

