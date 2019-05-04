from cityiq import CityIQ
import constants
import unittest


class TestENV(unittest.TestCase):

    def setUp(self):
        self.city = CityIQ()
        self.start_time = 1548867600000
        self.end_time = 1548871200000

    def test_temperature_by_assetuid(self):
        """
        Tests if you can get the temperature data by assetuid.
        """
        assetuid = '1ec8a25b-fb17-4242-ab6c-1aeed5c32e59'
        run_method = self.city.get_temperature_by_assetuid(assetuid, self.start_time, self.end_time)

        self.assertGreater(len(run_method['content']), 0)

    def test_humidity_by_assetuid(self):
        """
        Tests if you can get the humidity data by assetuid.
        """
        assetuid = '1ec8a25b-fb17-4242-ab6c-1aeed5c32e59'
        run_method = self.city.get_humidity_by_assetuid(assetuid, self.start_time, self.end_time)

        self.assertGreater(len(run_method['content']), 0)

    def test_pressure_by_assetuid(self):
        """
        Tests if you can get the pressure data by assetuid.
        """
        assetuid = '1ec8a25b-fb17-4242-ab6c-1aeed5c32e59'
        run_method = self.city.get_pressure_by_assetuid(assetuid, self.start_time, self.end_time)

        self.assertGreater(len(run_method['content']), 0)

    def test_temperature_by_bbox(self):
        """
        Tests if you can get the temperature data by bbox.
        """
        run_method = self.city.get_temperature_metadata_by_bbox(
            constants.sddt_bbox)
        run_result = run_method['content'][0]['assetUid']

        self.assertEqual(run_result, '00460a52-d112-4ec5-b754-fb690b9f180e')

    def test_humidity_by_bbox(self):
        """
        Tests if you can get the humidity data by bbox.
        """
        run_method = self.city.get_humidity_metadata_by_bbox(
            constants.sddt_bbox)
        run_result = run_method['content'][0]['assetUid']

        self.assertEqual(run_result, '00460a52-d112-4ec5-b754-fb690b9f180e')

    def test_pressure_by_bbox(self):
        """
        Tests if you can get the pressure data by bbox.
        """
        run_method = self.city.get_pressure_metadata_by_bbox(
            constants.sddt_bbox)
        run_result = run_method['content'][0]['assetUid']

        self.assertEqual(run_result, '00460a52-d112-4ec5-b754-fb690b9f180e')


if __name__ == '__main__':
    unittest.main()
