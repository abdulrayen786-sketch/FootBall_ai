from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in football video
model.predict(
    source="football.mp4",
    save=True
)

print("\nFOOTBALL VIDEO TEST COMPLETE!")