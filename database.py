import sqlite3

class BlogDatabase:
    def __init__(self, database_path='blog.db'):
        self.connection = sqlite3.connect(database_path, isolation_level=None)
        self.connection.row_factory = sqlite3.Row

    def cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()


            # Methods for posting on the blog

    def get_all_posts(self):
        cur = self.cursor()
        # Requirement: Order by dates, newest first
        cur.execute('SELECT * FROM posts ORDER BY publication_date DESC')
        return cur.fetchall()

    def get_post(self, post_id):
        cur = self.cursor()
        cur.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
        return cur.fetchone()

    def add_post(self, title, publication_date, body):
        cur = self.cursor()
        cur.execute('INSERT INTO posts (title, publication_date, body) VALUES (?, ?, ?)',
                    (title, publication_date, body))
        return cur.lastrowid

    def update_post(self, post_id, title, publication_date, body):
        cur = self.cursor()
        cur.execute('UPDATE posts SET title = ?, publication_date = ?, body = ? WHERE id = ?',
                    (title, publication_date, body, post_id))


                # Methods for commenting on the blog

    def get_comments_for_post(self, post_id):
        cur = self.cursor()
        cur.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY publication_date DESC',
                    (post_id,))
        return cur.fetchall()

    def add_comment(self, post_id, title, publication_date, content):
        cur = self.cursor()
        cur.execute('INSERT INTO comments (post_id, title, publication_date, content) VALUES (?, ?, ?, ?)',
                    (post_id, title, publication_date, content))
        return cur.lastrowid


                # Methods for using the tag function on the blog

    def get_tags_for_post(self, post_id):
        cur = self.cursor()
        cur.execute('SELECT name FROM tags WHERE post_id = ?', (post_id,))
        return [row['name'] for row in cur.fetchall()]

    def add_tag_to_post(self, post_id, tag_name):
        cur = self.cursor()
        cur.execute('INSERT OR IGNORE INTO tags (post_id, name) VALUES (?, ?)',
                    (post_id, tag_name.strip()))

    def clear_tags_for_post(self, post_id):
        cur = self.cursor()
        cur.execute('DELETE FROM tags WHERE post_id = ?', (post_id,))

    def get_posts_by_tag(self, tag_name):
        cur = self.cursor()
        cur.execute('''
            SELECT p.* FROM posts p 
            JOIN tags t ON p.id = t.post_id 
            WHERE t.name = ? 
            ORDER BY p.publication_date DESC
        ''', (tag_name,))
        return cur.fetchall()