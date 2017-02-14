import requests
from bs4 import BeautifulSoup

url = {
	'goal_live_india': 'http://www.goal.com/en-india/live-scores?ICID=HP_TN_8_2',
	'goal_table_epl': 'http://www.goal.com/en-india/tables/premier-league/8',
	'goal_table_laliga': 'http://www.goal.com/en-india/tables/primera-divisi%C3%B3n/7',
	'goal_table_bundesliga': 'http://www.goal.com/en-india/tables/bundesliga/9',
	'goal_table_ligue1': 'http://www.goal.com/en-india/tables/ligue-1/16',
	'goal_table_serieA': 'http://www.goal.com/en-india/tables/serie-a/13',
	'goal_news_england': 'http://www.goal.com/en-india/news/137/england?ICID=OP_TN_2_2_1', 
	'goal_news_spain': 'http://www.goal.com/en-india/news/138/spain?ICID=SP_TN_2_2_2',
	'goal_news_italy': 'http://www.goal.com/en-india/news/139/italy?ICID=SP_TN_2_2_3',
	'goal_news_germany': 'http://www.goal.com/en-india/news/3753/germany?ICID=SP_TN_2_2_4',
	'bbc_scorer_epl': 'http://www.bbc.com/sport/football/premier-league/top-scorers',
	'bbc_scorer_laliga': 'http://www.bbc.com/sport/football/spanish-la-liga/top-scorers',
	'bbc_scorer_bundesliga': 'http://www.bbc.com/sport/football/german-bundesliga/top-scorers',
	'bbc_scorer_serieA': 'http://www.bbc.com/sport/football/italian-serie-a/top-scorers',
	'bbc_scorer_ligue1': 'http://www.bbc.com/sport/football/french-ligue-one/top-scorers'
}

def get_html(url):
	return requests.get(url).text # returns the html as text

def get_bsoup_object(htmltext):
	return BeautifulSoup(htmltext, "lxml") # use lxml parser
