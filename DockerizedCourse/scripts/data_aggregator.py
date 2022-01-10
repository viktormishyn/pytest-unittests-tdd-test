from statistics import mean, median


def altitude_stat_per_country(data, country, stat):
    country_altitude_list = []
    for row in data:
        if row['Country'] == country:
            country_altitude_list.append(row['Altitude'])
    if stat.lower() == 'mean':
        result = mean(country_altitude_list)
    elif stat.lower() == 'median':
        result = median(country_altitude_list)
    return {'Country': country, stat: round(result, 2)}
