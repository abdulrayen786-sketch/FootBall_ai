import pandas as pd
import numpy as np

# Load tracking data
df = pd.read_csv("player_tracking_data.csv")

statistics = []

for player_id, group in df.groupby("player_id"):
    group = group.sort_values("frame")

    x = group["center_x"].values
    y = group["center_y"].values

    # Calculate movement between consecutive frames
    distance = np.sqrt(
        np.diff(x) ** 2 +
        np.diff(y) ** 2
    )

    total_distance = np.sum(distance)

    statistics.append({
        "player_id": int(player_id),
        "frames_tracked": len(group),
        "total_movement_pixels": round(total_distance, 2),
        "average_movement_per_frame": round(
            np.mean(distance), 2
        ) if len(distance) > 0 else 0
    })

stats_df = pd.DataFrame(statistics)

stats_df.to_csv("player_statistics.csv", index=False)

print("\nPLAYER STATISTICS GENERATED!")
print("File: player_statistics.csv")
print("\nStatistics:")
print(stats_df.to_string(index=False))