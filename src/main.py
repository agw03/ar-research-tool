from src.youtube import get_artist_data
from src.analyse import filter_emerging, compare_snapshots
from src.report import print_report, save_snapshot, print_growth_report, save_growth_snapshot
import pandas as pd
import os

try:
    with open("data/artists.txt", "r") as f:
        artist_names = f.read().splitlines()
except FileNotFoundError as e:
    print(f"Error: {e}")
    artist_names = []


artists = []

for artist_name in artist_names:
    artist_data = get_artist_data(artist_name)
    if artist_data:
        artists.append(artist_data)

emerging = filter_emerging(artists)
print_report(emerging)
save_snapshot(artists)

snapshot = sorted([f for f in os.listdir("output/") if f.startswith("snapshot_") and f.endswith(".csv")])
if len(snapshot) >= 2:
    current_df = pd.read_csv(f"output/{snapshot[-1]}")
    previous_df = pd.read_csv(f"output/{snapshot[-2]}")
    growth_df = compare_snapshots(current_df, previous_df)
    print_growth_report(growth_df)
    save_growth_snapshot(growth_df)
else:
    print("No previous snapshot to compare.")