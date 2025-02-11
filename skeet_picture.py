"""
Simple script made in the same vein as 'tweet_picture.py'. Takes an image and text string as arguments
and sends a skeet with the contents.

Login info for BlueSky saved as repository variables in GitHub

"""

import os
import argparse
from atproto import Client

# Set env variables from repo secrets
BSKY_LOGIN = os.environ['BSKY_LOGIN']
BSKY_PASSWORD = os.environ['BSKY_PASSWORD']


def send_skeet(image, text):
    """
    Given an image and text, login to the BlueSky client and send a skeet containing them.
    :param str image: Filepath to image which will be skeeted.
    :param str text: Text body of the skeet.
    """
    client = Client()

    client.login(BSKY_LOGIN, BSKY_PASSWORD)

    # Set the alt text to be the tweet body but without the hashtags
    alt_text = text.split('#')[0] if '#' in text else text

    with open(image, 'rb') as f:
        img_data = f.read()

        client.send_image(text=text, image=img_data, image_alt=alt_text)


def main(image, text):
    """
    Main function
    """
    send_skeet(image, text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True,
                        help='Path to image file which is to be skeeted.')
    parser.add_argument('-t', '--text', default='',
                        help='Text to be skeeted alongside image, defaults to empty string.')
    args = parser.parse_args()

    main(image=args.image, text=args.text)
