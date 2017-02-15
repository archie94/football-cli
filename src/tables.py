from bs4 import BeautifulSoup
from util import colors, url

def print_table(table):
	print "POS \tTEAM \tP \tW \tD \tL \tGS \tGA \tGD \tPoints"
	for i in range(0,len(table["position"])):
		if i < 4:  
			print colors.GREEN, table['position'][i] + '\t' + table['name'][i] + '\t' + table['played'][i] + '\t' + table['win'][i] + '\t' + table['draw'][i] + '\t' + table['loss'][i] + '\t' +table['goal_scored'][i] + '\t' + table['goal_against'][i] + '\t' +table['goal_diff'][i] + '\t' + table['points'][i]
		elif i < 6:
			print colors.ORANGE, table['position'][i] + '\t' + table['name'][i] + '\t' + table['played'][i] + '\t' + table['win'][i] + '\t' + table['draw'][i] + '\t' + table['loss'][i] + '\t' +table['goal_scored'][i] + '\t' + table['goal_against'][i] + '\t' +table['goal_diff'][i] + '\t' + table['points'][i]
		elif i < 17:
			print colors.BLUE, table['position'][i] + '\t' + table['name'][i] + '\t' + table['played'][i] + '\t' + table['win'][i] + '\t' + table['draw'][i] + '\t' + table['loss'][i] + '\t' +table['goal_scored'][i] + '\t' + table['goal_against'][i] + '\t' +table['goal_diff'][i] + '\t' + table['points'][i]
		else :
			print colors.RED, table['position'][i] + '\t' + table['name'][i] + '\t' + table['played'][i] + '\t' + table['win'][i] + '\t' + table['draw'][i] + '\t' + table['loss'][i] + '\t' +table['goal_scored'][i] + '\t' + table['goal_against'][i] + '\t' +table['goal_diff'][i] + '\t' + table['points'][i]


def get_table(soup, htmltext):
	soup = soup.find('table', attrs = {'class': 'short'})

	tournament = soup.caption.h2.text
	print tournament

	soup = soup.find('tbody')
	teams = soup.find_all('tr')

	table = {
	'position': [],
	'name': [],
	'played': [],
	'win': [],
	'draw': [],
	'loss':	[],
	'goal_scored': [],
	'goal_against': [],
	'goal_diff': [],
	'points': []
	}

	for team in teams:
		table["position"].append(team.find('td', attrs = {'class': 'legend position'}).text)
		table["name"].append(team.find('td', attrs = {'class': 'legend team full'}).a.text.strip('\n'))

		played, win, draw, loss = team.find_all('td', attrs = {'class': ''})
		table["played"].append(played.text)
		table["win"].append(win.text)
		table["draw"].append(draw.text)
		table["loss"].append(loss.text)

		table["goal_scored"].append(team.find('td', attrs = {'class': 'goals-scored full always-on-competition'}).text)
		table["goal_against"].append(team.find('td', attrs = {'class': 'goals-against full always-on-competition'}).text)
		table["goal_diff"].append(team.find('td', attrs = {'class': 'always-ltr'}).text.strip('\n'))
		table["points"].append(team.find('td', attrs = {'class': 'pts-last'}).text)

	print_table(table)

def main(link):
	htmltext = url.get_html(link)
	soup = url.get_bsoup_object(htmltext)

	get_table(soup, htmltext)
	print 'Data collected from ', link

if __name__ == "__main__":
	main()