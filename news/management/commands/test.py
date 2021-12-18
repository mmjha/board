from news.models import News
from bs4 import BeautifulSoup
from urllib import parse
from collections import OrderedDict
import requests, os, datetime

from django.core.management.base import BaseCommand
# https://www.boannews.com/robots.txt

class Command(BaseCommand):
	help = 'news insert'

	def handle(self, *args, **kwargs):
		self.hello_every_news()

	def hello_every_news(self):
		search = parse.urlparse(
			'https://www.boannews.com/search/news_list.asp?search=title&find=보안')
		
		query = parse.parse_qs(search.query)
		s_query = parse.urlencode(query, encoding='euc-kr', doseq = True)
		url = 'https://www.boannews.com/search/news_list.asp?{}'.format(s_query)
		self.article_crawll(url)
	
	def article_crawll(self, url):
		news_link = []
		response = requests.get(url)
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		
		for link in soup.find_all('a', href=True):
			notices_link = link['href']
			if '/media/view.asp?idx=' in notices_link:
				news_link.append(notices_link)
	
		news_link = list(OrderedDict.fromkeys(news_link))
		self.compare(news_link)
		#maintext_crawll(news_link, 0)
			
	
	def compare(self, news_link):
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		temp = []
		cnt = 0
		# with open(os.path.join(BASE_DIR, 'compare.txt'), 'r') as f_read:
		path = os.path.join(BASE_DIR, 'compare.txt') 
		mode = 'r' if os.path.exists(path) else 'w+'
		with open(path, mode) as f_read:
			before = f_read.readlines()
			before = [line.rstrip() for line in before] 
			
			f_read.close()
			for i in news_link:
				if i not in before:
					temp.append(i)
					cnt += 1
					with open(os.path.join(BASE_DIR, 'compare.txt'), 'a') as f_write:
						f_write.write(i+'\n')
						f_write.close()
			if cnt > 0:
				self.maintext_crawll(temp, cnt)
	
	def maintext_crawll(self, temp, cnt):
		#bot
		#chat_id
		#NEW
		#bot.sendMessage()
		news = []
		for n in temp:
			main_url = "https://www.boannews.com{}".format(n.strip())
			#bot.sendMessage()
	
			response = requests.get(main_url)
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')
			#title = soup.find_all('div', {'id':'news_title02'})
			#contents = soup.find_all('div', {'id':'news_content'})
			#date = soup.find_all('div',{'id':'news_util01'})
			#photos = soup.find_all('div',{'class':'news_image'})
			
			title = soup.find('div', {'id':'news_title02'})
			contents = soup.find('div', {'id':'news_content'})
			date = soup.find('div',{'id':'news_util01'})
			photos = soup.find('div',{'class':'news_image'})
	
			#for n in contents:
			#	text = n.text.strip()
			try:
				news.append(News(
					url=main_url,
					title=title.text,
					content=contents.text,
					date=datetime.datetime.now(),
					photo=photos.text
				))
			except Exception as e:
				print(e)
	
		News.objects.bulk_create(news)
