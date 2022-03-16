import glob
import logging
import os
import shutil

import cv2
from img2vec_keras import Img2Vec
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest


logger = logging.getLogger('ftpuploader')
img2vec = Img2Vec()

# @ ZAC -- insert a one-liner describing what the class does
class OutlierDetection:
	"""<ONELINER>"""

	def __init__(self, verbose: bool = False):
		self.input_directory = None
		self.output_directory = None
		self.image_classes = None
		self.verbose = verbose

	# @ ZAC -- complete the doc string below
	def get_image_classes(self, input_image_directory: str, output_directory: str) -> list:
		"""
		:param input_path: input path of the ____
		:param output_path: output path to write the ___ to
		:return: list of image classes
		"""
		self.input_directory = input_image_directory.rstrip('/')
		self.output_directory = output_directory.rstrip('/')

		try:
			list_of_dir = [name for name in os.listdir(self.input_directory)
						   if os.path.isdir(os.path.join(self.input_directory, name))]
			self.image_classes = list_of_dir

			if os.path.exists(f"{self.output_directory}/output/outliers/"):
				shutil.rmtree(f"{self.output_directory}/output/outliers/")
			return self.image_classes

		except Exception as e:
			logger.error(f'ERROR: OutlierDetection.get_image_classes({self.input_directory}, {self.output_directory}): \n\t{e}.')

	def vectorize_images(self) -> dict:
		"""Vectorize images and perform dimensionality reduction using PCA and TSNE
		:return: scaled dimensionality-reduced image vectors (values) by image class (key) as a Python dict
		"""
		if self.verbose:
			print(" \n### AUTODC: Outlier Detection -- In Progress --------'\n")

		tsne_scaled_results = dict()
		for image_class in self.image_classes:
			image_paths = list()
			image_paths.extend(glob.glob(f"{self.input_directory}/{image_class}/*.jpg"))

			image_vectors = dict()
			for image_path in image_paths:
				image_vectors[image_path] = img2vec.get_vec(image_path)
			X = np.stack(list(image_vectors.values()))

			pca_50 = PCA(n_components=50)
			pca_result_50 = pca_50.fit_transform(X)
			if self.verbose:
				print('Cumulative explained variation for 50 principal components: {}'.format(np.sum(pca_50.explained_variance_ratio_)))
				print(np.shape(pca_result_50))
			tsne = TSNE(n_components=2, verbose=1, n_iter=3000)
			tsne_result = tsne.fit_transform(pca_result_50)
			tsne_scaled = StandardScaler().fit_transform(tsne_result)
			tsne_scaled_results.setdefault(image_class, tsne_scaled)
			return tsne_scaled_results

	def detect_outliers(self):
		"""
		:return: 
		""""""
		For 
		    	
				clf = IsolationForest(random_state=123)
				preds = clf.fit_predict(tsne_result_scaled)

				images = []
				image_paths_outlier = []
				count = 0
				outlier_count = 0
				non_outlier_count = 0

				if not os.path.exists(output_path+"output/outliers/outlier_data/"+image_class):
					os.makedirs(output_path+"output/outliers/outlier_data/"+image_class)

				if not os.path.exists(output_path+"output/outliers/non_outlier_data/"+image_class):
					os.makedirs(output_path+"output/outliers/non_outlier_data/"+image_class)

				tsne_result_scaled_outlier = []
				for image_path in image_paths:
					if preds[count] == -1:
						image_paths_outlier.append(image_path)

						image = cv2.imread(image_path, 3)
						b,g,r = cv2.split(image)           # get b, g, r
						image = cv2.merge([r,g,b])         # switch it to r, g, b
						image = cv2.resize(image, (50,50))
						images.append(image)
						tsne_result_scaled_outlier.append(tsne_result_scaled[count])
						outlier_count = outlier_count + 1

						imgName =  os.path.split(image_path)[1]
						shutil.copy(image_path, output_path+"output/outliers/outlier_data/"+image_class+"/"+imgName)
					else:
						imgName =  os.path.split(image_path)[1]
						shutil.copy(image_path, output_path+"output/outliers/non_outlier_data/"+image_class+"/"+imgName)
						non_outlier_count = non_outlier_count+1
						count = count + 1

				if self.verbose:
					print("outlier_count : ",outlier_count)
					print("non_outlier_count : ",non_outlier_count)
					print("\n### AUTODC: Outlier Detection -- Completed --------\n")

			return True

		except Exception as e:
			logger.error('Something went wrong: ' + str(e))
