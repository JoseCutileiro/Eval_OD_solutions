from moviepy.editor import VideoFileClip

# Input and Output file paths
input_file = "vids/vid1080.mkv"
output_file = "vids/vid360.mkv"

# Load the video
clip = VideoFileClip(input_file)

# Resize the video
clip_resized = clip.resize(height=360)  # You can specify width or height, and MoviePy will maintain aspect ratio

# Write the resized video to the output file
clip_resized.write_videofile(output_file, codec="libx264")

print(f"Video has been resized and saved as {output_file}")

