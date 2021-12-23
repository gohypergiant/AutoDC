import os
import shutil, random, os
import logging
logger = logging.getLogger('ftpuploader')
import augly.image as imaugs



def imageAugmentation(input_path,output_path, aug_data_percent, aug_technique):

    try:

        outlier_dir = output_path+"output/outliers/outlier_data/"

        list_of_dir_outlier = [ name for name in os.listdir(outlier_dir) if os.path.isdir(os.path.join(outlier_dir, name)) ]
        # list_of_dir_non_outlier = [ name for name in os.listdir(non_outlier_dir) if os.path.isdir(os.path.join(non_outlier_dir, name)) ]
        
        image_classes = list_of_dir_outlier

        for image_class in image_classes:

            image_class_outlier_dir = outlier_dir+image_class

            total_outlier_data = len(os.listdir(image_class_outlier_dir))
            
            total_outlier_data_to_select = int((int(aug_data_percent)/100)*total_outlier_data)

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
            for fname in filenames_outlier:

                if(aug_technique == "noise"):
                    aug_image = imaugs.random_noise(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "crop"):
                    aug_image = imaugs.crop(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "vflip"):
                    aug_image = imaugs.vflip(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "rotate"):
                    aug_image = imaugs.rotate(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "saturation"):
                    aug_image = imaugs.saturation(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "brightness"):
                    aug_image = imaugs.brightness(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                elif(aug_technique == "scale"):
                    aug_image = imaugs.scale(outlier_dir+image_class+"/"+fname, output_path=output_path+"output/improved_data/"+image_class+"/aug_"+fname)
                else:
                    logger.error('Something went wrong: Invalid Augmentation Technique')
                    return False

        return True
    except Exception as e:
        logger.error('Something went wrong: ' + str(e))






