from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("football.jpg")

results[0].show()

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        name = model.names[class_id]

        print(f"{name}: {confidence:.2f}")

print("\nFOOTBALL IMAGE TEST COMPLETE!")