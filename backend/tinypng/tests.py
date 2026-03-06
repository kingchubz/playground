from datetime import datetime, timedelta

from django.utils import timezone
from django.test import TestCase, Client


class TestDatetime(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/time/'

    def test_time_returns_200(self):
        """
        curr_date() response status code = 200
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_time_wrong_url(self):
        """
        curr_date() response status code = 404
        """

        response = self.client.get('/api/a') # wrong url
        self.assertEqual(response.status_code, 404)

    def test_time_is_correct(self):
        """
        curr_date() returns correct time within 1 second.
        """

        response = self.client.get(self.url)
        data = response.json()
        self.assertIn('datetime', data)

        curr_datetime = datetime.fromisoformat(data['datetime'])
        diff = timezone.now() - curr_datetime
        self.assertTrue(diff <= timedelta(seconds=1))