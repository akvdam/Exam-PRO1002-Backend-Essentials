from flask import Flask, g, render_template, request, redirect, url_for
from datetime import date
from database import BlogDatabase

app = Flask('Norge til VM', static_folder='static')
database = None


@app.before_request
def load_db():
    global database
    if 'database' in globals() and database is not None:
        g.db = database
    else:
        g.db = BlogDatabase()


@app.route("/")
def index():
    raw_posts = g.db.get_all_posts()
    posts = []
    for post in raw_posts:
        p = dict(post)
        p['excerpt'] = post['body'].split('\n\n')[0][:150]
        p['tags'] = g.db.get_tags_for_post(post['id'])
        posts.append(p)

    response = render_template('main.html', posts=posts)
    return response


@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def show_post(id):
    error = None
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()

        if not title or not content:
            error = "Både tittel og kommentar må fylles ut!"
        else:
            g.db.add_comment(id, title, str(date.today()), content)
            return redirect(url_for('show_post', id=id))

    post = g.db.get_post(id)
    p = dict(post)
    p['tags'] = g.db.get_tags_for_post(id)

    response = render_template('post.html',
                               post=p,
                               comments=g.db.get_comments_for_post(id),
                               error=error)
    return response


@app.route('/posts/new')
def new_post():
    response = render_template('post-form.html',
                               post={},
                               tags_string="")
    return response


@app.route('/posts/<int:id>/edit')
def edit_post(id):
    post = g.db.get_post(id)
    tags_list = g.db.get_tags_for_post(id)
    tags_string = ", ".join(tags_list)

    response = render_template('post-form.html',
                               post=post,
                               tags_string=tags_string)
    return response


@app.route('/post/save', methods=['POST'])
def save_post():
    post_form = request.form
    id = post_form['id']

    if id == '':
        id = g.db.add_post(post_form['title'], str(date.today()), post_form['body'])
    else:
        g.db.update_post(int(id), post_form['title'], str(date.today()), post_form['body'])

    _set_tags(g, int(id), post_form)
    return redirect(url_for('show_post', id=id))


@app.route('/tags/<string:name>')
def show_tag(name):
    raw_posts = g.db.get_posts_by_tag(name)
    posts = []
    for post in raw_posts:
        p = dict(post)
        p['excerpt'] = post['body'].split('\n\n')[0][:150]
        p['tags'] = g.db.get_tags_for_post(post['id'])
        posts.append(p)

    response = render_template('tag.html', tag_name=name, posts=posts)
    return response


def _set_tags(g, id, form):
    g.db.clear_tags_for_post(id)
    tag_input = form.get('tags', '')
    if tag_input:
        for tag in tag_input.split(','):
            if tag.strip():
                g.db.add_tag_to_post(id, tag.strip().lower())

if __name__ == '__main__':
    app.run(port=5001, debug=True)