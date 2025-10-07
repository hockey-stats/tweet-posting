"""
Simple script made in the same vein as 'tweet_picture.py'. Takes an image and text string as 
arguments and sends a skeet with the contents.

Login info for BlueSky saved as repository variables in GitHub

"""

import os
import argparse
from atproto import Client, client_utils, models
from atproto_client.models.app.bsky.embed.defs import AspectRatio


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

    # Add link to explainer post for MLB charts
   # text_builder.text('For an explanation of the charts, click ')
   # text_builder.link('here', 'https://tinyurl.com/4499bd3r').text('\n\n')

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


def send_skeet(image, post_body, alt_text, aspect_ratio):
    """
    Given an image and text, login to the BlueSky client and send a skeet containing them.
    :param str image: Filepath to image which will be skeeted.
    :param str post_body: Text body of the skeet.
    :param str alt_text: Alt text for the skeet image.
    :param str apect_ratio: Aspect ratio to use for image in the form '{width},{height}'
    """
    client = Client()

    client.login(BSKY_LOGIN, BSKY_PASSWORD)

    # Aspect Ratio needs to be passed in as an AspectRatio object, parse the provided string
    # for width and height and construct the object. Raise an error if the provided string
    # isn't in proper format.
    try:
        width, height = aspect_ratio.split(',')
        image_aspect_ratio = AspectRatio(width=int(width), height=int(height))
    except ValueError as e:
        print("Aspect ratio provided in incorrect format!\n"\
              "Expected: '{width},{height}', e.g. '10,8'\n"\
              f"Recieved: '{aspect_ratio}'")
        raise e

    if image.split('.')[-1] == 'mp4':
        with open(image, 'rb') as f:
            vid_data = f.read()

        blob = client.upload_blob(vid_data)
        client.send_post(
            text=post_body,
            embed=models.AppBskyEmbedVideo.Main(video=blob.blob, alt=alt_text, aspect_ratio=image_aspect_ratio)
        )

    else:
        with open(image, 'rb') as f:
            img_data = f.read()
            client.send_image(text=post_body, image=img_data, image_alt=alt_text,
                              image_aspect_ratio=image_aspect_ratio)


def main(image, text, aspect_ratio):
    """
    Main function
    """
    post_body, alt_text = parse_text(text)
    send_skeet(image, post_body, alt_text, aspect_ratio)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True,
                        help='Path to image file which is to be skeeted.')
    parser.add_argument('-t', '--text', default='',
                        help='Text to be skeeted alongside image, defaults to empty string.')
    parser.add_argument('-a', '--aspect_ratio', default='10,8',
                        help='Aspect ratio to be used for image post. E.g., standard plots usually'\
                             'use 10x8, but game reports use 20x14. Defaults to "10,8".')
    args = parser.parse_args()

    main(image=args.image, text=args.text, aspect_ratio=args.aspect_ratio)
