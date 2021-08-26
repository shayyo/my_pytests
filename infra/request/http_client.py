import requests


class HttpClient:

    def __init__(self):
        self.__status_code = None
        self.__response_body = None

    def get_request(self, url='http://google.com'):
        r = requests.get(url)
        self.__status_code = r.status_code
        #self.__response_body = r.json()
        return self.__status_code #, self.__response_body
