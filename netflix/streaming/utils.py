import requests

API_KEY = "7212040052760a189a48613221440e5b"  # Tu API Key
BASE_URL = "https://api.themoviedb.org/3"

def fetch_data_from_api(endpoint, params=None, language='es-ES'):
    if not params:
        params = {}

    url = f'{BASE_URL}/{endpoint}'
    params['api_key'] = API_KEY
    params['language'] = language
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en la API: {response.status_code} - {response.text}")


def fetch_movies():
    """
    Obtiene una lista de películas populares desde el endpoint 'movie/popular'.
    """
    endpoint = 'movie/popular'
    response = fetch_data_from_api(endpoint)
    return response.get('results', [])