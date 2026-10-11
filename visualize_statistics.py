import pandas as pd
import matplotlib.pyplot as plt

# Load player statistics
df = pd.read_csv("player_statistics.csv")

# Select players with the most tracked frames
top_players = df.nlargest(10, "frames_tracked")

plt.figure(figsize=(10, 6))

plt.bar(
    top_players["player_id"].astype(str),
    top_players["total_movement_pixels"]
)

plt.xlabel("Player Tracking ID")
plt.ylabel("Total Movement (Pixels)")
plt.title("Top 10 Tracked Players - Movement Analysis")

plt.tight_layout()
plt.savefig("player_movement_chart.png")

print("\nPLAYER MOVEMENT CHART CREATED!")
print("File: player_movement_chart.png")