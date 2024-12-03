import cv2
from ultralytics import YOLO
import time
import logging, sys 

# AVOID PRINTING YOLO OUTPUT
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.getLogger("ultralytics").setLevel(logging.WARNING)


def eval_round(roundName,model,vid):

    # Open the video file
    cap = cv2.VideoCapture(vid)

    # Check if video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()


    # Variable to store the total count of detected objects
    total_objects_detected = 0
    frame_count = 0

    # Record the start time
    start_time = time.time()

    # Process each frame
    while True:
        ret, frame = cap.read()
        
        if not ret:  # If no frame is returned, video has ended
            break
        
        # Perform object detection using YOLO
        results = model(frame)
        
        # The detections are returned in the boxes attribute
        boxes = results[0].boxes  # Accessing the first result in the batch (usually only one frame at a time)
        
        # Get the list of detected objects (bounding boxes, class labels, and confidences)
        #detections = boxes.xywh  # Get the box coordinates in [x_center, y_center, width, height]
        confidences = boxes.conf  # Confidence scores of the detections
        #class_ids = boxes.cls  # Class IDs of the detected objects
        
        # Count the number of objects detected (filter by confidence threshold)
        num_objects = sum(conf.item() > 0.5 for conf in confidences)
        total_objects_detected += num_objects
        frame_count += 1


    # Record the end time
    end_time = time.time()

    # Calculate the runtime
    runtime_seconds = end_time - start_time

    # Print the total number of detected objects and runtime
    print(f"==== {roundName} ====")
    print(f"\nTotal objects detected in {frame_count} frames: {total_objects_detected}")
    print(f"Total runtime: {runtime_seconds:.2f} seconds")

    # Define your output file path
    output_file = "results.txt"

    # Open the file in write ('w') or append ('a') mode
    with open(output_file, 'a') as file:
        # Write the results to the file
        file.write(f"==== {roundName} ====\n")
        file.write(f"\nTotal objects detected in {frame_count} frames: {total_objects_detected}\n")
        file.write(f"Total runtime: {runtime_seconds:.2f} seconds\n\n")

    # Release the video capture
    cap.release()



models = ["models/yolo11s.pt","models/yolo11n.pt","models/yolo11x.pt","models/yolov8n.pt","models/yolov8x.pt"]
qualities = ["vid144.mkv","vid360.mkv","vid720.mkv","vid1080.mkv"]

for m in models:
    for q in qualities:
        name = m + q
        eval_round(name,YOLO(m),"vids/" + q)