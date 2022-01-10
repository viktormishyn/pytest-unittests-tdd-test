import pytest


def test_csv_reader_malformed_data_contents(process_data):
    """
    Sad Path test
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type='malformed_map.csv')
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"


def test_data_population_no_update(prep_transform_data):
    """
    Sad Path test: We don't want the data transformed twice
    """
    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)
    with pytest.raises(Exception) as e:
        data_to_transform.add_population(population_dict)
    assert str(e.value) == 'You cannot transform the data twice'
