# -*- coding: utf-8 -*-

from environ import Env
from exchange_rater.services.raters.official_journal import (
    HtmlUrllibGetterClient,
    BeautifulSoapCreator,
    BeautifulSoapScrapper,
    OfficialJournalRater,
)


def test_official_journal_get_rate_keys(get_env):
    """
    Official journal get rate keys
    :return:
    :rtype:
    """
    env = get_env()
    official_journal_api_url = env.str("OFFICIAL_JOURNAL_API_URL")
    html_urllib_getter_client = HtmlUrllibGetterClient(url=official_journal_api_url)
    bs_creator = BeautifulSoapCreator(client=html_urllib_getter_client)
    bs_scrapper = BeautifulSoapScrapper(bs_creator=bs_creator)
    official_journal_rater = OfficialJournalRater(bs_scrapper=bs_scrapper)
    rate = official_journal_rater.get_rate()
    assert 'last_updated' in rate
    assert 'value' in rate


