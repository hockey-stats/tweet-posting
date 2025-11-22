import re
import os
import json
import argparse
import requests
import tweepy

from requests_oauthlib import OAuth1


# Set env variables from repo secrets
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


def send_tweet(media_id, tweet_body):
    """
    Sends a tweet with the image denoted by the media_id, and the tweet_body as the text.
    Uses the requests library.
    :param str media_id: Identifier for media which was uploaded and is ready to send.
    :param str tweet_body: Text to send alongside the media in the tweet.
    """

    url = 'https://api.twitter.com/2/tweets'

    payload = json.dumps({
        "text": tweet_body,
        "media": {
            "media_ids": [media_id]
        }
    })

    headers = {
        'Content-Type': 'application/json',
    }

    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    response = requests.request("POST", url, headers=headers, auth=auth, data=payload, timeout=10)

    print(response.text)


def upload_media(image):
    """
    Given the path to an image file, upload that image to Twitter servers using
    tweepy, gather the resulting media_id value, and return it.
    :param str image: Path to image file.
    :return str media_id: ID value for media which was uploaded, used to send tweet.
    """

    if not os.path.isfile(image):
        raise FileNotFoundError(f"Image file {image} not found, aborting...")

    tweepy_auth = tweepy.OAuth1UserHandler(
        f"{API_KEY}",
        f"{API_SECRET}",
        f"{ACCESS_TOKEN}",
        f"{ACCESS_TOKEN_SECRET}"
    )

    tweepy_api = tweepy.API(tweepy_auth)

    # Use a different upload function for mp4 videos
    if image.split('.')[-1] == 'mp4':
        response = tweepy_api.media_upload(filename=image, chunked=True,
                                           media_category='tweet_cideo')
    else:
        response = tweepy_api.simple_upload(image)
    media_id = re.search("media_id=(.+?),", str(response)).group(1)
    print(media_id)
    return media_id


def main(image, text):
    """
    Main function
    """

    media_id = upload_media(image)
    send_tweet(media_id=media_id, tweet_body=text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True,
                        help='Path to image file which is to be tweeted.')
    parser.add_argument('-t', '--text', default='',
                        help='Text to be tweeted alongside image, defaults to empty string.')
    args = parser.parse_args()

    main(image=args.image, text=args.text)
