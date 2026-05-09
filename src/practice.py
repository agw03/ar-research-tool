
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
     
artist = get_artist_info("Arlo Parks", 500000, 44528797)

def print_report(artists):
     for artist in artists:
          name = artist["name"]
          subs = artist["subscribers"]
          emerging = is_emerging(artist)
          print(f"{name} | Subscribers: {subs} | Emerging: {emerging}")

def filter_emerging(artists):
     emerge = []
     for artist in artists:
          if is_emerging(artist):
               emerge.append(artist)
     
     return emerge

artist1 = get_artist_info("Arlo Parks", 105000, 44528797)
artist2 = get_artist_info("FKJ", 850000, 20000000)
artist3 = get_artist_info("Sampha", 200000, 15000000)
artists = [artist1, artist2, artist3]

emerging_artists = filter_emerging(artists)
print_report(emerging_artists)
