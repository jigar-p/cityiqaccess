from cityiq import CityIQ
import constants
import time
import unittest

class TestParking(unittest.TestCase):

    def setUp(self):
        self.city = CityIQ()
        self.start_time = 1548867600000
        self.end_time = 1548871200000


    def test_open_parking_locationuid(self):

        location_id = 'dvi25bk0tcfjk01npf9'
        run_method = self.city.get_open_parking_spots_by_locationuid(location_id,self.start_time,self.end_time)
        run_result = run_method['content'][0]['assetUid']
        self.assertEqual(run_result,'44e74476-a149-473f-9733-5cac565a410d')


    def test_occupied_parking_locationuid(self):

        location_id = 'dvi25bk0tcfjk01npf9'
        run_method = self.city.get_occupied_parking_spots_by_locationuid(location_id,self.start_time,self.end_time)
        run_result = run_method['content'][0]['assetUid']
        self.assertEqual(run_result,'daab92c2-ed35-4171-85fb-feb1de55efde')


    def test_open_parking_assetuid(self):

        assetuid = '44e74476-a149-473f-9733-5cac565a410d'
        run_method = self.city.get_open_parking_spots_by_assetuid(assetuid,self.start_time,self.end_time)
        run_result = run_method['content'][0]['locationUid']
        self.assertEqual(run_result,'dvi25bk0tcfjk01npf9')


    def test_occupied_parking_assetuid(self):

        assetuid = 'daab92c2-ed35-4171-85fb-feb1de55efde'
        run_method = self.city.get_occupied_parking_spots_by_assetuid(assetuid,self.start_time,self.end_time)
        run_result = run_method['content'][0]['locationUid']
        self.assertEqual(run_result,'e51c93gjizpjk01n3pi')



if __name__ == '__main__':
    unittest.main()
