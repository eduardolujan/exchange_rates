# -*- coding: utf-8 -*-


from typing import Optional

from bs4 import BeautifulSoup

from .html_urllib_getter import HtmlUrllibGetterClient


class BeautifulSoapCreator:
    """
    Html Beautiful Soap Parser
    """

    def __init__(self, client: HtmlUrllibGetterClient = None):
        """
        Constructor
        :param client: Instance client of HtmlUrllibGetterClient
        :type client: HtmlUrllibGetterClient
        """
        if not isinstance(client, HtmlUrllibGetterClient):
            raise Exception(f"Parameter client is not instance of HtmlUrllibGetterClient")

        self.__client = client

    def create(self) -> Optional[BeautifulSoup]:
        """
        Get BeautifulSoup instance
        :return: Optional[BeautifulSoup]
        :rtype: Optional[BeautifulSoup]
        """
        try:
            html = self.__client.get_html()
            bs = BeautifulSoup(html)
            return bs
        except Exception as err:
            return None
