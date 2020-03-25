from flask import request,render_template, session, redirect, \
    url_for, flash, current_app,make_response,jsonify

from . import main
from .. import db
from ..models import Content
from flask_login import login_required, current_user
from ..csv2mysql import csv_to_mysql,num
from bs4 import BeautifulSoup
import csv
from ..crawl import crawl_cotent 
from flask_cors import CORS

# CORS(main)

@main.route('/', methods=['GET'])
def index():
    #crawl_cotent()
    #csv_to_mysql()
    contents_json_list = []
    contents = Content.query.filter(Content.views > 500,Content.loves > 100).all()
    for item in contents:
        print(item.to_json())
        contents_json_list.append(item.to_json())
    contents_dic = jsonify({"list":contents_json_list})
    # page = request.args.get('page', 1, type=int)
    # pagination = Content.query.filter(Content.views > 500,Content.loves > 100).paginate(
    #         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #          error_out=False)
    # contents = pagination.items
    
    return contents_dic
   