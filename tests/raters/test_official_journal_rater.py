# -*- coding: utf-8 -*-

from typing import NoReturn
from unittest.mock import Mock, MagicMock, patch

import pytest


from tests.doubles.fake.official_journal import HtmlClientFaker
from exchange_rater.services.raters.official_journal import (
    HtmlClient,
    BeautifulSoapCreator,
    BeautifulSoapScrapper,
    OfficialJournalRater,
)


def test_official_journal_rate_keys(get_env) -> NoReturn:
    """
    Official journal get rate keys
    :return:
    :rtype:
    """
    env = get_env()
    official_journal_api_url = env.str("OFFICIAL_JOURNAL_API_URL")
    html_urllib_getter_client = HtmlClient(url=official_journal_api_url)
    bs_creator = BeautifulSoapCreator(client=html_urllib_getter_client)
    bs_scrapper = BeautifulSoapScrapper(bs_creator=bs_creator)
    official_journal_rater = OfficialJournalRater(bs_scrapper=bs_scrapper)
    rate = official_journal_rater.get_rate()
    assert 'last_updated' in rate
    assert 'value' in rate


def test_official_journal_rate_fake_html_client_empty_response(get_env) -> NoReturn:
    """
    Official journal get rate fake html client empty response
    """
    env = get_env()
    official_journal_api_url = env.str("OFFICIAL_JOURNAL_API_URL")
    html_urllib_getter_client = HtmlClientFaker(url=official_journal_api_url, response_file="empty_reponse.html")
    bs_creator = BeautifulSoapCreator(client=html_urllib_getter_client)
    bs_scrapper = BeautifulSoapScrapper(bs_creator=bs_creator)
    official_journal_rater = OfficialJournalRater(bs_scrapper=bs_scrapper)
    with pytest.raises(Exception, match="No Beautiful soap created"):
        rate = official_journal_rater.get_rate()


def test_official_journal_rate_fake_html_client_no_tr_rows(get_env) -> NoReturn:
    """
    Official journal get rate fake html client no tr rows
    """
    env = get_env()
    official_journal_api_url = env.str("OFFICIAL_JOURNAL_API_URL")
    html_urllib_getter_client = HtmlClientFaker(url=official_journal_api_url, response_file="no_trs_response.html")
    bs_creator = BeautifulSoapCreator(client=html_urllib_getter_client)
    bs_scrapper = BeautifulSoapScrapper(bs_creator=bs_creator)
    official_journal_rater = OfficialJournalRater(bs_scrapper=bs_scrapper)
    with pytest.raises(Exception, match="Not tr items found renglonNon or renglonPar"):
        rate = official_journal_rater.get_rate()


