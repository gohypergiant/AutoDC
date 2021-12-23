from img2vec_keras import Img2Vec
from IPython.display import Image
import glob
import os,shutil

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import cv2
import logging
logger = logging.getLogger('ftpuploader')
import edge_case_selection


img2vec = Img2Vec()



def outlierDetection(input_path,output_path):

	try:

		list_of_dir = [ name for name in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, name)) ]
		image_classes = list_of_dir

		if os.path.exists(output_path+"output/outliers/"):
		    	shutil.rmtree(output_path+"output/outliers")

		for image_class in image_classes:
		    image_paths = []
		    image_paths.extend(glob.glob(input_path + image_class + '/*.jpg'))

		    image_vectors = {}
		    for image_path in image_paths:
		        vector = img2vec.get_vec(image_path)
		        image_vectors[image_path] = vector

		    X = np.stack(list(image_vectors.values()))

		    pca_50 = PCA(n_components=50)
		    pca_result_50 = pca_50.fit_transform(X)
		    print('Cumulative explained variation for 50 principal components: {}'.format(np.sum(pca_50.explained_variance_ratio_)))
		    print(np.shape(pca_result_50))
		    
		    tsne = TSNE(n_components=2, verbose=1, n_iter=3000)
		    tsne_result = tsne.fit_transform(pca_result_50)

		    tsne_result_scaled = StandardScaler().fit_transform(tsne_result)
		    # plt.scatter(tsne_result_scaled[:,0], tsne_result_scaled[:,1])

		    # images = []
		    # for image_path in image_paths:
		    #     image = cv2.imread(image_path, 3)
		    #     b,g,r = cv2.split(image)           # get b, g, r
		    #     image = cv2.merge([r,g,b])         # switch it to r, g, b
		    #     image = cv2.resize(image, (50,50))
		    #     images.append(image)    


		    # fig, ax = plt.subplots(figsize=(20,15))
		    # artists = []

		    # for xy, i in zip(tsne_result_scaled, images):
		    #     x0, y0 = xy
		    #     img = OffsetImage(i, zoom=.7)
		    #     ab = AnnotationBbox(img, (x0, y0), xycoords='data', frameon=False)
		    #     artists.append(ax.add_artist(ab))
		    # ax.update_datalim(tsne_result_scaled)
		    # ax.autoscale(enable=True, axis='both', tight=True)
		    # plt.show()



		    # Outlier detection
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
		        
		    # print("outlier_count : ",outlier_count)
		    # print("non_outlier_count : ",non_outlier_count)

		return True
	except Exception as e:
		logger.error('Something went wrong: ' + str(e))
	    


