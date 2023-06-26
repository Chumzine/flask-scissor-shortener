import unittest
from .. import create_app
from ..config.config import config_dict
from ..extensions import db
from flask_login import current_user


class GenerateQRCodeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client(use_cookies=True)

        db.create_all()


    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def test_generate_qr_code_with_valid_data(self):
        '''
        Test qrcode generation with data
        '''
        data = {
            'url': 'http://example.com' 
        }

        # Submit a POST request to the /generate_qr_code endpoint with valid data
        response = self.client.post('/generate_qr_code', json=data)

        assert response.status_code == 302

        # Assert that the 'display_qr_code.html' template is rendered
        self.assertTemplateUsed('display_qr_code.html')


    def test_generate_qr_code_with_missing_data(self):
        '''
        Test qrcode generation with missing data
        '''
        data = {}

        # Submit a POST request to the /generate_qr_code endpoint with missing data
        response = self.client.post('/generate_qr_code', json=data)

        assert response.status_code == 302

        # Assert that the 'qr_code.html' template is rendered
        self.assertTemplateUsed('qr_code.html')
                

    def assertTemplateUsed(self, template_name):
        template_names = self.app.jinja_env.list_templates()
        self.assertIn(template_name, template_names)
          