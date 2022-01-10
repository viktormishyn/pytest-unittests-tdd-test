import pytest

from scripts import data_aggregator


def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data(file_name_or_type='clean_map.csv')
    header_fields = list(data[0].keys())
    assert header_fields == ['Country', 'City',
                             'State_Or_Province', 'Lat', 'Long', 'Altitude']


def test_csv_reader_data_contents(process_data):
    """
    Happy Path test to examine that each row
    has the appropriate data type per field
    """
    data = process_data(file_name_or_type='clean_map.csv')

    # check row types
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))

    assert len(data) == 180
    assert data[0]['Country'] == 'Andorra'
    assert data[179]['Country'] == 'United States'


def test_data_population_update(prep_transform_data):
    """
    Happy Path test
    """
    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)
    # transform object in place

    for row in data_to_transform.get_data():
        assert 'Population' in row
        assert 'Updated' in row


@pytest.mark.parametrize("country,stat,expected", [
    ("Andorra", "Mean", 1641.42),
    ("Andorra", "Median", 1538.02),
    ("Argentina", "Median", 125.0)
])
def test_altitude_stat_per_country(process_data, country, stat, expected):
    data = process_data(file_name_or_type='clean_map.csv')
    res = data_aggregator.altitude_stat_per_country(data, country, stat)

    assert res == {'Country': country, stat: expected}
