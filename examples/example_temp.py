from cityiqaccess import cityiq
import pandas as pd
from cityiqaccess import constants
import time
from datetime import datetime
import numpy as np
from sys import stdout


def convert_time(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%d-%m-%Y %H:%M')


def convert_to_frat(temp):
    return ((temp / 10) - 273.15) * (9 / 5.0) + 32


def month_to_month_temp(start_time, end_time, df, file_out_name, city):
    """
    Creates a .html file with the location of the sensor in color corresponding to the temperature for that area.
    :param start_time: timestamp of the start time you want to get the data
    :param end_time: timestamp of the end time you want to stop getting the data
    :param df: the dataframe with assestUid
    :param file_out_name: name of the html file
    :param city: the CityIQ object
    :return: none
    """

    # stores the temperature value and the sensors coordinates
    temp_data = []
    temp_coors = []

    count = 0
    # for each assetUid, it requests for temperature data from given start time to end time
    for i in range(len(df)):
        temp_results = city.get_temperature_by_assetuid(df.assetUid[i], start_time, end_time)
        df2 = pd.DataFrame.from_dict(temp_results['content'], orient='columns')
        try:
            median = [d.get('median') for d in df2.measures]  # finds the median from the sensors
            temp_data.append(convert_to_frat(np.mean(median)))
            temp_coors.append(df.coordinates[i])
        except AttributeError:
            # No data from this asset
            pass

        count += 1
        if count % 100 == 0:
            stdout.write('\r%d%% done.' % (100.0 * count / len(df)))
            stdout.flush()

    # uncomment if you want to save the temp data in a .txt file
    # with open(f'{file_out_name}.txt', 'w') as file_out:
    #     for i in range(len(temp_data)):
    #         file_out.write(str(temp_data[i]) + '\t' + str(temp_coors[i]) + '\n')

    city.gradient_temp(temp_data, temp_coors, file_out_name)


sandiego = cityiq.CityIQ()

# gets all the environment sensors from passed in bbox
all_env_data = sandiego.get_temperature_metadata_by_bbox(constants.sddt_bbox)

# creates a dataframe from the data
df = pd.DataFrame.from_dict(all_env_data['content'], orient='columns')

print('Total assets found:', len(df))


# use https://www.epochconverter.com/ to get the timeestamps
months_timestamps = {'may_2019': (1556755200000, 1556758800000),
                     'april_2019': (1554163200000, 1554166800000),
                     'march_2019': (1551488400000, 1551492000000),
                     'feb_2019': (1549069200000, 1549072800000),
                     'jan_2019': (1546390800000, 1546394400000),
                     'dec_2018': (1543712400000, 1543716000000),
                     'nov_2018': (1541116800000, 1541120400000),
                     'oct_2018': (1538438400000, 1538442000000),
                     'sept_2018': (1535846400000, 1535850000000),
                     'aug_2018': (1533168000000, 1533171600000),
                     'july_2018': (1530489600000, 1530493200000),
                     'june_2018': (1527897600000, 1527901200000),
                     'may_2018': (1525219200000, 1525222800000),
                     }

count = 0
for i in months_timestamps:
    month_to_month_temp(months_timestamps[i][0], months_timestamps[i][1], df, i + '_5to6pm', sandiego)
    print(count)
    count += 1
