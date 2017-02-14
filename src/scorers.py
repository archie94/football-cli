from bs4 import BeautifulSoup
from util import colors, url
import copy

scorer = {
	'name': [],
	'scored': [],
	'assist': [],
	'min_per_goal': [],
	'min_played': [],
	'team': []
}

ligue = {
	'epl': copy.deepcopy(scorer),
	'laliga': copy.deepcopy(scorer),
	'bundesliga': copy.deepcopy(scorer),
	'serieA': copy.deepcopy(scorer),
	'ligue1': copy.deepcopy(scorer),
	'ucl': copy.deepcopy(scorer),
	'europa': copy.deepcopy(scorer),
	'golden_boot': copy.deepcopy(scorer)
}

def print_scorers():
	for tournament in ligue:
		if len(ligue[tournament]['name']) > 0:
			print colors.RED, '\n\n' + tournament.upper()

		for i in range(len(ligue[tournament]['name'])):
			print colors.BLUE, ligue[tournament]['name'][i] + '\t' + colors.GREEN + ligue[tournament]['scored'][i] + '\t' + ligue[tournament]['assist'][i] + '\t' + colors.CYAN + ligue[tournament]['min_per_goal'][i] + '\t' + ligue[tournament]['min_played'][i] + '\t' + colors.ORANGE + ligue[tournament]['team'][i]

def get_scorers(soup, tournament):
	soup = soup.find('div', attrs = {'id': 'top-scorers', 'class': 'component'})

	players = soup.find_all('li')
	for i in range(5):
		name = players[i].find('h2', attrs = {'class': 'top-player-stats__name gel-double-pica'}).text
		team = players[i].find('div', attrs = {'class': 'top-player-stats__team'}).text
		min_per_goal = players[i].find('p', attrs = {'class': 'top-player-stats__mins-per-goal gel-long-primer'}).text
		min_played = players[i].find('p', attrs = {'class': 'top-player-stats__mins-played gel-long-primer'}).text
		scored = players[i].find('span', attrs = {'class': 'top-player-stats__goals-scored-number'}).text
		assist = players[i].find('span', attrs = {'class': 'top-player-stats__assists-number gel-double-pica'}).text
		ligue[tournament]['name'].append(name)
		ligue[tournament]['scored'].append(scored)
		ligue[tournament]['assist'].append(assist)
		ligue[tournament]['min_played'].append(min_played)
		ligue[tournament]['min_per_goal'].append(min_per_goal)
		ligue[tournament]['team'].append(team)

def main():
	links = [url.url['bbc_scorer_epl'],
			url.url['bbc_scorer_laliga'],
			url.url['bbc_scorer_bundesliga'],
			url.url['bbc_scorer_serieA'],
			url.url['bbc_scorer_ligue1']]
	tournament = ['epl', 'laliga', 'bundesliga', 'serieA', 'ligue1']
	for i in range(len(links)):
		htmltext = url.get_html(links[i])
		soup = url.get_bsoup_object(htmltext)

		get_scorers(soup, tournament[i])
	print_scorers()

if __name__ == "__main__":
	main()
