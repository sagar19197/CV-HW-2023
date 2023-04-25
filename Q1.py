# Computer Vision 2023
# Assignment-3
# Sagar Suman, 2019197

# Python File for Q1 : Point Cloud Registration

# Importing Dependencies 
import open3d;
import numpy as np;

# Name of objects in Dataset-
objectNamesList = ["bag", "basketball", "chair"];


# Iterating over 3 objects 
for object_name in objectNamesList:
	

	# Part 1 : Visualization of Source and Target point cloud

	
	# Generating point cloud directory - 
	point_cloud_directory = "PointCloudRegistration/" + object_name;

	# Reading Source point cloud
	source_point_cloud = open3d.io.read_point_cloud(point_cloud_directory+"/source.ply");
	# Reading Target Point cloud
	target_point_cloud = open3d.io.read_point_cloud(point_cloud_directory+"/target.ply");

	# Visualizing
	# For Source- 
	open3d.visualization.draw_geometries([source_point_cloud], window_name=object_name+": Source Point Cloud", width = 800, height = 650);

	# For target - 
	open3d.visualization.draw_geometries([target_point_cloud], window_name=object_name+": Target Point Cloud", width = 800, height = 650);

	print("------------------------------------------");
	print("For",object_name+" :");
	print("For source.ply :", source_point_cloud);
	print("For target.ply:",target_point_cloud);

	print("-------------------------------------------");






