

from abc import ABC, abstractmethod
from typing import Optional


class ExchangeRater(ABC):
    """
    Exchange rater
    """
    @abstractmethod
    def get_rate(self) -> Optional[dict]:
        """
        Gets the exchange rate from provider
        :return:
        :rtype:
        """
        raise NotImplementedError("Not implemented yet")

