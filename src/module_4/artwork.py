import requests

def get_artwork(query, limit):
    try:
        response = requests.get(
           "https://api.artic.edu/api/v1/artworks/search", 
            {"q": query,"limit": 3}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return[]
    
    content = response.json()
    return[artwork["title"] for artwork in content ["data"]]