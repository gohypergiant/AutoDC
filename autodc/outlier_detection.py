from collections import defaultdict
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

class OutlierDetection:
	"""
	This routine starts with image embeddings creation using ResNet50 ImageNet pre-trained weights (Img2Vec),
	then applys dimensionality reduction PCA and t-SNE,
	finally utilizes Isolation Forest to identify outlier candidates.
	"""

	def __init__(self, input_directory: str, output_directory: str, verbose: bool = True):
		self.input_directory = input_directory
		self.output_directory = output_directory
		self.image_classes = None
		self.all_image_paths_by_image_class = None
		self.image_paths_by_image_class = None
		self.image_vectors = None
		self.dim_reduced_img_vectors = None

		self.verbose = verbose

	def get_image_classes(self) -> list:
		"""
		:param input_path: input path of the target image directory
		:param output_path: output path to write the outlier candidates to the user-defiend output directory
		:return: list of image classes
		"""

		try:
			list_of_dir = [name for name in os.listdir(self.input_directory)
						   if os.path.isdir(os.path.join(self.input_directory, name))]
			self.image_classes = list_of_dir

			if os.path.exists(f"{self.output_directory}/output/outliers/"):
				shutil.rmtree(f"{self.output_directory}/output/outliers")
			return self.image_classes

		except Exception as e:
			logger.error(f'ERROR: OutlierDetection.get_image_classes({self.input_directory}, {self.output_directory}): \n\t{e}.')

	def vectorize_and_dim_reduce_images(self) -> dict:
		"""Vectorize images and perform dimensionality reduction using PCA and TSNE
		:return: scaled dimensionality-reduced image vectors (values) by image class (key) as a Python dict
		"""
		self.image_classes = self.get_image_classes()
		if self.verbose:
			print(" \n### AUTODC: Outlier Detection -- In Progress --------\n")

		self.all_image_paths_by_image_class = defaultdict(list)
		self.image_paths_by_image_class = defaultdict(list)
		tsne_scaled_results = dict()
		valid_images = [".jpg", ".png"] # only supports jpg and png
		for image_class in self.image_classes:
			if self.verbose:
				print(f"class: {image_class}")
			self.all_image_paths_by_image_class[image_class].extend(glob.glob(f"{self.input_directory}/{image_class}/*"))

			self.image_vectors = dict()
			for image_path in self.all_image_paths_by_image_class[image_class]:
				ext = os.path.splitext(image_path)[1]
				if ext.lower() in valid_images:
					self.image_vectors[image_path] = img2vec.get_vec(image_path)
					self.image_paths_by_image_class[image_class].append(image_path)

			X = np.stack(list(self.image_vectors.values()))

			pca_50 = PCA(n_components=50)
			pca_result_50 = pca_50.fit_transform(X)

			if self.verbose:
				print(f'Cumulative explained variation for 50 principal components: {np.sum(pca_50.explained_variance_ratio_)}')
				print(np.shape(pca_result_50))

			tsne = TSNE(n_components=2, verbose=1, n_iter=3000)
			tsne_result = tsne.fit_transform(pca_result_50)
			tsne_scaled = StandardScaler().fit_transform(tsne_result)
			tsne_scaled_results.setdefault(image_class, tsne_scaled)

		self.dim_reduced_img_vectors = tsne_scaled_results
		return self.dim_reduced_img_vectors

	def detect_img_outliers(self):
		"""
		Use Isolation Forest to identify outlier candidates and save outlier and non-outlier images to the user-defined output directory
		:return: True when the operation is successfull
		"""
		self.dim_reduced_img_vectors = self.vectorize_and_dim_reduce_images()
		for image_class, dim_red_img_vecs in self.dim_reduced_img_vectors.items():

			clf = IsolationForest(random_state=123)
			preds = clf.fit_predict(dim_red_img_vecs)

			images = list()
			image_paths_outlier = list()
			count = 0
			outlier_count = 0
			non_outlier_count = 0

			if not os.path.exists(f"{self.output_directory}/output/outliers/outlier_data/{image_class}"):
				os.makedirs(f"{self.output_directory}/output/outliers/outlier_data/{image_class}")
			if not os.path.exists(f"{self.output_directory}/output/outliers/non_outlier_data/{image_class}"):
				os.makedirs(f"{self.output_directory}/output/outliers/non_outlier_data/{image_class}")

			tsne_result_scaled_outlier = list()
			for image_path in self.image_paths_by_image_class[image_class]:
				if preds[count] == -1:
					image_paths_outlier.append(image_path)

					image = cv2.imread(image_path, 3)
					b,g,r = cv2.split(image)           # get b, g, r
					image = cv2.merge([r,g,b])         # switch it to r, g, b
					image = cv2.resize(image, (50,50))
					images.append(image)
					tsne_result_scaled_outlier.append(dim_red_img_vecs[count])
					outlier_count = outlier_count + 1

					img_name = os.path.split(image_path)[1]
					shutil.copy(image_path, f"{self.output_directory}/output/outliers/outlier_data/{image_class}/{img_name}")

				else:
					img_name = os.path.split(image_path)[1]
					shutil.copy(image_path, f"{self.output_directory}/output/outliers/non_outlier_data/{image_class}/{img_name}")
					non_outlier_count = non_outlier_count + 1
				count = count + 1

			if self.verbose:
				print(f"class: {image_class}")
				print(f"outlier_count: {outlier_count}")
				print(f"non_outlier_count: {non_outlier_count}")

		if self.verbose:
			print("\n### AUTODC: Outlier Detection -- Completed --------\n")

		return True


if __name__ == '__main__':
	None
