import requests
from bs4 import BeautifulSoup

url = {
	'goal_live_india': 'http://www.goal.com/en-india/live-scores?ICID=HP_TN_8_2',
	'goal_table_epl': 'http://www.goal.com/en-india/tables/premier-league/8',
	'goal_table_laliga': 'http://www.goal.com/en-india/tables/primera-divisi%C3%B3n/7',
	'goal_table_bundesliga': 'http://www.goal.com/en-india/tables/bundesliga/9',
	'goal_table_ligue1': 'http://www.goal.com/en-india/tables/ligue-1/16',
	'goal_table_serieA': 'http://www.goal.com/en-india/tables/serie-a/13'
}

def get_html(url):
	return requests.get(url).text # returns the html as text

def get_bsoup_object(htmltext):
	return BeautifulSoup(htmltext, "lxml") # use lxml parser
