from flask import request,render_template, session, redirect, \
    url_for, flash, current_app,make_response

from . import main
#from .forms import NameForm, EditProfileForm,EditProfileAdminForm,PostForm,CommentForm
from .. import db
from ..models import Content
from flask_login import login_required, current_user
from ..csv2mysql import csv_to_mysql,num

      


@main.before_app_first_request
def before_app_request():
    print('before_app_first_request')
    
    csv_to_mysql()
    
    print('commit')
    

    


@main.route('/')
def index():
    json = {
        "product":"product_board",
        "product manager":"Sky"
    }
    response = make_response(json)
    return "Hello Product Manager"