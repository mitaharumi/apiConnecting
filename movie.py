from access import apiKeyTheMovieDataBaseV3, apiKeyTheMovieDataBaseV4
import requests

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
    
    >> authentication API version 3:
    >> by single query parameter
    
    # example
    endpoint: 
    GET
    /movie/{movie_id}
    
    https://api.themoviedb.org/3/movie/550?api_key=e56a23d5fd1faaf6121235a3c0ba9052
    {protocol}    {domain}{version}{movie}{moveId}?api_key={apiKey} 

    >> authentication API version 4:
    >> token as a bearer
    
    https://www.themoviedb.org/authenticate/{REQUEST_TOKEN}

    https://www.themoviedb.org/authenticate/{REQUEST_TOKEN}?redirect_to=http://www.yourapp.com/approved

    >> token is expected to be sent along as a authorization
 
    cURL example: 
    <?php 
        curl --request GET \
          --url 'https://api.themoviedb.org/4/list/1' \
          --header 'Authorization: Bearer <<access_token>>' \
          --header 'Content-Type: application/json;charset=utf-8'
    ?>
        
"""
protocol = 'https'
domain = 'api.themoviedb.org'

# >> API version 3
apiVersion3 = '3'
apiKeyV3 = apiKeyTheMovieDataBaseV3()
movieId = '809-shrek-2'
endpointPath = f'movie/{movieId}'
# >> this is works in some APIs ...
# endpoint = f'{apiBaseUrl}{endpointPath}'
# r = requests.get(endpoint, data={'api_key': apiKey})
# r = requests.get(endpoint, json={'api_key': apiKey})
# <<
endpoint = f'{protocol}://{domain}/{apiVersion3}/{endpointPath}?api_key={apiKeyV3}'
r = requests.get(endpoint)
print('>> Version 3')
print(endpoint)
print('>> STATUS CODE')
print(r.status_code)
print('>> TEXT')
print(r.text)
print('>> JSON')
print(r.json())
# << API version 3 (END)

# >> API version 4
apiVersion4 = '4'
apiKeyV4 = apiKeyTheMovieDataBaseV4()
movieId = '808-shrek'
endpointPath = f'movie/{movieId}'
##### version 3: working! version 4: don't! -> have to learning how this versions works
## version 3 suports token
endpoint = f'{protocol}://{domain}/{apiVersion3}/{endpointPath}?api_key={apiKeyV4}'
headers = {
    'Authorization': f'Bearer {apiKeyV4}',
    'Content-Type': 'application/json;charset=utf-8'
    }
print('\n\n\n>> Version 4')
print(endpoint)
r = requests.get(endpoint, headers=headers)
print('>> STATUS CODE')
print(r.status_code)
print('>> TEXT')
print(r.text)
print('>> JSON')
print(r.json())

# search movie:

endpointPath = f'search/movie'
endpoint = f'{protocol}://{domain}/{apiVersion4}/{endpointPath}?api_key={apiKeyV3}&query=Shrek'
print(endpoint)
# >> API version 4 (END)
