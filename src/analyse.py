import pandas as pd

def get_artist_info(name, subscribers, views):
    result = {
        "name": name,
        "subscribers": subscribers,
        "views": views
    }
    return result

def is_emerging(artist):
    if artist["subscribers"] >= 500000:
        return False
    else:
        return True

def filter_emerging(artists):
    emerge = []
    for artist in artists:
        if is_emerging(artist):
            emerge.append(artist)
    return emerge

def calculate_growth(current, previous):
    if not isinstance(current, (int, float)):
        return None
    if not isinstance(previous, (int, float)):
        return None
    if previous == 0:
        return None
    return (current - previous) / previous*100

def compare_snapshots(current_df, previous_df):
    snapshots = []
    merged = current_df.merge(previous_df, on="name", suffixes=("_current", "_previous"))
    for index, row in merged.iterrows():
        compare = calculate_growth(row["subscribers_current"], row["subscribers_previous"])
        snapshots.append({
            "name": row["name"],
            "subscriber_growth": compare
        })
    return pd.DataFrame(snapshots)