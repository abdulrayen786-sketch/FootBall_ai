from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Track players in the football video
model.track(
    source="football.mp4",
    tracker="bytetrack.yaml",
    save=True
)

print("\nFOOTBALL PLAYER TRACKING COMPLETE!")