import praw
import dotenv
import os


dotenv.load_dotenv()
client_id = os.getenv('CLIENT_ID')
my_secret = os.getenv('CLIENT_SERCRET')
my_pass = os.getenv('PASSWORD')
username = os.getenv('MY_USERNAME')

reddit = praw.Reddit(client_id='SI8pN3DSbt0zor',
                     client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                     password='1guiwevlfo00esyy',
                     user_agent='testscript by /u/fakebot3',
                     username='fakebot3')
