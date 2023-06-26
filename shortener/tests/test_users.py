import unittest
from .. import create_app
from ..config.config import config_dict
from ..extensions import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import logout_user


class UserTestCase(unittest.TestCase):
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


    def test_user_registration(self):
        '''
        Test user registration
        '''
        data = {
            'firstname': 'testa',
            'lastname': 'teston',
            'username': 'test',
            'email': 'testuser@gmail.com',
            'password': 'password'
        }

        response = self.client.post('/register', json=data)

        assert response.status_code == 200


    def test_user_login(self):
        '''
        Test user login
        '''
        data = {
            'username': 'test',
            'password': 'password'
        }

        response = self.client.post('/login', json=data)

        assert response.status_code == 200


    def test_user_logout(self):
        '''
        Test user logout
        '''
        response = self.client.post('/logout')

        assert response.status_code == 302




