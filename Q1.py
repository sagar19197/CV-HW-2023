# COMPUTER VISION - Winter 2023
# Assignment - 2
# Sagar Suman, 2019197

# Python file for Question 1:
# CAMERA CALIBRATION

#---------------------------------------------


# Importing Libraries 
import numpy as np;
# Open CV library
import cv2 as cv;

# Glob -
import glob;

# Defining Termination Condition for OpenCV-
termination_criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001);

# Defining ChessBoard
chessBoard_Size = (5,8);
# Defining FrameSize
frameSize = (1096, 1461)

# Creating 3D world object points
dim = (chessBoard_Size[0]*chessBoard_Size[1], 3);
world_objp = np.zeros(dim, np.float32);

# Creating world coordinnates - 
# Using MeshGrid
world_points = np.mgrid[0:chessBoard_Size[0],0:chessBoard_Size[1]];
# Taking Transpose for points
world_points = world_points.T;
# Reshaping 
world_points = world_points.reshape(-1,2);
# Finally Creating points like (0,0,0), (1,0,0), etc
world_objp[:,:2] = world_points;


# Creating Temp list for storing Object points and Image Points
real_3D_points = [];
# Image points 2d
image_points = [];

# Loading Images - 
checkerBoard_images = glob.glob("./CheckerBoardPhotos/*.jpg");

# Iterating Images - 
image_number = 1;
for checkerBoard_image in checkerBoard_images:

	image = cv.imread(checkerBoard_image);
	# Converting to GrayScale
	gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY);

	# Finding ChessBoard Corners 
	return_value, corners_value = cv.findChessboardCorners(gray_image, chessBoard_Size, cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE);

	# If return_value = True
	if return_value == True:

		real_3D_points.append(world_objp);
		# Refining Pixel coordinates
		corners_2 = cv.cornerSubPix(gray_image, corners_value, (11,11), (-1,-1), termination_criteria);
		# Appending Corners
		image_points.append(corners_value);

		# Displaying Corners 
		image = cv.drawChessboardCorners(image, chessBoard_Size, corners_2, return_value);
		cv.imwrite("CornersDetectionImage"+str(image_number)+".jpg",image);
		image_number = image_number + 1;
		image =cv.resize(image, (500, 600));
		cv.imshow("Corners of ChessBoard", image);
		cv.waitKey(1000);

cv.destroyAllWindows();


# Calibration

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(real_3D_points, image_points, frameSize, None, None);

print("camera matrix :",cameraMatrix);
print("distortion Parameters:",dist);
print("Rotation Vectos:",rvecs);
print("Translation Vectors",tvecs);