from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=api_key)

def get_channel_stats(artist_name):
    request = youtube.search().list(
        q=artist_name,
        type="channel",
        part="snippet",
        maxResults=1
    )
    response = request.execute()
    return response

def get_subscriber_count(channel_id):
    request = youtube.channels().list(
        part="statistics, snippet",
        id=channel_id
    )
    response = request.execute()
    return response

channel_id = get_channel_stats("Arlo Parks")["items"][0]["id"]["channelId"]
print(f"Channel ID: {channel_id}")
print(get_subscriber_count(channel_id))

print(get_channel_stats("Arlo Parks"))

stats = get_subscriber_count(channel_id)["items"][0]["statistics"]
print(f"Subscribers: {stats['subscriberCount']}")
print(f"Total Views: {stats['viewCount']}")
print(f"Videos: {stats['videoCount']}")