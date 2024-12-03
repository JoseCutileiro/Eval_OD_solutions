import matplotlib.pyplot as plt
import numpy as np

# Data for each model at different resolutions
resolutions = ['144p', '360p', '720p', '1080p']
models = {
    "yolo11s": [13.84, 12.93, 15.70, 19.08],
    "yolo11n": [13.73, 13.79, 15.75, 18.11],
    "yolo11x": [61.55, 62.73, 65.36, 69.68],
    "yolov8n": [13.67, 13.46, 16.37, 18.39],
    "yolov8x": [63.55, 65.99, 69.73, 74.14]
}

# Set up the figure and axis
plt.figure(figsize=(10, 6))


m = []

# Plot each model with transparency (alpha) to overlay them
for model, times in models.items():
    plt.plot(resolutions, times, label=model, alpha=0.5)
    
    v = (max(times) - min(times)) / min(times)
    
    print("PERCENTAGE: " + str(v))
    m.append(v)

print("CRESCEU: " + str(np.mean(m)))
    

# Set y-axis limits based on the minimum and maximum times with extra padding
y_min = min(min(times) for times in models.values()) - 4
y_max = max(max(times) for times in models.values()) + 4
plt.ylim(y_min, y_max)

# Add labels, title, and grid
plt.xlabel('Resolution')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Comparison Across Models and Resolutions')
plt.grid(True)

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.show()
