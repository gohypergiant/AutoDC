import logging
import random
import os

import augly.image as imaugs


logger = logging.getLogger('ftpuploader')


class DataAugmentation:
    def __init__(self, input_path, output_path, aug_data_ratio, aug_technique):
        self.input_path, = input_path
        self.output_path = output_path
        self.aug_data_ratio = aug_data_ratio
        self.aug_technique = aug_technique

    def image_data(
        input_path: str,
        output_path: str,
        aug_data_ratio: int,
        aug_technique: str
        ):

        def image_aug_technique(
            aug_technique,
            outlier_path_string,
            output_path_string
            ):

            aug_functions = dict(
                noise=imaugs.random_noise(outlier_path_string, output_path_string),
                crop=imaugs.crop(outlier_path_string, output_path_string),
                vflip=imaugs.vflip(outlier_path_string, output_path_string),
                rotate=imaugs.rotate(outlier_path_string, output_path_string),
                saturation=imaugs.saturation(outlier_path_string, output_path_string),
                brightness=imaugs.brightness(outlier_path_string, output_path_string),
                scale=imaugs.scale(outlier_path_string, output_path_string)
            )

            if aug_technique.lower() not in aug_functions:
                raise ValueError(f'Invalid Augmentation Technique: {list(aug_functions.keys())}')

            return aug_functions.get(aug_technique)

        try:

            outlier_dir = output_path+"output/outliers/outlier_data/"
            list_of_dir_outlier = [ name for name in os.listdir(outlier_dir) if os.path.isdir(os.path.join(outlier_dir, name)) ]
            # list_of_dir_non_outlier = [ name for name in os.listdir(non_outlier_dir) if os.path.isdir(os.path.join(non_outlier_dir, name)) ]

            print(" ")
            print("### AUTODC: Data Augmentation -- In Progress --------")
            print(" ")

            image_classes = list_of_dir_outlier

            for image_class in image_classes:

                image_class_outlier_dir = outlier_dir+image_class

                total_outlier_data = len(os.listdir(image_class_outlier_dir))

                total_outlier_data_to_select = int((int(aug_data_ratio)/100)*total_outlier_data)

                # print("class : ", image_class)
                # print("outlier data : ", total_outlier_data_to_select)

                improved_output_dir = output_path+"output/improved_data/"+image_class

                # Create dir for improve data if not exist
                if not os.path.exists(improved_output_dir):
                    os.makedirs(improved_output_dir)

                # Copy files from outlier folder to final data folder
                # Non outlier data specific to an image class eg. "cats"

                # Outlier data
                dirpath_outlier = outlier_dir+image_class
                filenames_outlier = random.sample(os.listdir(dirpath_outlier), total_outlier_data_to_select)
                outlier_path_string = outlier_dir+image_class+"/"
                output_path_string =output_path+"output/improved_data/"+image_class+"/aug_"
                for fname in filenames_outlier:
                    print(fname)
                    image_aug_technique(aug_technique, outlier_path_string+fname, output_path_string+fname)

            print(" ")
            print("### AUTODC: Data Augmentation -- Completed --------")
            print(" ")

            return True

        except Exception as e:
            logger.error('Something went wrong: ' + str(e))#, exc_info=sys.exc_info())
