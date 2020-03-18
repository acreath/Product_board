from flask import request,render_template, session, redirect, \
    url_for, flash, current_app,make_response

from . import main
#from .forms import NameForm, EditProfileForm,EditProfileAdminForm,PostForm,CommentForm
from .. import db
from ..models import Content
from flask_login import login_required, current_user
from ..csv2mysql import csv_to_mysql,num
from bs4 import BeautifulSoup
import csv
from ..crawl import crawl_cotent 
      


@main.before_app_first_request
def before_app_request():
    print('before_app_first_request')
    crawl_cotent()
    csv_to_mysql()
    
    print('commit')
    


    


@main.route('/', methods=['GET'])
def index():
    
    #contents = Content.query.filter(Content.views > 2000).all()
    page = request.args.get('page', 1, type=int)
    pagination = Content.query.filter(Content.views > 500,Content.loves > 100).paginate(
            page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
             error_out=False)
    contents = pagination.items
    
    return render_template('index.html', contents=contents, pagination=pagination)
   