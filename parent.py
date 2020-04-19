import praw
import dotenv
import os

class reddit_parent():
    def __init__(self):
        dotenv.load_dotenv()
        client_id = os.getenv('CLIENT_ID')
        my_secret = os.getenv('CLIENT_SERCRET')
        my_pass = os.getenv('PASSWORD')
        my_username = os.getenv('MY_USERNAME')
        # print('testscript by /u/{}'.format(my_username))
        self.reddit = praw.Reddit(client_id=client_id,
                            client_secret=my_secret,
                            password=my_pass,
                            user_agent='testscript by /u/{}'.format(my_username),
                            username=my_username)
    def check(self):
        return self.reddit.user.me()
