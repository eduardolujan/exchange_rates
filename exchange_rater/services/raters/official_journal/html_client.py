# -*- coding: utf-8 -*-


import requests


class HtmlClient:
    """
    Html Extractor Client
    """

    def __init__(self, url: str = None, request_get=None):
        if type(url) is not str:
            raise Exception(f"Parameter url is not string, {url}")
        self.__url = url
        self.__request_get = request_get or requests.get

    def get_html(self):
        """
        Get html
        :return: html
        :rtype: BufferedReader
        """

        respose = self.__request_get(self.__url)
        response_content = respose.content.decode('utf-8')
        if respose.status_code not in [200]:
            raise Exception(f"The url {self.__url} response without code 200, "
                            f"{respose.http_status}, {response_content}")
        return response_content
