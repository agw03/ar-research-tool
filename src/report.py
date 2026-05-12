import pandas as pd
from datetime import datetime
from src.analyse import is_emerging

def save_snapshot(artists):
    df = pd.DataFrame(artists)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df.to_csv(f"output/snapshot_{timestamp}.csv", index=False)

def print_report(artists):
    for artist in artists:
        name = artist["name"]
        subs = artist["subscribers"]
        views = artist["views"]
        emerging = is_emerging(artist)
        print(f"Name: {name} | Subscribers: {subs} | Views: {views} | Emerging: {emerging}")