# -*- coding: utf-8 -*-


from app.services.raters.official_journal import (HtmlUrllibGetterClient,
                                                  BeautifulSoapCreator,
                                                  BeautifulSoapScrapper,
                                                  OfficialJournalRater, )
from app.services.raters.fixer_io import FixerApiClient, FixerExchangeRater
from app.services.raters.banxico import BanxicoApiClient, BanxicoRater


def main():
    """

    :return:
    :rtype:
    """
    ojf_api_url = "https://www.banxico.org.mx/tipcamb/tipCamMIAction.do"
    html_urllib_getter_client = HtmlUrllibGetterClient(url=ojf_api_url)
    bs_creator = BeautifulSoapCreator(client=html_urllib_getter_client)
    bs_scrapper = BeautifulSoapScrapper(bs_creator=bs_creator)
    official_journal_rater = OfficialJournalRater(bs_scrapper=bs_scrapper)
    rate = official_journal_rater.get_rate()
    print("Diario oficial", rate)

    fixer_io_api_key = "2403f378fea79fbef57aa5c43fb3692c"
    fixer_io_url = "http://data.fixer.io/api"
    fixer_io_api_client = FixerApiClient(url=fixer_io_url, api_key=fixer_io_api_key)
    fixer_io_exchange_rater = FixerExchangeRater(api_client=fixer_io_api_client)
    rate = fixer_io_exchange_rater.get_rate()
    print("Fixer io", rate)

    banxico_api_token = "81278a411674b6a9c2e134b18a4b96cf7d8d9792716cd5d01a8409a3a19a57a0"
    banxico_api_url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos"
    banxico_api_client = BanxicoApiClient(url=banxico_api_url, api_token=banxico_api_token)
    banxico_rater = BanxicoRater(api_client=banxico_api_client)
    rate = banxico_rater.get_rate()
    print("Banxico", rate)

if __name__ == '__main__':
    main()

