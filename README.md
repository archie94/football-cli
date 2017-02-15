# football-cli

Yet another CLI to show details of live football matches.

![alt tag](https://github.com/archie94/football-cli/blob/master/screenshots/Screenshot%20from%202017-02-15%2023:37:16.png)
![alt tag](https://github.com/archie94/football-cli/blob/master/screenshots/Screenshot%20from%202017-02-15%2023:38:11.png)
![alt tag](https://github.com/archie94/football-cli/blob/master/screenshots/Screenshot%20from%202017-02-15%2023:38:33.png)

## Build

```
git clone https://github.com/archie94/football-cli.git
cd football-cli
```

## Usage

### Get table standings for league 

```
python footballcli.py -t epl
```

or

```
python footballcli.py --table epl
```

- Premier League use `epl`
- La Liga use `laliga`
- Bundesliga use `bundesliga`
- Serie A use `serieA`
- Ligue 1 use `ligue1`

Currently we are limited to these leagues only.

### Get top scorers 

```
python footballcli.py -ts
```

or 

```
python footballcli.py --topscorer
```

### Get status of matches for the day

Use `-cd` or `--currentday` while running `footballcli,py`

### Get news from top leagues 

Use `-n` or `--news` while running `footballcli,py`

## Acknowledgements

This is a simple example of web scrapping made primarily for educational purpose. All the data have been collected from [Goal.com](http://www.goal.com/en-india) and [BBC](http://www.bbc.com/sport/football). 


### TODO 

Find in TODO.md
