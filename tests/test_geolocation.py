import unittest

from geolocation import GeoLocation


class TestGeoLocation(unittest.TestCase):
    def test_deg_to_rad(self):
        # Test degree to radian conversion
        loc1 = GeoLocation.from_degrees(26.062951, -80.238853)
        loc2 = GeoLocation.from_radians(loc1.rad_lat, loc1.rad_lon)
        assert (loc1.rad_lat == loc2.rad_lat and loc1.rad_lon == loc2.rad_lon
                and loc1.deg_lat == loc2.deg_lat and loc1.deg_lon == loc2.deg_lon)

    def test_distance(self):
        # Test distance between two locations
        loc1 = GeoLocation.from_degrees(26.062951, -80.238853)
        loc2 = GeoLocation.from_degrees(26.060484, -80.207268)
        assert loc1.distance_to(loc2) == loc2.distance_to(loc1)

    def test_eq(self):
        loc = GeoLocation.from_degrees(26.062951, -80.238853)
        loc2 = GeoLocation.from_degrees(26.062951, -80.238853)
        assert loc == loc2

    def test_init_invalid(self):
        self.assertRaises(ValueError,
                          GeoLocation.from_radians, 4, 4)

    def test_bounding_locations_invalid_radius(self):
        loc = GeoLocation.from_degrees(0, 0)
        self.assertRaises(ValueError, loc.bounding_locations, -1)

    def test_bounding_locations_invalid_distance(self):
        loc = GeoLocation.from_degrees(0, 0)
        self.assertRaises(ValueError, loc.bounding_locations, 100, -5)

if __name__ == '__main__':
    unittest.main()