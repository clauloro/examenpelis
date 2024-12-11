import requests

API_KEY = "7212040052760a189a48613221440e5b"  # Tu API Key
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies():
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
