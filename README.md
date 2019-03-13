# velodyne_imu_tools

Short scripts to pull data from the Velodyne LIDAR ROS driver publishing on the topic /velodyne_points, and an GPS/IMU unit publishing on the topic /navsat/odom. For each point cloud, it extracts the 3D position of each point and writes them to a file. For each message from the IMU/GPS, it extracts the position, orientation, and covariance matrix and writes it to a file. This assumes the directories ./oxts/,  /.oxts/data, ./velodyne_points,  and ./velodyne_points/data exist.
