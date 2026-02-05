import unittest
import requests
from unittest.mock import patch, MagicMock


class WebServer:
    """getting data from a website
    """
    def get_data(self, url: str) -> dict:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"HTTP Error: {response.status_code}")


class WebServerTest(unittest.TestCase):

    @patch('requests.get')
    def test_get_data(self, mock_get):
        fake_responce = MagicMock()
        fake_responce.status_code = 200
        fake_responce.json.return_value = {"data": "test"}
        mock_get.return_value = fake_responce

        ws = WebServer()
        result = ws.get_data("https://weather.com/home-garden/video/when-should-you-shovel-snow-during-winter-storm")

        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_data_not_found(self, mock_get):
        fake_responce = MagicMock()
        fake_responce.status_code = 404

        mock_get.return_value = fake_responce
        ws = WebServer()
        with self.assertRaises(Exception) as context:
            ws.get_data("https://weather.com")
        self.assertIn("404", str(context.exception))

        mock_get.assert_called_once()

    @patch('requests.get')
    def test_fet_data_server_error(self, mock_get):
        fake_responce = MagicMock()
        fake_responce.status_code = 500
        mock_get.return_value = fake_responce
        ws = WebServer()
        with self.assertRaises(Exception) as context:
            ws.get_data("https://weather.om")
        self.assertIn("HTTP Error", str(context.exception))
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
