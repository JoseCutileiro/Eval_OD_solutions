import cv2
import numpy as np
import random
import os

# List your images (adjust the file paths as needed)
image_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
# Corresponding labels
labels = ["8 person", "4 car", "5 car", "1 person", "3 person, 1 car"]

# Repeat each image 20 times
repeated_images = image_paths * 200
repeated_labels = labels * 200

# Zip images and labels together, shuffle them, and then unzip
paired = list(zip(repeated_images, repeated_labels))
random.shuffle(paired)
shuffled_images, shuffled_labels = zip(*paired)

# Initialize video settings
frame_width = 640  # Set to the width of your images
frame_height = 480  # Set to the height of your images
fps = 30  # Frames per second (you can adjust)
output_video_path = "out.mp4"

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Open the text file to write labels
with open("vid.txt", "w") as label_file:
    # Read and write the images to the video
    for img_path, label in zip(shuffled_images, shuffled_labels):
        img = cv2.imread("imgs/" + img_path)
        img_resized = cv2.resize(img, (frame_width, frame_height))  # Resize if necessary
        out.write(img_resized)
        
        # Write the corresponding label to the file
        label_file.write(f"{label}\n")

# Release the VideoWriter object
out.release()

print("Video creation complete!")
print("Labels written to 'vid.txt'.")
