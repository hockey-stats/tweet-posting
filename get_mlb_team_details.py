"""
Small script that, given a team 3-letter acronym, returns the teams full name and official hashtag.
"""

import sys
import os

team_dict = {
	"ARI": "Arizona Diamondbacks",
	"ATH": "Homeless Athletics",
	"ATL": "Atlanta Braves",
	"BAL": "Baltimore Orioles",
	"BOS": "Boston Red Sox",
	"CHC": "Chicago Cubs",
	"CHW": "Chicago White Sox",
	"CIN": "Cincinnati Reds",
	"CLE": "Cleveland Guardians",
	"COL": "Colorado Rockies",
	"DET": "Detroit Tigers",
	"HOU": "Houston Astros",
	"KCR": "Kansas City Royals",
	"LAA": "Los Angeles Angels",
	"LAD": "Los Angeles Dodgers",
	"MIA": "Miami Marlins",
	"MIL": "Milwaukee Brewers",
	"MIN": "Minnesota Twins",
	"NYM": "New York Mets",
	"NYY": "New York Yankees",
	"PHI": "Philadelia Phillies",
	"PIT": "Pittsburgh Pirates",
	"SDP": "San Diego Padres",
	"SEA": "Seattle Mariners",
	"SFG": "San Francisco Giants",
	"STL": "St. Louis Blues",
	"TBR": "Tamba Bay Rays",
	"TEX": "Texas Rangers",
	"TOR": "Toronto Blue Jays",
	"WSN": "Washington Nationals",
}


if __name__ == '__main__':
    team = sys.argv[1]
    team_full_name = team_dict[team]
    if team in {'BOS', 'CHW', 'TOR'}:
        hashtag = '#' + ''.join(team_full_name.split()[-2:])
    else:
        hashtag = '#' + team_full_name.split()[-1]

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
        print(f'team_full_name={team_full_name}\n', file=fh)
        print(f'hashtag={hashtag}', file=fh)
