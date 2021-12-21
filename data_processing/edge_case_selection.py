import os
import shutil, random, os
import logging
logger = logging.getLogger('ftpuploader')




def edgeCaseSelection(input_path,output_path, non_outlier_data_percent, outlier_data_percent,):

	try:

		outlier_dir = output_path+"output/outliers/outlier_data/"
		non_outlier_dir = output_path+"output/outliers/non_outlier_data/"

		list_of_dir_outlier = [ name for name in os.listdir(outlier_dir) if os.path.isdir(os.path.join(outlier_dir, name)) ]
		# list_of_dir_non_outlier = [ name for name in os.listdir(non_outlier_dir) if os.path.isdir(os.path.join(non_outlier_dir, name)) ]
		
		image_classes = list_of_dir_outlier

		for image_class in image_classes:

		    image_class_outlier_dir = outlier_dir+image_class
		    image_class_non_outlier_dir = non_outlier_dir+image_class

		    # onlyfiles = next(os.walk(image_class_outlier_dir))[2]
		    total_non_outlier_data = len(os.listdir(image_class_non_outlier_dir))
		    total_outlier_data = len(os.listdir(image_class_outlier_dir))
		    
		    total_non_outlier_data_to_select = int((int(non_outlier_data_percent)/100)*total_non_outlier_data)
		    total_outlier_data_to_select = int((int(outlier_data_percent)/100)*total_outlier_data)

		    print("class : ", image_class)
		    print("outlier data : ", total_outlier_data_to_select)
		    print("non_outlier data : ", total_non_outlier_data_to_select)

		    improved_output_dir = output_path+"output/improved_data/"+image_class

		    # Create dir for improve data if not exist
		    if not os.path.exists(improved_output_dir):
		    	os.makedirs(improved_output_dir)


		   	# Copy files from outlier folder to final data folder
		   	# Non outlier data specific to an image class eg. "cats"
		    dirpath_non_outlier = non_outlier_dir+image_class
		    filenames_ņon_outlier = random.sample(os.listdir(dirpath_non_outlier), total_non_outlier_data_to_select)
		    for fname in filenames_ņon_outlier:
		    	srcpath = os.path.join(dirpath_non_outlier, fname)
		    	shutil.copy(srcpath, improved_output_dir)

		   	# Outloer data 
		    dirpath_outlier = outlier_dir+image_class
		    filenames_outlier = random.sample(os.listdir(dirpath_outlier), total_outlier_data_to_select)
		    for fname in filenames_outlier:
		    	srcpath = os.path.join(dirpath_outlier, fname)
		    	shutil.copy(srcpath, improved_output_dir)

		return True
	except Exception as e:
		logger.error('Something went wrong: ' + str(e))

# edgeCaseSelection(input_path,output_path, 40 , 10)