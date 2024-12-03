from moviepy.editor import VideoFileClip


def up(out):
    
    # Input and Output file paths
    input_file = "out.mp4"
    output_file = f"out{out}.mp4"

    # Load the video
    clip = VideoFileClip(input_file)

    # Resize the video
    clip_resized = clip.resize(height=out)  # You can specify width or height, and MoviePy will maintain aspect ratio

    # Write the resized video to the output file
    clip_resized.write_videofile(output_file, codec="libx264")

    print(f"Video has been resized and saved as {output_file}")
    


qualities = [144,360,720]

for e in qualities:
    up(e)

