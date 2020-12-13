# -*- coding: utf-8 -*-


from urllib.request import urlopen


class HtmlUrllibGetterClient:
    """
    Html Extractor Client
    """

    def __init__(self, url: str = None, url_open_fn: str = None):
        if type(url) is not str:
            raise ValueError(f"Parameter url is not string, {url}")

        self.__url = url
        self.__url_open = url_open_fn or urlopen

    def get_html(self) -> str:
        """
        Get html
        :return: html
        :rtype: str
        """
        html = self.__url_open(self.__url)
        return html
