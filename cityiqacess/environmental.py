import constants
import os
import requests



class Env:

    def __init__(self, token):
        self.token = token

    def _get_header(self, zone):
        """
        Creates the header to pass in with the requests.
        :param zone: The Zone ID of the city
        :return: Header in the form of a dict
        """
        return {'Authorization': 'Bearer ' + self.token, 'Predix-Zone-Id': zone}

    def get_env_sensors_metadata(self, eventtype, bbox=constants.default_bbox):
        """
        Gets all the metadata for the env sensors in the bbox provided. Return Example:
        'content': [{
            'assetUid': 'xxx.xxx.x',
            'parentAssetUid': 'xxxx-xxx-xxx-x-xxx-xxx',
            'eventTypes': ['HUMIDITY', 'ORIENTATION', 'TEMPERATURE', 'PRESSURE'],
            'mediaType': None,
            'assetType': 'ENV_SENSOR',
            'coordinates': '{lat}:{log}'
        }, {
        :param eventtype: Type of event (Temperature, Pressure, or Humidity)
        :param bbox: Bounding box to where to find all the assets from.
        :return: JSON formated string with the content showed above.
        """

        headers = self._get_header(constants.environmental_zone)

        response = requests.request(constants.GET,
                                    f'{constants.metadata_api}/search?bbox={bbox}&page=0&size=30000&q=eventTypes:{eventtype}',
                                    headers=headers)
        return response.json()

    def get_env_data_by_assetuid(self, assetUid, start_time, end_time, eventtype=constants.TEMPERATURE):
        """

        Args:
            assetUid: The assetUid of the sensor you want to get the data from.
            start_time: the start timestamp
            end_time: the end timestamp
            eventtype: type of env data you want: Temperature ("TEMPERATURE"), Humidity ("HUMIDITY") or Pressure ("PRESSURE")

        Returns: JSON formatted string.

        """
        headers = self._get_header(constants.environmental_zone)

        response = requests.request(constants.GET,
                                    f'{constants.event_service_api}/{assetUid}/events?eventType={eventtype}&startTime={start_time}&endTime={end_time}',
                                    headers=headers)

        return response.json()
