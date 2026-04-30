# def calculate_growth(current, previous):
#     if not isinstance(current, (int, float)):
#         return None
#     elif not isinstance(previous, (int, float)):
#         return None
#     elif previous == 0:
#         return None
#     else:
#         growth = (current - previous) / previous*100
#         return growth

# artists = [
#     {"name": "Arlo Parks", "current": 1200000, "previous": 1000000},
#     {"name": "FKJ", "current": 850000, "previous": 800000},
#     {"name": "Sampha", "current": 850000, "previous": 500000},
# ]

# for artist in artists:
#     result = calculate_growth(artist.get("current"), artist.get("previous"))
#     if result is None:
#         print(f"{artist.get('name')}: Insufficient data")
#     else:
#         print(f"{artist.get('name')}: {result:.1f}% growth")

try:
    with open("data/artists.txt", "r") as f:
        artists = f.read().splitlines()
except FileNotFoundError as e:
    print(f"Error: {e}")
    artists = []

print(artists)