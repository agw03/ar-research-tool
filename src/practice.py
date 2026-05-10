
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

emerging_artists = filter_emerging(artists)
print_report(emerging_artists)
