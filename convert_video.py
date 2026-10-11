import cv2

input_file = "runs/detect/track/football.avi"
output_file = "analyzed_football.mp4"

cap = cv2.VideoCapture(input_file)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_file,
    fourcc,
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)

cap.release()
out.release()

print("VIDEO CONVERSION COMPLETE!")
print("Created:", output_file)