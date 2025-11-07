import requests


class RequestFailed(Exception):
    pass

class APIClient:
    '''
    Client to interact with some API
    '''

    def __init__(self):
        self.BASE_URL = "https://...."


    def get_response(self, url: str, params: dict = None, headers: str = None):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.InvalidURL:
            raise RequestFailed("Request failed, please try again.")

if __name__ == '__main__':
    try:
        client = APIClient()
        client.get_response(client.BASE_URL)
    except RequestFailed as e:
        print(e)

