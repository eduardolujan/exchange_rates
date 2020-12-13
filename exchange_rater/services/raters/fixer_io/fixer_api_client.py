# -*- coding: utf-8 -*-


import json
from datetime import datetime

import requests
from exchange_rater.services.shared.utils.enviroment_files import get_env


env = get_env()


class FixerApiClient:
    """
    Fixer IO Api Client
    """
    def __init__(self, url='', api_key: str = None):
        self.__api_key = api_key or env.str("FIXER_IO_ACCESS_KEY", default=None)
        self.__url = url

    def get_exchange(self, date: datetime = datetime.now()):
        """
        Get exchange
        :return:
        :rtype:
        """

        if type(self.__api_key) is not str:
            raise ValueError(f"Fixer IO API KEY is not set")

        today_str = date.strftime('%Y-%m-%d')
        data_fixer_url = f"{self.__url}/{today_str}?access_key={self.__api_key}"
        response = requests.get(data_fixer_url)

        if response.status_code != 200:
            raise Exception(f"Fixer io responding without 200 status: {response.status_code}")

        content_json = response.content.decode('utf-8')
        data = json.loads(content_json)
        return data

