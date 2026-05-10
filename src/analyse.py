
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