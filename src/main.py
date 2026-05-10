from src.youtube import get_channel_stats, get_subscriber_count
from src.analyse import get_artist_info, filter_emerging, is_emerging
from src.report import print_report

try:
    with open("data/artists.txt", "r") as f:
        artist_names = f.read().splitlines()
except FileNotFoundError as e:
    print(f"Error: {e}")
    artist_names = []

artists = []

for artist_name in artist_names:
    channel_stats = get_channel_stats(artist_name)
    channel_id = channel_stats["items"][0]["id"]["channelId"]
    stats = get_subscriber_count(channel_id)["items"][0]["statistics"]
    artist_info = get_artist_info(artist_name, int(stats["subscriberCount"]), int(stats["viewCount"]))
    artists.append(artist_info)

emerging = filter_emerging(artists)
print_report(emerging)