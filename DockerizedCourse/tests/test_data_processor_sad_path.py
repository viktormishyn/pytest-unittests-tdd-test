import pytest

from scripts import data_processor
from constants import CITY_LIST_LOCATION_MALFORMED


def test_csv_reader_malformed_data_contents():
    """
    Sad Path test
    """
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(CITY_LIST_LOCATION_MALFORMED)
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"
