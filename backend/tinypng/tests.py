from datetime import datetime, timedelta
import json
import os

from django.test import TestCase, Client

client = Client()

class DatetimeTest(TestCase):
    def test_time_is_correct(self):
        """
        curr_date() returns correct time within 1 second.
        """
        allowed_hosts = os.environ['ALLOWED_HOSTS'].split('|')

        for host in allowed_hosts:
            response = client.get('/api/time/', headers={'Host': host})
            self.assertEqual(response.status_code, 200)

            curr_date_dict = json.loads(response.getvalue())
            curr_datetime = datetime.strptime(curr_date_dict['datetime'], '%a %d %b %Y %H:%M:%S')
            diff = datetime.now() - curr_datetime
            self.assertIs(diff <= timedelta(seconds=1), True)