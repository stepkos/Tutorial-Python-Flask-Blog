import json
from flaskblog import db
from flaskblog.models import Post


# REQUIRED 3 USERS with id 1, 2, 3

posts = json.load(open('flaskblog/seed/posts.json'))

for post in posts:
    db.session.add(Post(title=post['title'], content=post['content'], user_id=post['user_id']))
    db.session.commit()