from cityiqaccess import constants
from cityiqaccess import parking
import requests
import os
from dotenv import load_dotenv
import base64
from cityiqaccess import environmental
from gmplot import *
from colour import Color
import math


class CityIQ:

    def __init__(self, token=None):
        if (token):
            self.token = token
        else:
            self.token = self.collect_token()
        self.parking = parking.Parking(self.token)
        self.env = environmental.Env(self.token)

    def collect_token(self):
        """
        Gets the authentication using appropriate credentials.
        Returns:  the authentication token
        """

        # loads the env variables
        load_dotenv()
        client_id = os.getenv("CLIENTID")  # inside a hidden .env file
        client_secret = os.getenv("ClIENTSECRET")  # inside a hidden .env file

        headers = {
            'Authorization': 'Basic ' + (base64.b64encode(bytes(client_id + ':' + client_secret, 'ascii'))).decode(
                'ascii')}
        response = requests.request(constants.GET, constants.uaa + "/oauth/token?grant_type=client_credentials",
                                    headers=headers)
        return response.json()["access_token"]

    def get_token(self):
        return self.token

    def set_token(self, new_token):
        self.token = new_token

    ##################### PARKING #####################

    def get_parking_metadata(self, bbox=constants.default_bbox):
        """
        Returns the parking metadata (assetUid, parentAssetUid, eventTypes, mediaType, assetType, coordinates) found in
        the bbox provided. If no bbox is provided, default bbox will be used.
        Args:
            bbox: the bounding box of area you want to get the parking metadata from

        Returns: JSON formated dictionary

        """
        return self.parking.get_parking_metadata(bbox)

    def get_open_parking_spots_by_bbox(self, starttime, endtime, bbox=constants.default_bbox):
        """
        Returns all OPEN parking spots found inside the bbox provided from start timestamp to end timestamp
        (UNIX timestamp). If no bbox is provided, default bbox will be used.
        Args:
            starttime: start timestamp
            endtime: end timestamp
            bbox:  the bounding box of the area you want to get the open parking data from.

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        and measures

        """
        return self.parking.get_parking_events_by_location(constants.PKIN, starttime, endtime, bbox)

    def get_occupied_parking_spots_by_bbox(self, starttime, endtime, bbox=constants.default_bbox):
        """
        Returns all OCCUPIED parking spots found inside the bbox provided from start timestamp to end timestamp
        (UNIX timestamp). If no bbox is provided, default bbox will be used.
        Args:
            starttime: start timestamp
            endtime: end timestamp
            bbox:  the bounding box of the area you want to get the open parking data from.

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        and measures

        """
        return self.parking.get_parking_events_by_location(constants.PKOUT, starttime, endtime, bbox)

    def get_open_parking_spots_by_locationuid(self, locationid, starttime, endtime):
        """
         Returns all OPEN parking spots records on location ID provided from start timestamp to end timestamp
        (UNIX timestamp).
        Args:
            starttime: start timestamp
            endtime: end timestamp
            locationid:  the locationUid of the assets you are trying to get the data of

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        measures, and metaData

        """
        return self.parking.get_parking_events_by_locationuid(locationid, constants.PKIN, starttime, endtime)

    def get_occupied_parking_spots_by_locationuid(self, locationid, starttime, endtime):
        """
        Returns all OCCUPIED parking spots records on location ID provided from start timestamp to end timestamp
        (UNIX timestamp).
        Args:
            starttime: start timestamp
            endtime: end timestamp
            locationid:  the locationUid of the assets you are trying to get the data of

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        measures, and metaData

        """
        return self.parking.get_parking_events_by_locationuid(locationid, constants.PKOUT, starttime, endtime)

    def get_open_parking_spots_by_assetuid(self, assetuid, starttime, endtime):
        """
        Returns all OPEN parking spots records based on Asset ID provided from start timestamp to end timestamp
        (UNIX timestamp).
        Args:
            starttime: start timestamp
            endtime: end timestamp
            assetuid:  the assetUID of the assets you are trying to get the data of

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        measures, and metaData

        """
        return self.parking.get_parking_events_by_assetuid(assetuid, constants.PKIN, starttime, endtime)

    def get_occupied_parking_spots_by_assetuid(self, assetuid, starttime, endtime):
        """
        Returns all OCCUPIED parking spots records based on Asset ID provided from start timestamp to end timestamp
        (UNIX timestamp).
        Args:
            starttime: start timestamp
            endtime: end timestamp
            assetuid:  the assetUID of the assets you are trying to get the data of

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (orgPixelCoordinates, pixelCoordinates, objectUid, geoCoordinates), imageAssetUid,
        measures, and metaData

        """
        return self.parking.get_parking_events_by_assetuid(assetuid, constants.PKOUT, starttime, endtime)

    ##################### ENVIRONMENTAL #####################

    def get_temperature_metadata_by_bbox(self, bbox=constants.default_bbox):
        """
        Returns TEMPERATURE data for assets found inside the bbox provided. If no bbox is provided, default
        bbox will be used.

        Args:
            bbox: the bounding box of the area you want to get temperature data from.

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """
        return self.env.get_env_sensors_metadata(constants.TEMPERATURE, bbox)

    def get_humidity_metadata_by_bbox(self, bbox=constants.default_bbox):
        """
        Returns HUMIDITY data for assets found inside the bbox provided. If no bbox is provided, default
        bbox will be used.

        Args:
            bbox: the bounding box of the area you want to get HUMIDITY data from.

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """
        return self.env.get_env_sensors_metadata(constants.HUMIDITY, bbox)

    def get_pressure_metadata_by_bbox(self, bbox=constants.default_bbox):
        """
        Returns PRESSURE data for assets found inside the bbox provided. If no bbox is provided, default
        bbox will be used.

        Args:
            bbox: the bounding box of the area you want to get PRESSURE data from.

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """
        return self.env.get_env_sensors_metadata(constants.PRESSURE, bbox)

    def get_temperature_by_assetuid(self, assetuid, starttime, endtime):
        """

        Returns TEMPERATURE data for assetuid provided.
        bbox will be used.
        Args:
            assetuid: the assetuid you want the TEMPERATURE data for
            starttime: start timestamp
            endtime: end timestamp

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """

        return self.env.get_env_data_by_assetuid(assetuid, starttime, endtime, constants.TEMPERATURE)

    def get_humidity_by_assetuid(self, assetuid, starttime, endtime):
        """
        Returns HUMIDITY data for assetuid provided.
        bbox will be used.
        Args:
            assetuid: the assetuid you want the HUMIDITY data for
            starttime: start timestamp
            endtime: end timestamp

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """
        return self.env.get_env_data_by_assetuid(assetuid, starttime, endtime, constants.HUMIDITY)

    def get_pressure_by_assetuid(self, assetuid, starttime, endtime):
        """
        Returns PRESSURE data for assetuid provided.
        bbox will be used.
        Args:
            assetuid: the assetuid you want the PRESSURE data for
            starttime: start timestamp
            endtime: end timestamp

        Returns: JSON formated dictionary with locationUid, assetUid, eventType, timestamp, timestamp,
        properties (units,powerOf10), imageAssetUid,
        measures (min, median, max, mean), and metaData

        """
        return self.env.get_env_data_by_assetuid(assetuid, starttime, endtime, constants.PRESSURE)

    ##################### TRAFFIC #####################
    # TODO

    ##################### PEDESTRAIN #####################
    # TODO


    ##################### MAPPING #####################
    # TODO
    def _get_color(self, value):
        """
        Returns a hex color based on the value of the temperature.
        :param value: the temperature value
        :return: hex
        """

        blue = Color("#37e8ca")
        colors = list(blue.range_to(Color("#9b1717"), 11)) #color gradient

        # create a color gradient based on temperature
        index = math.ceil((85-int(value))/5)
        index = 11 - index

        #returns hex value
        if (value > 85):
            index = 10
        #print(value, index)
        return colors[index].hex


    def gradient_temp(self, temp_data, temp_coords, filename):
        if(len(temp_data) == 0):
            print("No data found.")
            return
        all_coord = []
        for i in temp_coords:
            test = i.split(":")
            all_coord.append((float(test[0]), float(test[1])))

        lat, log = zip(*all_coord)
        print(f'Found {len(lat)} total')


        gmap = gmplot.GoogleMapPlotter(32.713227, -117.163201, 16.3)  # starting zoom
        gmap.apikey = os.getenv("google_api_key")

        for i in range(len(lat)):
            gmap.scatter([lat[i]],[log[i]],self._get_color(temp_data[i]),size=20, marker=False)

        gmap.draw(f"{filename}.html")
        print(f"Published to {filename}.html")
