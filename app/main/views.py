from flask import request,render_template, session, redirect, \
    url_for, flash, current_app,make_response

from . import main
#from .forms import NameForm, EditProfileForm,EditProfileAdminForm,PostForm,CommentForm
from .. import db
from ..models import Content
from flask_login import login_required, current_user

def num(n):
    print(n)
    if n[len(n)-1] == '万':

        return float(n[0:len(n)-1])*10000
    else:
        return int(n)

def csv_to_mysql(i):
    title = i[0]
    author = i[1]
    author_des = i[2]
    date = i[3]
    views = num(i[4])
    loves = num(i[5])
    zans = num(i[6])
    comment_num = num(i[7])
    #art = i[8]
    url = i[8]
    content = Content(title=title,author=author,author_des=author_des,date=date,views=views, \
                loves=loves,zans=zans,comment_num=comment_num,url=url)
    db.session.add(content)


@main.before_app_first_request
def before_app_request():
    file = open('./data.csv','r').readlines()
    for f in file:

        f = f.split(',')
        
        
        if len(f) ==9 and f[0] != 'title': 
            print(f)
            csv_to_mysql(f)
        elif len(f) > 9 and f[0] != 'title': 
            print('f[0:4]:{}'.format(f[0:3]))
            print('f[-6:-1]:{}'.format(f[-6:]))

            f_9 = f[0:3]+f[-6:]
            print("if len(f) > 9:{}",format(f_9))
            csv_to_mysql(f_9)


@main.route('/')
def index():
    json = {
        "product":"product_board",
        "product manager":"Sky"
    }
    response = make_response(json)
    return "Hello Product Manager"