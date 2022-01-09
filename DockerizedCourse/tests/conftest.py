import pytest

from scripts import data_processor
from tests.constants import CITY_LIST_LOCATION


@pytest.fixture(scope="module")
def process_data():
    return data_processor.csv_reader(CITY_LIST_LOCATION)
