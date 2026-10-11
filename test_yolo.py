from ultralytics import YOLO

# Load a pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Test the model
results = model("https://ultralytics.com/images/bus.jpg")

# Show the detection result
results[0].show()

print("YOLO TEST SUCCESSFUL!")