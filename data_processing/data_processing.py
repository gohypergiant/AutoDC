import outlier_detection
import edge_case_selection



input_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/sample_data/gygygs"
output_path = "/Users/akashnair/Desktop/Akash/Project/Hypergiant/Data_Labeling/dogs-vs-cats/vgvhbhb"
outlier_data_percent = 10
non_outlier_data_percent = 40


outlier_detection.outlierDetection(input_path,output_path)

edge_case_selection.edgeCaseSelection(input_path,output_path, non_outlier_data_percent , outlier_data_percent)