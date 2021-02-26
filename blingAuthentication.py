import requests

from access import apiKeyBlingTribo

apiKey = apiKeyBlingTribo()

'''
    # in bling documentation

    <?php 
        curl -X GET "https://bling.com.br/Api/v2/produtos/json/"
            -G 
            -d "apikey={apikey}"
    ?>
    https://bling.com.br/Api/v2/produtos/json/&apikey={apikey}"
    {protocol}{domain}/Api/{apiVersion}/produtos/json/&apikey={apiKey}

    # simple filters
    <?php 
        curl -X GET "https://bling.com.br/Api/v2/notasfiscais/json/"
             -G
             -d "filters=nome_do_filtro[valor]" 
             -d "apikey={apikey}"
    ?>


    # multiple filters
    <?php
        curl -X GET "https://bling.com.br/Api/v2/notasfiscais/json/"
             -G
             -d "filters=nome_do_filtro[valor];nome_do_filtro_2[valor]" 
             -d "apikey={apikey}"
    ?>
        
    
'''

apiVersion = 'v2'
protocol = 'https://'
domain = 'bling.com.br'

endpoint = f'{protocol}{domain}/Api{apiVersion}/produtos/json/&apikey={apiKey}'

r = requests.get(endpoint)

print(r.status_code)
print(r.json)
print(r.text)

print(r.text)