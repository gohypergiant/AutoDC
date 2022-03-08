import outlier_detection
import edge_case_selection
import data_augmentation

# Specify required inputs
input_path = "/Users/zacliu/Documents/HG/AutoDC/sample_data/dog_vs_cat/"
output_path = "/Users/zacliu/Documents/HG/AutoDC/sample_data/dog_vs_cat/"
outlier_data_ratio = 10
non_outlier_data_ratio = 40
augmented_data_ratio = 20

# Outlier detection
outlier_detection.OutlierDetection(input_path, output_path)

# Edge case selection
edge_case_selection.EdgeCaseSelection(input_path, output_path, non_outlier_data_ratio, outlier_data_ratio)

# Image augmentation
# option: noise, crop, vflip, rotate, saturation, brightness, scale
data_augmentation.ImageAugmentation(input_path, output_path, augmented_data_ratio, "noise")