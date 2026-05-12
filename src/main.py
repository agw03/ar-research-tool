from src.youtube import get_channel_stats, get_subscriber_count
from src.analyse import get_artist_info, filter_emerging, is_emerging, compare_snapshots, calculate_growth
from src.report import print_report, save_snapshot
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
    #verified_name = verify_artist(artist_name)
    #if not verified_name:
       # print(f"{artist_name} not found on Spotify. Skipping...")
        #continue
    channel_stats = get_channel_stats(artist_name)
    if not channel_stats["items"]:
        print(f"{artist_name} not found on YouTube")
        continue
    channel_id = channel_stats["items"][0]["id"]["channelId"]
    raw_stats = get_subscriber_count(channel_id)
    stats = raw_stats["items"][0]["statistics"]
    topics = raw_stats["items"][0].get("topicDetails", {}).get("topicCategories", [])
    if not any("Music" in topic for topic in topics):
        print(f"{artist_name}: not a music channel, skipping")
        continue
    artist_info = get_artist_info(artist_name, int(stats["subscriberCount"]), int(stats["viewCount"]))
    artists.append(artist_info)

emerging = filter_emerging(artists)
print_report(emerging)
save_snapshot(artists)

snapshot = sorted([f for f in os.listdir("output/") if f.endswith(".csv")])
if len(snapshot) >= 2:
    current_df = pd.read_csv(f"output/{snapshot[-1]}")
    previous_df = pd.read_csv(f"output/{snapshot[-2]}")
    growth_df = compare_snapshots(current_df, previous_df)
    print(growth_df)
else:
    print("No previous snapshot to compare.")