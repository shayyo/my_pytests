from http_client import HttpClient
import pytest


@pytest.fixture(scope='class')
def get_client():
    return HttpClient
