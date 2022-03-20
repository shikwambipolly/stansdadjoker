import tweepy
import requests
import praw
import time

def send_tweet(text):
    api_key = 'whateveryoursis'
    api_key_secret = 'whateveryoursis'

    bearer_token = 'whateveryoursis'

    access_token = 'whateveryoursis'
    access_token_secret = 'whateveryoursis'

    joker = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    joker.create_tweet(text=text)


def get_posts():
    posts = []
    reddit = praw.Reddit(
        client_id="whateveryoursis",
        client_secret="whateveryoursis",
        user_agent="whateveryoursis"
    )
    for submission in reddit.subreddit('csMajors').top(time_filter='month', limit=5):
        title = submission.title.lower()
        body = submission.selftext.lower()
        if ((len(title) + len(body) + 10) < 280):
            posts.append(title + '\n' + '\n' + body)
    return posts


def main():
    for post in get_posts():
        send_tweet(post)
        time.sleep(5)

if __name__ == '__main__':
    main()
