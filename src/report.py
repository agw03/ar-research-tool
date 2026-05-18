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

def print_growth_report(growth_df):
    print("\n--- Growth Report ---")
    for index, row in growth_df.iterrows():
        print(f"{row['name']}: {row['subscriber_growth']:+.1f}%")

def save_growth_snapshot(growth_df):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    growth_df.to_csv(f"output/growth_{timestamp}.csv", index=False)