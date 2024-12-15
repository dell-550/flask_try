import unittest
import json
# import re
# from base64 import b64encode
from app import create_app, db
# from app.models import User, Role, Post, Comment


class TestUser(unittest.TestCase):
    def setUp(self):
        print("setUp  test")
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # Role.insert_roles()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        print("tearDown  test")

    def test_add_user(self):
        response = self.client.post(
            '/api/v1/adduser/',
            data=json.dumps({
                'username': 'john',
                'password': 'cat',
                'email': "12414"
           }),
            content_type='application/json'
        )
        print(f"results {response}")
        self.assertEqual(response.status_code, 200)