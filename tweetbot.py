#tweet bot using python and tweepy.
#python and tweepy required to be installed.
import tweepy
from time import sleep
import random

#Go to developer.twitter.com
#sign up for devoloper account then create an app and your unque Keys and secret.
CONSUMER_KEY = 'xxxxxx'
CONSUMER_SECRET = 'yyyyyy'
ACCESS_KEY = 'zzzzz'
ACCESS_SECRET = 'zzz'

print('Script started',)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#twitter compares the tweets multiple tweet can not have same value, so we are going to generate random value an add that to our every tweet.
#generating random number(int) to add in last of the tweet so it don't look same
randomlist = random.sample(range(0, 99), 99)
int = random.choice(randomlist)
print(int)
#intiger value can not be tweeted so
#converting intiger to string.
string = f'{int}'
print('Attempting to Comment.', flush=True)
for status in api.user_timeline():
    #Edit Hashtags
    #items(no.) no. of time you want to tweet
    api.update_status('YOUR TEXT TO BE TWEETED @User_name #Hashtags ' + ' ' + string).items(100)
    print('Comment successful')
    #Read the twitter automaation guidlines don't get blocked.
    #sleep(60) In second
    sleep(60)