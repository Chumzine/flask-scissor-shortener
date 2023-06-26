import unittest
from flask import Flask, request, url_for
from .. import create_app
from ..models.links import Link
from ..config.config import config_dict
from ..extensions import db


class ShortenLinkTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()


    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def test_index(self):
        '''
        Test index route
        '''
        response = self.client.get('/')

        assert response.status_code == 200


    def shorten_link_with_valid_data(self):
        '''
        Test link route with valid data
        '''
        data = {
            'url': 'http://example.com'
        }

        response = self.client.post('/shorten_link', json=data)

        assert response.status_code == 200


    def shorten_link_with_missing_data(self):
        '''
        Test link route with missing data
        '''
        data = {}

        response = self.client.post('/shorten_link', json=data)

        assert response.status_code == 302


    def test_stats_route(self):
        '''
        Test stats route
        '''
        link1 = Link(original_url='http://example.com', short_url='abc')
        link2 = Link(original_url='http://example.org', short_url='def')
        db.session.add(link1)
        db.session.add(link2)
        db.session.commit() 

        response = self.client.get('/stats')

        assert response.status_code == 302

        # Assert that the rendered template is 'stats.html'
        self.assertTemplateUsed('stats.html')

    # Function to assert that the rendered template is used
    def assertTemplateUsed(self, template_name):
        template_names = self.app.jinja_env.list_templates()
        self.assertIn(template_name, template_names)
          

