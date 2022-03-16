#USEAGE: python starter_image_data.py --input Users/sample_data/ --output Users/sample_data/

import autodc.outlier_detection as od
import autodc.edge_case_selection as ecs
import autodc.data_augmentation as da
import argparse

# construct te argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help='input image directory')
ap.add_argument("-o", "--output", required=True, help='output image directory')
ap.add_argument("-r", "--o_ratio", required=False, default=100, help='outlier data ratio')
ap.add_argument("-n", "--n_ratio", required=False, default=100, help='non outlier data ratio')
ap.add_argument("-a", "--a_ratio", required=False, default=20, help='augmented data ratio')
ap.add_argument("-t", "--aug_fn", required=False, default='noise', help='augmentation techqniue')

args = vars(ap.parse_args())

# Specify required inputs
input_path = str(args["input"])
output_path = str(args["output"])
outlier_data_ratio = args["o_ratio"]
non_outlier_data_ratio = args["n_ratio"]
augmented_data_ratio = args["a_ratio"]

# Outlier detection
od_process = od.OutlierDetection
od_process.image_data(input_path, output_path)

# Edge case selection
ecs_process = ecs.EdgeCaseSelection
ecs_process.image_data(input_path, output_path, non_outlier_data_ratio, outlier_data_ratio)

# Image augmentation
# option: noise, crop, vflip, rotate, saturation, brightness, scale
da_process = da.DataAugmentation
da_process.image_data(input_path, output_path, augmented_data_ratio, str(args["aug_fn"]))
