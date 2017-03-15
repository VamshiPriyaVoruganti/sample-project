# from math import sqrt
# from celery import Celery
# from __future__ import absolute_import
# app = Celery('tasks', broker='redis://127.0.0.1:6379/0')
# app.config.CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# @app.task
# def square_root(value):
# 	return sqrt(value)



# @app.task
# def fibo_task():
# 	a, b = 0,1
# 	for item in range(4):
# 		a, b = b, a + b
# 	print(a)



# if __name__ == "__main__":
# 	square_root()
# 	fibo_task()
# import re
# import requests
# from bs4 import BeautifulSoup
from math import sqrt
from celery import Celery


app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@app.task
def square_root(value):
	return sqrt(value)



@app.task
def add(x, y):
    return x + y


@app.task
def fibo_task(value):
	a, b = 0,1
	for item in range(value):
		a, b = b, a + b
	message = "The Fibonacci calculated with task id %s" \
	" was %d" % (fibo_task.request.id, a)
	return (value, message)

# @app.task
# def trade_spider():
#         url = 'https://www.cardekho.com/photo-gallery.htm'
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#         for link in soup.findAll('a', {'href': re.compile("photoGallery")}):
#             href = link.get('href')
#             title = link.string
#             print(title)
#             get_single_item_data(href)

# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, "html.parser")
#     for link in soup.findAll('a', {'href': re.compile("pictures")}):
#         href = link.get('href')
#         title = link.string
#         print(href)