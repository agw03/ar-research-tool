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
        part="statistics, topicDetails",
        id=channel_id
    )
    response = request.execute()
    return response

def get_artist_data(artist_name):
    channel_stats = get_channel_stats(artist_name)
    if not channel_stats["items"]:
        print(f"{artist_name} not found on YouTube")
        return None
    channel_id = channel_stats["items"][0]["id"]["channelId"]
    raw_stats = get_subscriber_count(channel_id)
    stats = raw_stats["items"][0]["statistics"]
    topics = raw_stats["items"][0].get("topicDetails", {}).get("topicCategories", [])
    if not any("Music" in topic for topic in topics):
        print(f"{artist_name}: not a music channel, skipping")
        return None
    return {
        "name": artist_name,
        "subscribers": int(stats["subscriberCount"]),
        "views": int(stats["viewCount"])
    }