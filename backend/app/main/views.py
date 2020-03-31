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

@main.route('/<page>', methods=['GET'])
def index(page):
    
    contents_json_list = []
    #求分页的页数
    contents = Content.query.filter(Content.views > 200,Content.loves > 10).all()
    num_page = list(range(1,int(len(contents)/10) + 2))
    
    #获取请求的当前页数内容
    page=int(page)
    pagination = Content.query.filter(Content.views > 200,Content.loves > 10).paginate(
             page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
              error_out=False)
    
    for item in pagination.items:
        
        contents_json_list.append(item.to_json())

    contents_dic = jsonify({"list":contents_json_list,"num_page":num_page})

    return contents_dic
   