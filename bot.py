import tweepy
import schedule
import time
import random
from dotenv import load_dotenv
import os
from datetime import datetime

# Load .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Tweet and Comment Templates
TWEET_TEMPLATES = [
    "Hunt smarter, not harder. Scryptex.xyz #AirdropHunter",
    "Wallet empty? Hope full? Let's farm smarter. #Web3Hunter",
    "Farm smarter, not harder. Early hunters win big. #ScryptexHunt"
]

COMMENT_TEMPLATES = [
    "Another one to the farming list! Let's go!",
    "Validation first, farming later. Scryptex fam knows!",
    "Early alpha spotted. Secured my spot.",
    "Me seeing another airdrop: *grabs ledger*",
    "Over 75% airdrops are trash. Hunt smarter with Scryptex."
]

TARGET_ACCOUNTS = ['Galxe', 'TaskOnXYZ', 'Zealy_io']  # ganti jika mau tambah target akun

# Post random tweet
def post_random_tweet():
    tweet = random.choice(TWEET_TEMPLATES)
    api.update_status(tweet)
    print(f"[{datetime.now()}] Posted Tweet: {tweet}")

# Reply random comment to target accounts
def auto_reply_campaign():
    for account in TARGET_ACCOUNTS:
        try:
            tweets = api.user_timeline(screen_name=account, count=5, tweet_mode='extended')
            for tweet in tweets:
                comment = random.choice(COMMENT_TEMPLATES)
                api.update_status(status=f"@{account} {comment}", in_reply_to_status_id=tweet.id)
                print(f"[{datetime.now()}] Replied to @{account}: {comment}")
                time.sleep(random.randint(60, 180))
        except Exception as e:
            print(f"Error replying to @{account}: {e}")

# Schedule tasks
schedule.every().day.at("10:00").do(post_random_tweet)
schedule.every(3).hours.do(auto_reply_campaign)

print("Scryptex Bot Running...")
while True:
    schedule.run_pending()
    time.sleep(30)
