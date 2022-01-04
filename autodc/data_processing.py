import outlier_detection
import edge_case_selection
import data_augmentation



input_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/sample_data/"
output_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/"
outlier_data_percent = 10
non_outlier_data_percent = 40
augmentation_data_percent = 20


outlier_detection.outlierDetection(input_path,output_path)

edge_case_selection.edgeCaseSelection(input_path,output_path, non_outlier_data_percent , outlier_data_percent)

# noise, crop, vflip, rotate, saturation, brightness, scale
data_augmentation.imageAugmentation(input_path,output_path, augmentation_data_percent, "noise")