#!/usr/bin/env python

import rospy
#import tf
from nav_msgs.msg import Odometry

nfiles = 1
output_dir = "./oxts/data/"

def callback(msg):

    global nfiles
    # Filename is 10 zeros, plus file # starting at 0
    fnumber = str(nfiles)
    fname = output_dir + fnumber.zfill(10) + ".txt"
    f = open(fname, "w")

    x =  msg.pose.pose.position.x
    y =  msg.pose.pose.position.y
    z =  msg.pose.pose.position.z
    # First is lat, lon, alt. Instead write x y z, since we have it directly
    # x y are in UTM; z height
    f.write("%f %f %f " %(x, y, z))

    # Orientation as quaternion
    q = msg.pose.pose.orientation
    #explicit_q = [q.x, q.y, q.z, q.w]

    #r, p, y = tf.transformations.euler_from_quaternion(explicit_q)
    f.write("%f %f %f %f " %(q.x, q.y, q.z, q.w))

    cov = msg.pose.covariance

    for c in cov:
        f.write("%f " %(c))

    f.close()

    nfiles = nfiles+1

    # Write timestamps to file
    fname = "./oxts/" + "timestamps.txt"
    f = open(fname, "a")
    f.write("2019-03-07 %f\n" %(msg.header.stamp.to_sec()))
    f.close()


def main():

	rospy.init_node('odom_listener', anonymous=True)

	rospy.Subscriber("/navsat/odom", Odometry, callback)

	print("Running subscriber node...")
	rospy.spin()



if __name__ == '__main__':
	main()
