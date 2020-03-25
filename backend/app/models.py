from . import db
import pylint_flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_required, AnonymousUserMixin
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 
from flask import current_app
from datetime import datetime
import hashlib
from flask import request, url_for
from markdown import markdown
import bleach


#'title':title, 'author':author, 'author_des':author_des, 'date':date, 
# 'views':views, 'loves':loves, 'zans':zans, 'comment_num':comment_num}
class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True, nullable=False)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64),index=True)
    author_des = db.Column(db.Text)
    date = db.Column(db.String(64))
    views = db.Column(db.Integer)
    loves = db.Column(db.Integer)
    zans = db.Column(db.Integer)
    comment_num = db.Column(db.Integer)
    #art = db.Column(db.Text)
    url = db.Column(db.String(64))

    def to_json(self):
        json_post = {
        'title': self.title, 
        'author': self.author,
        'author_des': self.author_des,
        'date': self.date,
        'views': self.views,
        'loves': self.loves,
        'zans': self.zans,
        'comment_num': self.comment_num,
        'url': self.url
        }
        return json_post