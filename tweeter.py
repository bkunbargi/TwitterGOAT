import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token,config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


keyword = input("First Search Term:  ")
other_key = input("Second Search Term: ")
goat_list = list()

def run_bot(input1, input2):
    print('Building Set')
    for tweet in tweepy.Cursor(api.search, q = input1).items(1000):
        if input2 in tweet.text:
            print("Next Tweet: " + tweet.text)
            goat_list.append(tweet.text)

    print("List is built")
    file = open('output.txt','w')
    goat_set = set(goat_list)
    for tweet in goat_set:
        file.write(tweet + '\n')
    file.close()
    print('Finished program')


run_bot(keyword,other_key)
