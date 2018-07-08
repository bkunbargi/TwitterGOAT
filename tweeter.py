import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token,config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


keyword = input("First Search Term:  ")
other_key = input("Second Search Term: ")
goat_set = list()

def run_bot(input1, input2):
    print('Building Set')
    for tweet in tweepy.Cursor(api.search, q = input1).items():
        if input2 in tweet.text:
            goat_set.append(tweet.text)

    for element in goat_set:
        print("Tweet: " + element)

run_bot(keyword,other_key)
