import unittest
from src.recommendation import get_recommendation_data, update_recommendation_data, delete_recommendation_data
from src.database.recommendation_data import recommendation_data

class TestRecommendation(unittest.TestCase):

    def setUp(self):
        self.recommendation_data = recommendation_data

    def test_get_recommendation_data(self):
        result = get_recommendation_data()
        self.assertEqual(result, self.recommendation_data)

    def test_update_recommendation_data(self):
        new_data = {"college": "Test College", "likelihood": 0.8}
        update_recommendation_data(new_data)
        self.assertIn(new_data, self.recommendation_data)

    def test_delete_recommendation_data(self):
        data_to_delete = {"college": "Test College", "likelihood": 0.8}
        delete_recommendation_data(data_to_delete)
        self.assertNotIn(data_to_delete, self.recommendation_data)

if __name__ == '__main__':
    unittest.main()