from src.analyse import is_emerging

def print_report(artists):
    for artist in artists:
        name = artist["name"]
        subs = artist["subscribers"]
        views = artist["views"]
        emerging = is_emerging(artist)
        print(f"Name: {name} | Subscribers: {subs} | Views: {views} | Emerging: {emerging}")