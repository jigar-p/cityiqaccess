from cityiqaccess import constants
import requests


class Parking:

    def __init__(self, token):
        self.token = token

    def _get_header(self, zone):
        """
        Creates the header to pass in with the requests.
        :param zone: The Zone ID of the city
        :return: Header in the form of a dict
        """
        return {'Authorization': 'Bearer ' + self.token, 'Predix-Zone-Id': zone}

    def get_parking_events_by_location(self, eventtype, starttime, endtime, bbox):
        """

        Args:
            eventtype:
            starttime:
            endtime:
            bbox:

        Returns:

        """
        headers = self._get_header(constants.parking_zone)
        response = requests.request(constants.GET,
                                    f'{constants.parking_api}/events?bbox={bbox}&locationType=PARKING_ZONE&eventType={eventtype}&startTime={starttime}&endTime={endtime}',
                                    headers=headers)
        return response.json()

    def get_parking_metadata(self, bbox=constants.default_bbox):
        """

        Args:
            bbox:

        Returns:

        """
        headers = self._get_header(constants.parking_zone)
        response = requests.request(constants.GET,
                                    f'{constants.metadata_api}/search?Q=locationType:PARKING_ZONE&bbox={bbox}',
                                    headers=headers)
        return response.json()

    def get_parking_events_by_locationuid(self, locationid, eventtype, starttime, endtime):
        """

        Args:
            locationid:
            eventtype:
            starttime:
            endtime:

        Returns:

        """
        headers = self._get_header(constants.parking_zone)
        response = requests.request(constants.GET,
                                    f'{constants.parking_api}/{locationid}/events?eventType={eventtype}&startTime={starttime}&endTime={endtime}',
                                    headers=headers)
        return response.json()

    def get_parking_events_by_assetuid(self, assetuid, eventtype, starttime, endtime):
        """

        Args:
            assetuid:
            eventtype:
            starttime:
            endtime:

        Returns:

        """
        headers = self._get_header(constants.parking_zone)
        response = requests.request(constants.GET,
                                    f'{constants.parking_asset_api}/{assetuid}/events?eventType={eventtype}&startTime={starttime}&endTime={endtime}',
                                    headers=headers)
        return response.json()
