import requests

from access import apiKeyBling

apiKey = apiKeyBling()

'''
    # in bling documentation

    <?php 
        curl -X GET "https://bling.com.br/Api/v2/produtos/json/"
            -G 
            -d "apikey={apikey}"
    ?>
    https://bling.com.br/Api/v2/produtos/json/&apikey={apikey}"
    {protocol}{domain}/Api/{apiVersion}/produtos/json/&apikey={apiKey}
'''

apiVersion = 'v2'
protocol = 'https://'
domain = 'bling.com.br'

endpoint = f'{protocol}{domain}/Api{apiVersion}/produtos/json/&apikey={apiKey}'

r = requests.get(endpoint)
print(r.status_code)
print(r.json)