import pandas as pd


cols = ['time', 'wind', 'name', 'birth-year', 'team', 'position', 'location', 'date', 'sex', 'event', 'type']
event_types = ['P', 'I', 'S']  # track, indoor, road
years = list(range(2005, 2022))
event_keys = {'distance': 0, 'type': 1, 'event_number': 2, 'down_limit': 3, 'sex': 4}
events = {
    '60m': [60, ['I'], '01', '6.0', ['M', 'F']],
    '100m': [100, ['P'], '03', '9.0', ['M', 'F']],
    '110m H91': [110, ['P'], 'KB', '10.0', ['M']],  # only male
    '110m H84': [100, ['P'], 'H2', '10.0', ['F']],  # only female
    '200m': [200, ['P', 'I'], '04', '18.0', ['M', 'F']],
    '300m': [300, ['P'], '05', '29.0', ['M', 'F']],
    '400m': [400, ['P', 'I'], '06', '40.0', ['M', 'F']],
    '400m H': [400, ['P'], 'KQ', '40.0', ['M']],  # only male
    '4000m H76': [400, ['P'], 'KS', '45.0', ['F']],  # only female
    '800m': [800, ['P', 'I'], '08', '1:40.0', ['M', 'F']],
    '1000m': [1000, ['P'], '09', '2:0.0', ['M', 'F']],
    '1500m': [1500, ['P', 'I'], '11', '3:20.0', ['M', 'F']],
    '3000m': [3000, ['P', 'I'], '13', '7:10.0', ['M', 'F']],
    '3000m SC H84': [3000, ['P'], 'S3', '7:30.0', ['M']],  # only male
    '3000m SC H76': [3000, ['P'], 'S4', '8:30.0', ['F']],  # only female
    '5000m': [5000, ['P'], '14', '12:20.0', ['M', 'F']],
    '10000m': [10000, ['P'], '15', '26:0.0', ['M', 'F']],
    'Halfmarathon': [21097, ['S'], '68', '55:0.0', ['M', 'F']],   # exclude B events (90)
    'Marathon': [42195, ['S'], '53', '1h55:0', ['M', 'F']],  # exclude B events (85)
    '5km road': [5000, ['S'], '92', '12:20.0', ['M', 'F']],
    '10k road': [10000, ['S'], '18', '26:0.0', ['M', 'F']],
    '50k road': [50000, ['S'], '70', '2h20:0', ['M', 'F']],
    '100k road': [100000, ['S'], '71', '5h50:0', ['M', 'F']],
}


def str_to_time(time_str):
    if 'h' in time_str and ':' in time_str and '.' in time_str:
        time_format = '%Hh%M:%S.%f'
    elif 'h' in time_str and ':' in time_str:
        time_format = '%Hh%M:%S'
    elif 'h' in time_str:
        time_format = '%Hh%M'
    elif ':' in time_str and '.' in time_str:
        time_format = '%M:%S.%f'
    elif ':' in time_str:
        if len(time_str.split(':')) == 3:
            time_format = '%M:%S:%f'
        else:
            time_format = '%M:%S'
    elif '.' in time_str:
        time_format = '%S.%f'
    else:
        return pd.NA
    return pd.to_datetime(time_str, format=time_format).time()
