from access import apiKeyTheMovieDataBase
import requests

apiKey = apiKeyTheMovieDataBase()


"""
    # HTTP requests METHODS
    
    GET -> grab data  
    POST -> send data -> add/update data 
    
    PATCH 
    PUT 
    DELETE  
    
    # endpoint
    #   >> likes: where is where we want request (url)
    
    # HTTP method
    #   >> what http we need? <GET> <POST> <DEL> <PUT>
    
    # example
    endpoint: 
    GET
    /movie/{movie_id}
    
    https://api.themoviedb.org/3/movie/550?api_key=e56a23d5fd1faaf6121235a3c0ba9052
    {protocol}    {domain}{version}{movie}{moveId}?api_key={apiKey} 
    
"""
movieId = '808-shrek'
apiVersion = 3
apiBaseUrl = f'https://api.themoviedb.org/{apiVersion}'

endpointPath = f'/movie/{movieId}'

# >> this is works in some APIs ...
# endpoint = f'{apiBaseUrl}{endpointPath}'
# r = requests.get(endpoint, data={'api_key': apiKey})
# r = requests.get(endpoint, json={'api_key': apiKey})
# <<

endpoint = f'{apiBaseUrl}{endpointPath}?api_key={apiKey}'
r = requests.get(endpoint)
print(r.status_code)
print(r.text)


