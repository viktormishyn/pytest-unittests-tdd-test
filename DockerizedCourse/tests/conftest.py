import pytest

from scripts import data_processor
from scripts import map_population_update
from tests.constants import CITY_LIST_LOCATION


@pytest.fixture(scope="module")
def process_data():
    return data_processor.csv_reader(CITY_LIST_LOCATION)


@pytest.fixture(scope="function")
def prep_transform_data(process_data):
    population_dict = {
        'Andorra': 77142,
        'Argentina': 44780677,
        'Cape Verde': 546388,
        'Germany': 83670653,
        'Greece': 10473455,
        'India': 1366417754,
        'Japan': 128860301,
        'Morocco': 36471769,
        'Senegal': 16296364,
        'United States': 329064917
    }
    data = process_data
    data_to_transform = map_population_update.MapData(data, False)
    yield data_to_transform, population_dict
