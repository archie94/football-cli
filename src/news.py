from bs4 import BeautifulSoup
from util import colors, url

articles = {
	'headline': [],
	'content': [],
	'time': []
}

def print_news():
	for i in range(len(articles['time'])):
		print colors.ORANGE, articles['time'][i], '\t', colors.BLUE, articles['headline'][i], '\n\t', colors.GREEN, articles['content'][i]

def get_news(soup):
	soup = soup.find('div', attrs = {'class': 'main-content'})

	all_articles = soup.find_all('article', attrs = {'class': 'story clearfix'})
	for article in all_articles:
		if article.h4.text not in articles['headline']:
			articles['headline'].append(article.h4.text)
			articles['content'].append(article.p.text[5:])
			articles['time'].append(article.p.text[:5])
	

def main():
	links = [url.url['goal_news_england'], 
			url.url['goal_news_spain'],
			url.url['goal_news_italy'],
			url.url['goal_news_germany']]
	for link in links:
		htmltext = url.get_html(link)
		soup = url.get_bsoup_object(htmltext)

		get_news(soup)
	#(articles['time'], articles['headline'], articles['content']) in sorted(zip(articles['time'], articles['headline'], articles['content']))
	print_news()

if __name__ == "__main__":
	main()
