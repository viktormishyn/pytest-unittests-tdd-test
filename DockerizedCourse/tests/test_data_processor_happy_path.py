def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data
    header_fields = list(data[0].keys())
    assert header_fields == ['Country', 'City',
                             'State_Or_Province', 'Lat', 'Long', 'Altitude']


def test_csv_reader_data_contents(process_data):
    """
    Happy Path test to examine that each row
    has the appropriate data type per field
    """
    data = process_data

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
