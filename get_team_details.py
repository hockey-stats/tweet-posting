"""
Small script that, given a team 3-letter acronym, returns the teams full name and official hashtag.
"""

import sys
import os

team_dict = {
    'MIN': {
    	'full_name': 'Minnesota Wild',
		'hashtag': '#mnwild'
    },
    'VGK': {
    	'full_name': 'Vegas Golden Knights',
		'hashtag': '#VegasBorn'
    },
    'OTT': {
    	'full_name': 'Ottawa Senators',
		'hashtag': '#GoSensGo'
    },
    'CAR': {
    	'full_name': 'Carolina Hurricanes',
		'hashtag': '#RaiseUp'
    },
    'CBJ': {
    	'full_name': 'Columbus Blue Jackets',
		'hashtag': '#CBJ'
    },
    'FLA': {
    	'full_name': 'Florida Panthers',
		'hashtag': '#TimeToHunt'
    },
    'LA': {
    	'full_name': 'Los Angeles Kings',
		'hashtag': '#GoKingsGo'
    },
    'LAK': {
    	'full_name': 'Los Angeles Kings',
		'hashtag': '#GoKingsGo'
    },
    'NJ': {
    	'full_name': 'New Jersey Devils',
		'hashtag': '#NJDevils'
    },
    'NJD': {
    	'full_name': 'New Jersey Devils',
		'hashtag': '#NJDevils'
    },
    'MTL': {
    	'full_name': 'Montreal Canadiens',
		'hashtag': '#GoHabsGo'
    },
    'COL': {
    	'full_name': 'Colorado Avalanche',
		'hashtag': '#GoAvsGo'
    },
    'WSH': {
    	'full_name': 'Washington Capitals',
		'hashtag': '#ALLCAPS'
    },
    'DET': {
    	'full_name': 'Detroit Red Wings',
		'hashtag': '#LGRW'
    },
    'TBL': {
    	'full_name': 'Tampa Bay Lightning',
		'hashtag': '#GoBolts'
    },
    'TB': {
    	'full_name': 'Tampa Bay Lightning',
		'hashtag': '#GoBolts'
    },
    'VAN': {
    	'full_name': 'Vancouver Canucks',
		'hashtag': '#Canucks'
    },
    'DAL': {
    	'full_name': 'Dallas Stars',
		'hashtag': '#TexasHockey'
    },
    'NYR': {
    	'full_name': 'New York Rangers',
		'hashtag': '#NYR'
    },
    'BUF': {
    	'full_name': 'Buffalo Sabres',
		'hashtag': '#SabreHood'
    },
    'PHI': {
    	'full_name': 'Philadelphia Flyers',
		'hashtag': '#LetsGoFlyers'
    },
    'EDM': {
    	'full_name': 'Edmonton Oilers',
		'hashtag': '#LetsGoOilers'
    },
    'STL': {
    	'full_name': 'St Louis Blues',
		'hashtag': '#stlblues'
    },
    'SEA': {
    	'full_name': 'Seattle Kraken',
		'hashtag': '#SeaKraken'
    },
    'TOR': {
    	'full_name': 'Toronto Maple Leafs',
		'hashtag': '#LeafsForever'
    },
    'SJ': {
    	'full_name': 'San Jose Sharks',
		'hashtag': '#TheFutureIsTeal'
    },
    'SJS': {
    	'full_name': 'San Jose Sharks',
		'hashtag': '#TheFutureIsTeal'
    },
    'PIT': {
    	'full_name': 'Pittsburgh Penguins',
		'hashtag': '#LetsGoPens'
    },
    'WPG': {
    	'full_name': 'Winnipeg Jets',
		'hashtag': '#GoJetsGo'
    },
    'CGY': {
    	'full_name': 'Calgary Flames',
		'hashtag': '#Flames'
    },
    'BOS': {
    	'full_name': 'Boston Bruins',
		'hashtag': '#NHLBruins'
    },
    'NSH': {
    	'full_name': 'Nashville Predators',
		'hashtag': '#Smashville'
    },
    'ANA': {
    	'full_name': 'Anaheim Ducks',
		'hashtag': '#FlyTogether'
    },
    'CHI': {
    	'full_name': 'Chicago Blackhawks',
		'hashtag': '#Blackhawks'
    },
    'ARI': {
    	'full_name': 'Arizona Coyotes',
		'hashtag': '#LolArizona'
    },
    'NYI': {
    	'full_name': 'New York Islanders',
		'hashtag': '#Isles'
    },
    'UTA': {
        'full_name': 'Utah Hockey Club',
        'hashtag': '#UtahHC'
    }
}

if __name__ == '__main__':
    team = sys.argv[1]

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
        print(f'team_full_name={team_dict[team]["full_name"]}\n', file=fh)
        print(f'hashtag={team_dict[team]["hashtag"]}', file=fh)
