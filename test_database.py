import unittest
from shared_test_setup import BlogTestCase


class TestBlogDatabase(BlogTestCase):
    def test_add_and_get_post(self):
        post_id = self.database.add_post("Ny VM Tittel", "2026-06-04", "Innhold tekst.")

        post = self.database.get_post(post_id)
        self.assertIsNotNone(post)
        self.assertEqual(post['title'], "Ny VM Tittel")

    def test_add_tags(self):
        self.database.add_tag_to_post(1, "taktikk")
        tags = self.database.get_tags_for_post(1)
        self.assertIn("taktikk", tags)


if __name__ == '__main__':
    unittest.main()