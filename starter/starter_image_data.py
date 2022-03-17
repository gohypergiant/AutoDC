#USEAGE: python starter_image_data.py --input Users/sample_data/ --output Users/sample_data/

import autodc.outlier_detection as od
import autodc.edge_case_selection as ecs
import autodc.data_augmentation as da
import argparse

# construct te argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help='input image directory')
ap.add_argument("-o", "--output", required=True, help='output image directory')
ap.add_argument("-r", "--o_percent", required=False, default=100, help='outlier data percent')
ap.add_argument("-n", "--n_percent", required=False, default=100, help='non outlier data percent')
ap.add_argument("-a", "--a_percent", required=False, default=25, help='augmented data percent')
ap.add_argument("-t", "--aug_fn", required=False, default='vflip', help='augmentation techqniue')

args = vars(ap.parse_args())

# Specify required inputs
input_path = str(args["input"])
output_path = str(args["output"])
outlier_data_percent = args["o_percent"]
non_outlier_data_percent = args["n_percent"]
augmented_data_percent = args["a_percent"]

# Outlier detection
od_process = od.OutlierDetection(input_path, output_path)
od_process.detect_img_outliers()

# Edge case selection
ecs_process = ecs.EdgeCaseSelection(input_path, output_path, non_outlier_data_percent, outlier_data_percent)
ecs_process.select_img_edge_cases()

# Image augmentation
# option: noise, crop, vflip, rotate, saturation, brightness, scale
da_process = da.DataAugmentation(input_path, output_path, augmented_data_percent, str(args["aug_fn"]))
da_process.augment_img_data()
