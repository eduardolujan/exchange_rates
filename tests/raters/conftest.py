# -*- coding: utf-8 -*-


import os
from pathlib import Path

import pytest
from environs import Env
from requests import Response


@pytest.fixture
def get_respose():
    def wrapp(content, http_status):
        response = Response()
        response._content = content
        response.status_code = http_status
        yield response
    return wrapp


@pytest.fixture
def get_env() -> Env:
    """
    Get enviroment
    """
    def wrapper():
        """

        :return:
        :rtype:
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        project_path = Path(current_path).parent.parent
        env = Env()
        env_path = os.path.join(project_path, '.env')

        if not os.path.exists(env_path):
            raise Exception(f"File not found {env_path}")

        env.read_env(env_path)
        return env
    return wrapper

