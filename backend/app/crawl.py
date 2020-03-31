import requests
from bs4 import BeautifulSoup
import csv
import sys
import importlib


def crawl_cotent():
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie' : 't=MHpOYzlnMmp6dkFJTEVmS3pDeldrSWRTazlBOXpkRjBzRXpZOU4yVkNZWWl5QVhMVXBjMU5WcnpwQ2NCQS90ZkVsZ3lTU2Z0T3puVVZFWFRFOXR1TnVrbUV2UFlsQWxuemY4NG1wWFRYMENVdDRPQ1psK0NFZGJDZ0lsN3BQZmo%3D; s=Njg4NDkxLCwxNTQyMTk0MTEzMDI5LCxodHRwczovL3N0YXRpYy53b3NoaXBtLmNvbS9XWF9VXzIwMTgwNV8yMDE4MDUyMjE2MTcxN180OTQ0LmpwZz9pbWFnZVZpZXcyLzIvdy84MCwsJUU1JUE0JUE3JUU4JTk5JUJF; Hm_lvt_b85cbcc76e92e3fd79be8f2fed0f504f=1547467553,1547544101,1547874937,1547952696; Hm_lpvt_b85cbcc76e92e3fd79be8f2fed0f504f=1547953708'
    }

    with open('../data.csv', 'a', encoding='utf-8',newline='') as csvfile:
        fieldnames = ['title', 'author', 'author_des', 'date', 'views', 'loves', 'zans', 'comment_num','url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for page_number in range(3, 5):
            page_url = "http://www.woshipm.com/category/pmd/page/{}".format(str(page_number))
            #print('url:'+page_url)
            print('正在抓取第' + str(page_number) + '页>>>')
            response = requests.get(url=page_url, headers=headers)
            #print('请求结果：' + str(response.status_code))
            if response.status_code == 200:
                page_data = response.text
                #print('page_data:{}'.format(page_data))
                if page_data:
                    soup = BeautifulSoup(page_data, 'html.parser')
                    article_urls = soup.find_all("h2", class_="post-title")
                    #print('article_urls:{}'.format(article_urls))
                    for item in article_urls:
                            url = item.find('a').get('href')
                            # 文章页面解析，获取文章标题、作者、作者简介、日期、浏览量、收藏量、点赞量、评论量、正文、文章链接
                            response = requests.get(url=url, headers=headers)
                            # time.sleep(3)
                            print('正在抓取：' + url)
                            # print(response.status_code)
                            if response.status_code == 200:
                                article = response.text
                                #print(article)
                            if article:
                                try:
                                    soup = BeautifulSoup(article, 'html.parser')
                                    #print(soup)
                                    # 文章标题
                                    title = soup.find(class_='article-title').get_text().strip()
                                    # 作者
                                    author = soup.find(class_='post-meta-items').find_previous_siblings()[1].find('a').get_text().strip()
                                    # 作者简介
                                    author_des = soup.find(class_='post-meta-items').find_previous_siblings()[0].get_text().strip()
                                    # 日期
                                    date = soup.find(class_='post-meta-items').find_all(class_='post-meta-item')[0].get_text().strip()
                                    # 浏览量
                                    views = soup.find(class_='post-meta-items').find_all(class_='post-meta-item')[1].get_text().strip()
                                    # 收藏量
                                    loves = soup.find(class_='post-meta-items').find_all(class_='post-meta-item')[2].get_text().strip()
                                    # 点赞量
                                    zans = soup.find(class_='post-meta-items').find_all(class_='post-meta-item')[3].get_text().strip()
                                    # 评论量
                                    comment = soup.find('ol', class_="comment-list").find_all('li')
                                    comment_num = len(comment)
                                    # 正文
                                    #art = soup.find(class_="grap").get_text().strip()
                                    writer.writerow({'title':title, 'author':author, 'author_des':author_des, 'date':date, 'views':views, 'loves':int(loves), 'zans':int(zans), 'comment_num':int(comment_num), 'url':url})
                                    print({'title':title, 'author':author, 'author_des':author_des, 'date':date, 'views':views, 'loves':loves, 'zans':zans, 'comment_num':comment_num})
                                    print("写入成功----------------")
                                except:
                                    print('抓取失败')
                                    print("抓取完毕！")
