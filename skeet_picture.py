"""
Simple script made in the same vein as 'tweet_picture.py'. Takes an image and text string as 
arguments and sends a skeet with the contents.

Login info for BlueSky saved as repository variables in GitHub

"""

import os
import argparse
from atproto import Client, client_utils

# Set env variables from repo secrets
BSKY_LOGIN = os.environ['BSKY_LOGIN']
BSKY_PASSWORD = os.environ['BSKY_PASSWORD']


def parse_text(text):
    """
    The atproto API requires extra parsing to have hashtags appear properly in posts.
    Create a TextBuilder object that has the proper text body and hashtags, and use
    this to populate the text of the post.

    :param str text: The raw text of the post, including hashtags.
    """
    text_builder = client_utils.TextBuilder()

    # First get the plain text (i.e. everything before the first hashtag)
    # This will also be returned as the alt_text
    plain_text = text.split('#')[0]
    text_builder.text(plain_text + '\n\n')  # Also add newlines so that the hashtags are alone

    # Now get all the hashtags, e.g. if the input text is
    #"Game Report - Montreal Canadiens vs Tampa Bay Lightning - 2025-02-09 #GoHabsGo #GoBolts #NHL"
    # then `hashtags`` will look like:
    #   ['GoHabsGo', 'GoBolts', 'NHL']
    hashtags = text.split(' #')[1:]

    # Add them to the text builder
    for hashtag in hashtags:
        text_builder.tag(f'#{hashtag} ', hashtag)

    # Return text_builder and alt_text
    return text_builder, plain_text


def send_skeet(image, post_body, alt_text):
    """
    Given an image and text, login to the BlueSky client and send a skeet containing them.
    :param str image: Filepath to image which will be skeeted.
    :param str post_body: Text body of the skeet.
    :param str alt_text: Alt text for the skeet image.
    """
    client = Client()

    client.login(BSKY_LOGIN, BSKY_PASSWORD)

    with open(image, 'rb') as f:
        img_data = f.read()

        client.send_image(text=post_body, image=img_data, image_alt=alt_text)


def main(image, text):
    """
    Main function
    """
    post_body, alt_text = parse_text(text)
    send_skeet(image, post_body, alt_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True,
                        help='Path to image file which is to be skeeted.')
    parser.add_argument('-t', '--text', default='',
                        help='Text to be skeeted alongside image, defaults to empty string.')
    args = parser.parse_args()

    main(image=args.image, text=args.text)
