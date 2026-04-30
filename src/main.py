def calculate_growth(current, previous):
    if not isinstance(current, (int, float)):
        return None
    elif not isinstance(previous, (int, float)):
        return None
    elif previous == 0:
        return None
    else:
        growth = (current - previous) / previous*100
        return growth

artists = [
    {"name": "Arlo Parks", "current": 1200000, "previous": 1000000},
    {"name": "FKJ", "current": 850000, "previous": 800000},
    {"name": "Sampha", "current": "unknown", "previous": 500000},
]

for artist in artists:
    result = calculate_growth(artist["current"], artist["previous"])
    if result is None:
        print(f"{artist['name']}: Insufficient data")
    else:
        print(f"{artist['name']}: {result:.1f}% growth")