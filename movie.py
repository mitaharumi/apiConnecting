from access import apiKey
import requests

APIKEY = apiKey()

# HTTP requests METHODS
"""
GET -> grab data  
POST -> send data -> add/update data 

PATCH 
PUT 
DELETE  
"""
# endpoint
#   >> likes: where is where we want request (url)

# HTTP method
#   >> what http we need? <GET> <POST> <DEL> <PUT>

"""
endpoint: 
GET
/movie/{movie_id}

https://api.themoviedb.org/3/movie/550?api_key=e56a23d5fd1faaf6121235a3c0ba9052
"""

movieId = [550]
apiVersion = 3
apiBaseUrl = f'https://api.themoviedb.org/{apiVersion}'
endpointPath = f'/movie/{movieId}'
endpoint = f'{apiBaseUrl}{endpointPath}'

r = requests.get(endpoint, data={'APIKEY': APIKEY})
print(r.status_code)
print(r.text)
