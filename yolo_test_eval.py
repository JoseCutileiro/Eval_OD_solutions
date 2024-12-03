import os

# Path to the directory containing YOLO output files
yolo_output_dir = 'res'

# Path to the ground truth file
ground_truth_file_path = 'vid.txt'

# Read the ground truth file
with open(ground_truth_file_path, 'r') as ground_truth_file:
    ground_truth_lines = ground_truth_file.readlines()

# List all files in the /res directory (assuming they are YOLO output files)
yolo_output_files = [f for f in os.listdir(yolo_output_dir) if f.endswith('.txt')]

# Ensure there are YOLO output files in the directory
if not yolo_output_files:
    raise ValueError(f"No YOLO output files found in the directory: {yolo_output_dir}")

# Iterate over each YOLO output file in the /res directory
for yolo_file in yolo_output_files:
    yolo_output_file_path = os.path.join(yolo_output_dir, yolo_file)
    
    # Read the YOLO output file
    with open(yolo_output_file_path, 'r') as yolo_output_file:
        yolo_output_lines = yolo_output_file.readlines()

    # Ensure both files have the same number of lines
    if len(ground_truth_lines) != len(yolo_output_lines):
        print(f"Warning: The number of lines in {ground_truth_file_path} and {yolo_file} do not match.")
        continue  # Skip this file if the line count doesn't match
    
    # Initialize a counter for correct lines
    correct_count = 0

    # Compare lines
    for gt_line, yolo_line in zip(ground_truth_lines, yolo_output_lines):
        # Normalize both lines: sort items and strip whitespace
        gt_normalized = ', '.join(sorted(gt_line.strip().split(', ')))
        yolo_normalized = ', '.join(sorted(yolo_line.strip().split(', ')))

        # Compare normalized lines
        if gt_normalized == yolo_normalized:
            correct_count += 1

    # Print the result for this YOLO output file
    print(f"Results for {yolo_file}:")
    print(f"Number of correct lines: {correct_count}\n")
