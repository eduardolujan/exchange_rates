# -*- coding: utf-8 -*-


from typing import Optional

from .beautiful_soap_scrapper import BeautifulSoapScrapper
from exchange_rater.services.raters import ExchangeRater


class OfficialJournalRater(ExchangeRater):
    """
    OfficialJournalRater implementation
    """

    def __init__(self, bs_scrapper: BeautifulSoapScrapper = None):
        if not isinstance(bs_scrapper, BeautifulSoapScrapper):
            raise Exception(f"Parameter bs_scrapper is not instance "
                            f"BeautifulSoapScrapper, {bs_scrapper}")

        self.__bs_scrapper = bs_scrapper

    def get_rate(self) -> Optional[dict]:
        """
        Gets rate
        :return: Optional[dict]
        :rtype: Optional[dict]
        """
        parsed_items = self.__bs_scrapper.get_content()
        items = sorted(parsed_items.items(), key=lambda item: item[0], reverse=True)
        _, data = items[0]
        exchange_data = dict(
            last_updated=data.get('date'),
            value=data.get('to_pay')
        )
        return exchange_data

