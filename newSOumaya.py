from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '13',
    'limit': '1',
}

soumaya_token= '69da3e74-f280-4e41-b849-c623a11fd588'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': soumaya_token
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)