import os
import unittest
from metadata.election import Election, Request

class TestElection(unittest.TestCase):
    def test_request_url_with_start_date(self):
        url = "http://openelections.net/api/v1/election/?format=json&state__postal=LA&start_date__gte=2014-01-01&offset=0"
        r = Request('LA', '2014-01-01')
        self.assertEqual(r.url, url)

    def test_request_url_with_start_date_end_date(self):
        url = "http://openelections.net/api/v1/election/?format=json&state__postal=LA&start_date__gte=2014-01-01&end_date__lte=2014-12-31&offset=0"
        r = Request('LA', '2014-01-01', '2014-12-31')
        self.assertEqual(r.url, url)

    def test_request_url_with_offset(self):
        url = "http://openelections.net/api/v1/election/?format=json&state__postal=LA&start_date__gte=2002-01-01&offset=20"
        r = Request('LA', '2002-01-01', None, 20)
        self.assertEqual(r.url, url)

    def test_election_generated_filename(self):
        r = Request('LA', '2014-01-01')
        elections = r.parse()
        self.assertEqual(elections[0].generated_filename(), '20141206__la__general.csv')
