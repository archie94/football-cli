# football-cli

Yet another CLI to show details of live football matches.

## Build

```
git clone 
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
