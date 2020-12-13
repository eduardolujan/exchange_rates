# -*- coding: utf-8 -*-


import re

from .beautiful_soap_creator import BeautifulSoapCreator
from app.services.shared.utils.parse_utils import parse_to_float, parse_to_datetime


class BeautifulSoapScrapper:
    """
    BeautifulSoup content parser
    """
    def __init__(self, bs_creator: BeautifulSoapCreator = None):
        if not isinstance(bs_creator, BeautifulSoapCreator):
            raise Exception(f"Paramter bs_creator is not instance of BeautifulSoapCreator, {bs_creator}")

        self.__bs_creator = bs_creator

    def get_content(self):
        """
        Get content
        :return:
        :rtype:
        """
        bs_soap = self.__bs_creator.create()
        rows = bs_soap.find_all('tr', attrs={'class': re.compile(r"^renglonNon|renglonPar$")})
        exchanges_data = dict()

        for row in rows:
            tds = row.find_all('td')
            if len(tds) != 4:
                raise Exception(f"Parse error td not found content")

            date = tds[0].text.strip()
            _date = parse_to_datetime(date)
            fix = parse_to_float(tds[1].text.strip()) if tds[1] else 0.00
            dob = parse_to_float(tds[2].text.strip()) if tds[2] else 0.00
            to_pay = parse_to_float(tds[3].text.strip()) if tds[3] else 0.00

            row_data = dict(
                date=_date,
                fix=fix,
                dob=dob,
                to_pay=to_pay,
            )
            exchanges_data[_date] = row_data

        return exchanges_data

