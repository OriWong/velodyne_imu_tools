#!/usr/bin/env python

import rospy
import sensor_msgs
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2

nfiles = 0
output_dir = "./velodyne_points/data/"

def callback(msg):
    
    global nfiles
    # Filename is 10 zeros, plus file # starting at 0
    fnumber = str(nfiles)
    fname = output_dir + fnumber.zfill(10) + ".txt"
    f = open(fname, "w")

    # Write every point (xyz coordinates) in the message to a file
    for point in pc2.read_points(msg, skip_nans=True):
        pt_x = point[0]
        pt_y = point[1]
        pt_z = point[2]
        f.write("%f %f %f 0\n" %(pt_x, pt_y, pt_z))
    f.close()

    nfiles = nfiles+1
    
    # Write timestamps to file
    fname = "./velodyne_points/" + "timestamps.txt"
    f = open(fname, "a")
    f.write("2019-03-07 %f\n" %(msg.header.stamp.to_sec()))
    f.close()


def main():
	
	rospy.init_node('listener', anonymous=True)
   
	rospy.Subscriber("/velodyne_points", sensor_msgs.msg.PointCloud2, callback)
	print "Running subscriber node..."
	rospy.spin()



if __name__ == '__main__':
	main()