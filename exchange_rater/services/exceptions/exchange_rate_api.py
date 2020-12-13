

class ExchangeRateApi(Exception):
    """
    ExchangeRateApi exception
    """
    def __init__(self, message, http_status=400):
        super(ExchangeRateApi, self).__init__(message)
        self.__http_status = http_status

    @property
    def http_status(self):
        return self.___http_status

    @http_status.setter
    def http_status(self, value):
        raise Exception(f"You can't override the http_status")

