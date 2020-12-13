# -*- coding: utf-8 -*-


import re
from typing import Optional
from datetime import datetime, date


def parse_to_float(value: str) -> Optional[float]:
    """
    Parse str to float
    """
    _value = value.strip()
    if re.match(r'\d*.\d+', _value):
        return float(_value)
    return None


def parse_to_datetime(value: str, format: str='%d/%m/%Y') -> Optional[date]:
    """
    Parse
    :param value: date in str format
    :type value: str
    :param format: format
    :type format: str
    :return: Optional[date]
    :rtype: Optional[date]
    """
    try:
        _value = value.strip()
        return datetime.strptime(_value, format)
    except Exception:
        return None


def parse_to_iso_format(value: str) -> Optional[str]:
    """
    Parse
    :param value: date in str format
    :type value: str
    :return: datetime in iso format Optional[str]
    :rtype: Optional[str]
    """
    try:
        _value = value.strip()
        return datetime.strptime(_value, '%d/%m/%Y')
    except Exception as err:
        return None
