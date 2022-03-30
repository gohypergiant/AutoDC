import logging
import random
import os

import augly.image as imaugs
from PIL import Image

logger = logging.getLogger('ftpuploader')

class DataAugmentation:
    def __init__(self, input_path: str, output_path: str,
                 aug_data_percent: float, aug_technique: str,
                 verbose: bool = True):
        """
        :param input_path: input file directory where images are located
        :param output_path: output file directory location to write outlier image data
        :param aug_data_percent: the number of percent of total train data to be augmented and added to output/improved dataset
        :param aug_technique: user-specified augmentation technique
        """
        self.input_path = input_path
        self.output_path = output_path
        self.aug_data_percent = aug_data_percent
        self.aug_technique = aug_technique
        self.verbose = verbose

        self.outlier_dir = None
        self.image_classes = None

    def get_image_classes(self):
        """Get image classes to use
        :return: list of image classes
        """
        self.outlier_dir = f"{self.output_path}/output/outliers/outlier_data/"
        list_of_dir_outlier = [name for name in os.listdir(self.outlier_dir)
                               if os.path.isdir(os.path.join(self.outlier_dir, name))]
        if self.verbose:
            print("### AUTODC: Data Augmentation -- In Progress --------\n")

        self.image_classes = list_of_dir_outlier
        return self.image_classes

    @staticmethod
    def image_aug_technique(aug_technique: str, outlier_path: str, output_path: str) -> Image:
        """Augments image located in outlier_path based on specified aug_technique, and writes to the specified output path
        :param aug_technique: augmentation technique as a string
        :param outlier_path: outlier image filepath
        :param output_path: image filepath to write augmented image to
        :return: an augmented PIL Image
        """
        aug_functions = dict(
        noise=imaugs.random_noise(outlier_path, output_path),
        crop=imaugs.crop(outlier_path, output_path),
        vflip=imaugs.vflip(outlier_path, output_path),
        rotate=imaugs.rotate(outlier_path, output_path),
        saturation=imaugs.saturation(outlier_path, output_path),
        brightness=imaugs.brightness(outlier_path, output_path),
        scale=imaugs.scale(outlier_path, output_path)
        )

        if aug_technique.lower() not in aug_functions:
            raise ValueError(f'Invalid Augmentation Technique: {list(aug_functions.keys())}')
        return aug_functions.get(aug_technique)

    def augment_img_data(self) -> bool:
        """
        Augmenting image data from the user-defined augmentation technique and augmented data percent
        :return: True if the process is successful
        """
        self.image_classes = self.get_image_classes()
        for image_class in self.image_classes:
            image_class_outlier_dir = f"{self.outlier_dir}{image_class}"
            total_outlier_data = len(os.listdir(image_class_outlier_dir))

            total_outlier_data_to_select = int((int(self.aug_data_percent) / 100) * total_outlier_data)

            if self.verbose:
                print(f"class: {image_class}")
                print(f"outlier data: {total_outlier_data_to_select}")

            improved_output_dir = f"{self.output_path}/output/improved_data/{image_class}"
            # Create dir for improve data if not exist
            if not os.path.exists(improved_output_dir):
                os.makedirs(improved_output_dir)

            # Copy files from outlier folder to final data folder
            # Non outlier data specific to an image class eg. "cats"

            # Outlier data
            dirpath_outlier = f"{self.outlier_dir}{image_class}"
            filenames_outlier = random.sample(os.listdir(dirpath_outlier), total_outlier_data_to_select)
            output_path_string = f"{self.output_path}/output/improved_data/{image_class}/aug_"
            for fname in filenames_outlier:
                aug_img = DataAugmentation.image_aug_technique(str(self.aug_technique),
                                                     f"{dirpath_outlier}/{fname}",
                                                     f"{output_path_string}{fname}")
                aug_img.save(f"{output_path_string}{fname}")

        if self.verbose:
            print("\n### AUTODC: Data Augmentation -- Completed --------\n")

        return True


if __name__ == "__main__":
    None
