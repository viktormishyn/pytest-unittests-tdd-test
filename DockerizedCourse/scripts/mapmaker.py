class Point():
    def __init__(self, name, lat, long):

        if not isinstance(name, str):
            raise AttributeError("Location name should be a string")

        self._name = name

        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid latitude or longitude")

        self._lat = lat
        self._long = long

    def get_lat_long(self):
        return self._lat, self._long
