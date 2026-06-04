import unittest
import sqlite3
from database import BlogDatabase


class TestBlogDatabase(unittest.TestCase):
    def setUp(self):

        self.db = BlogDatabase(':memory:')
        cur = self.db.cursor()
        # Create minimal schemas to verify queries against
        cur.execute('CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, publication_date TEXT, body TEXT)')
        cur.execute('CREATE TABLE tags (post_id INTEGER, name TEXT)')
        cur.execute(
            'CREATE TABLE comments (id INTEGER PRIMARY KEY, post_id INTEGER, title TEXT, publication_date TEXT, content TEXT)')

    def tearDown(self):
        self.db.close()

    def test_add_and_get_post(self):
        post_id = self.db.add_post("Test Tittel", "2026-06-04", "Dette er testinnhold.")
        self.assertEqual(post_id, 1)

        post = self.db.get_post(1)
        self.assertIsNotNone(post)
        self.assertEqual(post['title'], "Test Tittel")

    def test_add_tags(self):
        self.db.add_tag_to_post(1, "taktikk")
        tags = self.db.get_tags_for_post(1)
        self.assertIn("taktikk", tags)


if __name__ == '__main__':
    unittest.main()