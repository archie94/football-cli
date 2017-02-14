import sys
from src import tables, currentday, news, scorers
from src.util import errmsg, url

def main():
	if len(sys.argv) > 1:
		if len(sys.argv) > 2 and (sys.argv[1] == '--table' or sys.argv[1] == '-t'):
			if sys.argv[2] == 'epl':
				tables.main(url.url['goal_table_epl'])
			elif sys.argv[2] == 'laliga':
				tables.main(url.url['goal_table_laliga'])
			elif sys.argv[2] == 'bundesliga':
				tables.main(url.url['goal_table_bundesliga'])
			elif sys.argv[2] == 'ligue1':
				tables.main(url.url['goal_table_ligue1'])
			elif sys.argv[2] == 'serieA':
				tables.main(url.url['goal_table_serieA'])
			else:
				print "error"

		elif sys.argv[1] == '--currentday' or sys.argv[1] == '-cd':
			currentday.main()

		elif sys.argv[1] == '--news' or sys.argv[1] == '-n':
			news.main()

		elif sys.argv[1] == '--topscorer' or sys.argv[1] == '-ts':
			scorers.main()

if __name__ == "__main__":
	main()
