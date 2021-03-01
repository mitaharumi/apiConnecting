# first connection in API bling
# get all products and categories

import requests
from access import apiKeyBlingTribo

apiVersion = 'v2'
protocol = 'https'
domain = 'bling.com.br'

apiKey = apiKeyBlingTribo()
p = {
    'apikey':apiKey
}
'''
    authentication: 
        curl -X GET "https://bling.com.br/Api/v2/produtos/json/"
             -G 
             -d "apikey={apikey}"
        or 
        https://bling.com.br/Api/v2/produtos/json/&apikey={apikey}"
        
        example:
        endpoint = {protocol}{domain}/Api/{apiVersion}/produtos/json/
        p = {
            'apikey':apiKey
        }
        r = request.get(endpoint, params=p)
        or
        endpoint = {protocol}{domain}/Api/{apiVersion}/produtos/json/&apikey={apiKey}
        r = request.get(endpoint)
'''
# get all products
endpointProducts = f'{protocol}://{domain}/Api/{apiVersion}/produtos/json/'
print(endpointProducts)
r = requests.get(endpointProducts, params=p)
print('>> products')
print('status code: '+str(r.status_code))
'''
    product example structure:
        {'retorno': 
            {'produtos': 
                [
                    {'produto': 
                        {'id': '7731541129', 
                         'codigo': '1231', 
                         'descricao': 'Gestão Google Ads', 
                         'tipo': 'S', 
                         'situacao': 'Ativo', 
                         'unidade': 'Un', 
                         'preco': '399.9000000000', 
                         'precoCusto': None, 
                         'descricaoCurta': '', 
                         'descricaoComplementar': '', 
                         'dataInclusao': '2020-03-17', 
                         'dataAlteracao': '2020-03-17', 
                         'imageThumbnail': None, 
                         'urlVideo': '', 
                         'nomeFornecedor': '', 
                         'codigoFabricante': '', 
                         'marca': '', 
                         'class_fiscal': '', 
                         'cest': '', 
                         'origem': '0', 
                         'idGrupoProduto': '0', 
                         'linkExterno': '', 
                         'observacoes': '', 
                         'grupoProduto': None, 
                         'garantia': None, 
                         'descricaoFornecedor': None, 
                         'idFabricante': '', 
                         'categoria': 
                            {'id': '1081566', 
                             'descricao': 'Categoria padrão'
                             } # end dict categoria
                        }
                    }, # end dict produto 
                    {'produto': 
                        { 
                            ...
                        } 
                    }, # end dict produto
                    ...
                ] # end list of dict produto
            } # end dict produtos
        } # end dict retorno
'''
products = r.json()
products = products['retorno']
products = products['produtos']

# list of products
for product in products:
    # access inside produto
    productData = product['produto']
    productId = productData['id']
    print(productId)
    productDescription = productData['descricao']
    print(productDescription)
'''
    category:
        curl -X GET "https://bling.com.br/Api/v2/categorias/json/"
             -G
             -d "apikey={apikey}"
'''
endpointCategory = f'{protocol}://{domain}/Api/{apiVersion}/categorias/json/'
print(endpointCategory)
r = requests.get(endpointCategory, params=p)
print('\n>> category request: '+ str(r.status_code))
# print(r.json())
'''
    category return:
        {'retorno': 
            {'categorias': 
                [
                    {'categoria': 
                        {
                            'id': '128714', 
                            'descricao': 'Alero Drink', 
                            'idCategoriaPai': '0'}
                        }
                    }, # end dict categoria
                    {'categoria':
                        {
                        ...
                        }
                    }, # end dict categoria
                    ...
                ] # end list categoria
            } # end dict categorias
        } # end dict retorno
'''
# get all categories
dictReturn = r.json()['retorno']
dictCategories = dictReturn['categorias']

for category in dictCategories:
    id = category['categoria']
    id = id['id']
    print(id)
    description = category['categoria']
    description = description['descricao']
    print(description)
