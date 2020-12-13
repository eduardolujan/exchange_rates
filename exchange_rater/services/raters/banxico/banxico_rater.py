
from typing import Optional

from .banxico_api_client import BanxicoApiClient
from app.services.raters import ExchangeRater
from app.services.shared.utils.parse_utils import parse_to_datetime, parse_to_float


class BanxicoRater(ExchangeRater):
    """
    BanxicoRater exchange rater
    """
    parse_date_format = '%d/%m/%Y'

    def __init__(self, api_client: BanxicoApiClient):
        self.__api_client = api_client

    def get_rate(self) -> Optional[dict]:
        """
        Get rate
        :return:
        :rtype:
        """
        data_rates = self.__api_client.get_rates()
        formatted_values = {
            parse_to_datetime(
                item.get('fecha'),
                format=self.parse_date_format): dict(last_updated=parse_to_datetime(item.get('fecha')),
                                                     value=parse_to_float(item.get('dato'))) for item in data_rates}
        ordered_items = sorted(formatted_values.items(), key=lambda item: item[0], reverse=True)
        if not ordered_items:
            raise Exception(f"Empty values in baxico results")
        _, today_rate = ordered_items[0]

        return today_rate

