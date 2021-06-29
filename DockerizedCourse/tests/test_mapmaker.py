import pytest
from scripts.mapmaker import Point


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as e:
        Point("Buenos Aires", 12.11386, -200.39999)
    # breakpoint()
    assert str(e.value) == 'Invalid latitude or longitude'


def test_name_should_be_string():
    with pytest.raises(AttributeError) as e:
        Point(1234, 14.7167, 17.4677)
    assert str(e.value) == 'Location name should be a string'
