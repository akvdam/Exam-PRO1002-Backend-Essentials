import unittest
import app as flask_app
from database import BlogDatabase


class TestBlogApp(unittest.TestCase):
    def setUp(self):
        flask_app.app.config['TESTING'] = True
        self.client = flask_app.app.test_client()

        self.test_db = BlogDatabase(':memory:')
        cur = self.test_db.cursor()
        cur.execute('CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, publication_date TEXT, body TEXT)')
        cur.execute('CREATE TABLE tags (post_id INTEGER, name TEXT)')
        cur.execute(
            'CREATE TABLE comments (id INTEGER PRIMARY KEY, post_id INTEGER, title TEXT, publication_date TEXT, content TEXT)')

        self.test_db.add_post("VM Drømmen", "2026-06-04", "Innhold her.")
        flask_app.database = self.test_db

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        html_text = response.data.decode('utf-8')
        self.assertIn("VM Drømmen", html_text)

    def test_new_post_form_loads(self):
        response = self.client.get('/posts/new')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()