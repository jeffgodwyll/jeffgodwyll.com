import unittest

from google.appengine.api import testbed

from main import app


class MainAppTest(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.app = app.test_client()

    def tearDown(self):
        self.testbed.deactivate()

    def testAbout(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
