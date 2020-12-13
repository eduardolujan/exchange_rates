

import os

from exchange_rater.services.raters.official_journal import HtmlClient


class HtmlClientFaker(HtmlClient):
    """
    Html Client Faker
    """

    def __init__(self, url: str = None, request_get=None, response_file="wellformed_response.html"):
        super(HtmlClientFaker, self).__init__(url, request_get)
        self.__response_file = response_file

    def get_html(self):
        """
        Get html
        :return: html
        :rtype: BufferedReader
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        response_path = os.path.join(current_path, f"responses/{self.__response_file}")
        with open(response_path) as f:
            content = f.read()
            f.close()
            return content
