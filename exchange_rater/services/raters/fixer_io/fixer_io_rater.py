# -*- coding: utf-8 -*-


from typing import Optional
from datetime import datetime

from .fixer_api_client import FixerApiClient
from app.services.raters import ExchangeRater
from app.services.shared.utils.math_utils import truncate


class FixerExchangeRater(ExchangeRater):
    """
    Fixer IO Exchange Rater
    """

    def __init__(self, from_exchange='USD', to_exchange='MXN', api_client: FixerApiClient = None):
        """
        Fixer IO from 1 USD to X MXN
        :param from_exchange:
        :type from_exchange:
        :param to_exchange:
        :type to_exchange:
        :param api_client:
        :type api_client:
        """
        self.__api_client = api_client
        self.__from_exchange = from_exchange
        self.__to_exchange = to_exchange

    def get_rate(self) -> Optional[dict]:
        rate_data = self.__api_client.get_exchange()
        date = rate_data.get('date')
        from_rate = rate_data.get('rates', {}).get(self.__to_exchange)
        to_rate = rate_data.get('rates', {}).get(self.__from_exchange)
        price = from_rate / to_rate
        price = truncate(price, 4)
        rate_data = dict(
            last_updated=datetime.strptime(date, '%Y-%m-%d'),
            value=price
        )
        return rate_data

