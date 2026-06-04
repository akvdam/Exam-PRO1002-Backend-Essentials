import unittest
from database import BlogDatabase


class BlogTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = BlogDatabase(':memory:')

        with open("blogposts.sql", "r") as file:
            sql_script = file.read()
        cursor = cls.database.cursor()
        cursor.executescript(sql_script)

    @classmethod
    def tearDownClass(cls):
        cls.database.close()

    def setUp(self):
        self.database = self.__class__.database
        self.database.cursor().execute('BEGIN TRANSACTION')

    def tearDown(self):
        self.database.cursor().execute('ROLLBACK')