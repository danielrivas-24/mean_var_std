import unittest
import demographic_data_analyzer
class TestDemographicData(unittest.TestCase):
    def test_calculate_demographic_data(self):
        result = demographic_data_analyzer.calculate_demographic_data(print_data=False)
        self.assertIsInstance(result, dict)
        self.assertIn('average_age_men', result)

if __name__ == '__main__':
    unittest.main()