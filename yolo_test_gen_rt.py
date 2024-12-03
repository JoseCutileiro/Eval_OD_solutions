import cv2
from ultralytics import YOLO
import time


iterff = 0

def rl_fun(m,q):

    global iterff
    
    iterff += 1

    # Initialize the YOLO model
    model = YOLO(m)

    # Open the video file
    cap = cv2.VideoCapture(f'out{q}.mp4')

    # Get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Initialize variable to track the total time spent processing frames
    sum_time_took = -1.5

    # Open the text file to write results
    with open(f'res_rt/{iterff}_{q}.txt', 'w') as f:
        frame_number = 0
        
        while True:
            # Read the next frame
            ret, frame = cap.read()
            
            if not ret:
                break  # End of the video
            
            frame_number += 1
            
            # Start timer to simulate real-time processing
            start_time = time.time()
            
            # Execute the YOLO model on the current frame
            results = model(frame)

            # Extract detection boxes
            detections = results[0].boxes
            class_ids = detections.cls.cpu().numpy()  # Detected class IDs
            labels = results[0].names  # Class names (e.g., 'car', 'person', 'truck')

            # Counters for classes of interest
            counts = {'car': 0, 'person': 0}
            
            for class_id in class_ids:
                # Get the name of the detected class
                label_name = labels[int(class_id)]

                # Treat 'truck' as 'car'
                if label_name == 'truck':
                    counts['car'] += 1
                elif label_name in counts:
                    counts[label_name] += 1

            # Prepare a detection string (e.g., "5 car, 8 person")
            detection_str = ', '.join([f"{count} {label}" for label, count in counts.items() if count > 0])
            
            # Calculate the time taken to process the current frame
            processing_time = time.time() - start_time

            # Update the sum of time taken
            sum_time_took += processing_time
            
            # After catching up (if needed), write the result for the current frame
            f.write(detection_str + '\n')
            print(f"Processed frame {frame_number}")
            
            # Check if we need to skip frames to catch up
            while sum_time_took > (1 / fps):
                # If sum_time_took exceeds the allowed time for one frame, skip frames
                f.write('\n')  # Write an empty line to the output file for the skipped frame
                print(f"Frame {frame_number} skipped.")
                
                # Decrease sum_time_took by the time we should have spent on one frame
                sum_time_took -= (1 / fps)
                frame_number += 1  # Move to the next frame
                
                # Read the next frame
                ret, frame = cap.read()
                if not ret:
                    break  # End of the video
                



    # Release the video capture object
    cap.release()

models = ["models/yolov8n.pt","models/yolov8m.pt","models/yolo11n.pt","models/yolo11s.pt","models/yolo11m.pt"]
quals = [144,360,720,1080]

for m in models:
    for q in quals:
        rl_fun(m,q)
        