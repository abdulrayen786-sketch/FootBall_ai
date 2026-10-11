from ultralytics import YOLO
import pandas as pd

model = YOLO("yolo11n.pt")

results = model.track(
    source="football.mp4",
    tracker="bytetrack.yaml",
    stream=True
)

data = []

for frame_number, result in enumerate(results):
    if result.boxes.id is not None:
        track_ids = result.boxes.id.cpu().numpy()
        boxes = result.boxes.xyxy.cpu().numpy()

        for track_id, box in zip(track_ids, boxes):
            x1, y1, x2, y2 = box

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            data.append({
                "frame": frame_number,
                "player_id": int(track_id),
                "center_x": center_x,
                "center_y": center_y
            })

df = pd.DataFrame(data)

df.to_csv("player_tracking_data.csv", index=False)

print("\nPLAYER MOVEMENT DATA SAVED!")
print("File: player_tracking_data.csv")
print("Total tracking records:", len(df))