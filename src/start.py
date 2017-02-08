import requests
from bs4 import BeautifulSoup
import datetime
from util import colors

def get_current_date():
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d") # returns current date in YYYY-mm-dd format

def get_html(url):
	return requests.get(url).text # returns the html as text

def get_bsoup_object(htmltext):
	return BeautifulSoup(htmltext, "lxml") # use lxml parser

# print data in a tabular form
def print_table(col1, col2, col3, col4):
	for i in range(0, len(col1)):
		print col1[i], '\t', col2[i], '\t\t\t', col3[i], '\t', col4[i]

def matches_today(date, soup, htmltext):
	soup = soup.find('section', attrs = {'class': 'matchdays-wrapper'})
	current_day_matches = soup.find_all('section', attrs = {'class': 'matchday', 'data-day' : date})

	for i in range(0, len(current_day_matches)):

		header = current_day_matches[i].find('header', attrs = {'class': 'info-header'}).h3.text
		print " Showing matches for ", header

		tables = current_day_matches[i].find_all('table', attrs = {'class': 'matches'})
		for j in range(0, len(tables)):
			out_color = colors.color[j%len(colors.color)]
			print out_color, " ================================================================================="
			tournament = tables[j].find('span', attrs = {'class': 'comp-title'})
			if tournament is not None:
				print tournament.text
			fixtures = tables[j].find_all('tbody')
			
			print "Total ", len(fixtures), " fixtures for today"
			
			home_teams = []
			away_teams = []
			match_status = []
			match_result = []
			for fixture in fixtures:
				status = fixture.find('td', attrs = {'class': 'status'}).span.text
				vs = fixture.find('td', attrs = {'class': 'vs'}).div.text.strip('\n')

				team1, team2 = fixture.find_all('td', attrs = {'class': 'team'})
				team1 = team1.div.span.text
				team2 = team2.div.span.text
				home_teams.append(team1)
				away_teams.append(team2)
				match_status.append(status)
				match_result.append(vs)

			print_table(match_status, home_teams, match_result, away_teams)

def main():
	date = get_current_date()
	urls = ["http://www.goal.com/en-india/live-scores?ICID=HP_TN_8_2"]  

	htmltext = get_html(urls[0])
	soup = get_bsoup_object(htmltext)

	matches_today(date, soup, htmltext)
	
if __name__ == "__main__":
	main()