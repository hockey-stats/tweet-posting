"""
Small script where, given the filename for a game report PNG file in the format
    {team_a}_{team_b}_{date}.png
Parse it out and assemble a tweet body to be used in the tweet with the PNG.
"""

import os
import sys
from get_team_details import team_dict

if __name__ == '__main__':
    filename = sys.argv[1]
    basename = filename.split('.')[0]

    team_a, team_b, date = basename.split('_')

    hashtag_a = team_dict[team_a]['hashtag']
    hashtag_b = team_dict[team_b]['hashtag']

    full_team_a = team_dict[team_a]['full_name']
    full_team_b = team_dict[team_b]['full_name']

    tweet_body = f"Game Report - {full_team_a} vs {full_team_b} - {date}\n"\
                 f"{hashtag_a} {hashtag_b}"

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
        print(f'tweet_body={tweet_body}\n', file=fh)
        print(f'image_filename=${filename}\n', file=fh)
