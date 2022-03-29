import logging
import os
import random
import shutil

logger = logging.getLogger('ftpuploader')

class EdgeCaseSelection:
	def __init__(self, input_path: str, output_path: str,
				 non_outlier_data_percent: int, outlier_data_percent: int,
				 verbose: bool = True):
		"""
		:param input_path: file directory where images are located
		:param output_path: file directory to write images
		:param non_outlier_data_percent: the percent of non-outlier data that will be included in the output/improved dataset
		:param outlier_data_percent: the percent of identified outlier data that will be included in the output/improved dataset
		"""
		self.input_path = input_path
		self.output_path = output_path
		self.non_outlier_data_percent = non_outlier_data_percent
		self.outlier_data_percent = outlier_data_percent
		self.verbose = verbose

		self.image_classes = None
		self.outlier_dir = None
		self.non_outlier_dir = None

	def get_image_classes(self):
		"""Get image classes to use
        	:return: list of image classes
        	"""
		self.outlier_dir = f"{self.output_path}/output/outliers/outlier_data/"
		self.non_outlier_dir = f"{self.output_path}/output/outliers/non_outlier_data/"
		list_of_dir_outlier = [name for name in os.listdir(self.outlier_dir)
							   if os.path.isdir(os.path.join(self.outlier_dir, name))]

		# Remove existing data
		if os.path.exists(f"{self.output_path}/output/improved_data/"):
			shutil.rmtree(f"{self.output_path}/output/improved_data")

		if self.verbose:
			print("\n### AUTODC: Edge Case Selection -- In Progress --------\n")

		self.image_classes = list_of_dir_outlier
		return self.image_classes

	def select_img_edge_cases(self):
		"""
        	Selecting edge case to be included in the output/improved dataset from the outlier candidates,
			based on user-defined data percent
        	:return: True if the process is successful
        	"""
		self.image_classes= self.get_image_classes()
		for image_class in self.image_classes:
			image_class_outlier_dir = f"{self.outlier_dir}{image_class}"
			image_class_non_outlier_dir = f"{self.non_outlier_dir}{image_class}"

			total_non_outlier_data = len(os.listdir(image_class_non_outlier_dir))
			total_outlier_data = len(os.listdir(image_class_outlier_dir))

			total_non_outlier_data_to_select = int((int(self.non_outlier_data_percent) / 100) * total_non_outlier_data)
			total_outlier_data_to_select = int((int(self.outlier_data_percent) / 100) * total_outlier_data)

			if self.verbose:
				print(f"class: {image_class}")
				print(f"outlier data: {total_outlier_data_to_select}")
				print(f"non_outlier data: {total_non_outlier_data_to_select}")

			improved_output_dir = f"{self.output_path}/output/improved_data/{image_class}"

			# Create dir for improve data if not exist
			if not os.path.exists(improved_output_dir):
				os.makedirs(improved_output_dir)

			# Copy files from outlier folder to final data folder
			# Non outlier data specific to an image class eg. "cats"
			dirpath_non_outlier = f"{self.non_outlier_dir}{image_class}"
			filenames_non_outlier = random.sample(os.listdir(dirpath_non_outlier), total_non_outlier_data_to_select)
			for fname in filenames_non_outlier:
				srcpath = os.path.join(dirpath_non_outlier, fname)
				shutil.copy(srcpath, improved_output_dir)

			# Outlier data
			dirpath_outlier = f"{self.outlier_dir}{image_class}"
			filenames_outlier = random.sample(os.listdir(dirpath_outlier), total_outlier_data_to_select)
			for fname in filenames_outlier:
				srcpath = os.path.join(dirpath_outlier, fname)
				shutil.copy(srcpath, improved_output_dir)

		if self.verbose:
			print("\n### AUTODC: Edge Case Selection -- Completed --------\n")

		return True


if __name__ == "__main__":
	None
