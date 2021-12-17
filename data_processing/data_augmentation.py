# # pip install Pillow if you don't already have it

# # import image utilities
# from PIL import Image

# # import os utilities
# import os

# # imagePath = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/Roman_numbers_dataset/data/outlier_data_augment/train/ix/"
# # imagePath = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/outlier_data_augment/training/dogs/"
# imagePath = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/snails_dataset/outlier_data_augment/training_set/Melanoides/"

# # define a function that rotates images in the current directory
# # given the rotation in degrees as a parameter
# def rotateImages(rotationAmt):
#   # for each image in the current directory
# #   for image in os.listdir(os.getcwd()):
#   for image in os.listdir(imagePath):  
#     print("image path : ", image)
#     # open the image
#     img = Image.open(imagePath+image)
#     # rotate and save the image with the same filename
#     img.rotate(rotationAmt).save(imagePath+"aug_"+image)
#     # close the image
#     img.close()
    
# # examples of use
# rotateImages(180)





import cv2 as cv
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#instantiate the ImageDataGenerator class
datagen = ImageDataGenerator(
        rotation_range=40,
        height_shift_range=0.2,
        width_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
#loop over the data in batches and this automatically saves the images



input_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/sample_data/"
output_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/"

outlier_dir = output_path+"output/outliers/outlier_data"
aug_outlier_dir = output_path+"output/aug"

i = 0
for batch in datagen.flow_from_directory('outlier_dir', batch_size=6,target_size=(256,256),
                          save_to_dir='path_to_output_folder', save_format='jpg'):
    i += 1
    if i > 5:
        break