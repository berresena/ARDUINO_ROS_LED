#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def led_control_publisher():
    rospy.init_node('led_control_publisher', anonymous=True)
    pub = rospy.Publisher('led_control', String, queue_size=10)

    rate = rospy.Rate(1) # 1 Hz
    while not rospy.is_shutdown():
        # LED'i yak
        pub.publish("true")
        rospy.loginfo("LED Control: true")
        rate.sleep()

        # 5 saniye bekle
        rospy.sleep(5)

        # LED'i kapat
        pub.publish("false")
        rospy.loginfo("LED Control: false")
        rate.sleep()

if __name__ == '__main__':
    try:
        led_control_publisher()
    except rospy.ROSInterruptException:
        pass
