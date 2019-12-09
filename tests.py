import unittest
import json
import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from application import *

app = create_app()
app.config.from_object('config.Config')

class TestPlacesAPI(unittest.TestCase):
    
    # Setup for tests...
    def setUp(self):
        """
            This method is run before each test.
            Database setup, if any, must be done here.
        """
        self.client = app.test_client()  # Get the flask test client
        app.testing = True


    def tearDown(self):
        """
            Destroy temporary setup done for tests.
            This is called after each test
        """
        pass


    def test_get_root(self):
        response = self.client.get('/')

        # We respond with 405 for any routes other than /places
        self.assertEqual(response.status_code, 405)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data["message"], "Method Not Allowed")


    def test_here_api_lookup(self):
        query_string = {
            "at": "13.0563101,77.5951032",
            "q": "Godrej+Woodsman+Estate",
        }

        response = self.client.get('/places', query_string=query_string)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
