import unittest
import app as flask_app
from shared_test_setup import BlogTestCase


class TestBlogApp(BlogTestCase):
    def setUp(self):
        super().setUp()

        flask_app.app.config['TESTING'] = True
        self.client = flask_app.app.test_client()
        flask_app.database = self.database

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        html_text = response.data.decode('utf-8')
        self.assertIn("Norge", html_text)

    def test_new_post_form_loads(self):
        response = self.client.get('/posts/new')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()