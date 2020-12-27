
import requests
import json
from datetime import datetime, timedelta

from exchange_rater.services.shared.utils.enviroment_files import get_env


env = get_env()


class BanxicoApiClient:
    """
    Banxico Client Api
    """

    def __init__(self, url: str = None, date: datetime = datetime.now(), days_offset=-1, api_token=None):
        """
        Constructor
        :param url:
        :type url:
        :param date:
        :type date:
        :param days_offset:
        :type days_offset:
        :param api_token:
        :type api_token:
        """
        self.__date = date
        self.__days_offset = days_offset
        self.__token = api_token or env.str("BANXICO_API_TOKEN", default=None)
        self.__url = url

    def get_rates(self) -> dict:
        """
        Get rates from api
        :return: data dict
        :rtype: dict
        """
        _from_date = self.__date + timedelta(days=self.__days_offset)
        _from_date = _from_date.strftime('%Y-%m-%d')
        _to_date = self.__date.strftime('%Y-%m-%d')
        url_banxico_rater = f"{self.__url}/{_from_date}/{_to_date}/?token={self.__token}"
        response = requests.get(url_banxico_rater)
        response_content = response.content.decode('utf-8')

        if response.status_code not in [200]:
            raise Exception(f"Banxico response without code 200, {response.status_code}, message:{response_content}")

        response_json = json.loads(response_content)
        series = response_json.get('bmx', {}).get('series', [])

        serie_sf43718 = series[0]
        return serie_sf43718.get('datos', [])
