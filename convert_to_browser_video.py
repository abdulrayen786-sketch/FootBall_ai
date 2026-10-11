import imageio_ffmpeg
import subprocess

input_file = "analyzed_football.mp4"
output_file = "analyzed_football_browser.mp4"

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

command = [
    ffmpeg,
    "-y",
    "-i", input_file,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    output_file
]

subprocess.run(command, check=True)

print("\nBROWSER-COMPATIBLE VIDEO CREATED!")
print("File:", output_file)