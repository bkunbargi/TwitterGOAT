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
    result = tweepy.Cursor(api.search,q = input1, wait_on_rate_limit = True, tweet_mode = 'extended').items(100)
    for element in result:
        try:
            if(element.retweet_count == 0):
                tweet_text = element._json['full_text'].replace('\n','lineskip')
                if(input2 in (tweet_text)):
                    print(tweet_text.replace('\n',' '))
                    goat_list.append(tweet_text)
            else:
                tweet_text = element._json['retweeted_status']['full_text'].replace('\n','lineskip')
                if(input2 in (tweet_text)):
                    goat_list.append(tweet_text)
        except:
            print('Didnt work here')
            #print(element)

    #for tweet in tweepy.Cursor(api.search,q = input1, wait_on_rate_limit = True, tweet_mode = 'extended').items(1000):
    #    if input2 in tweet.text:
    #        print("Next Tweet: " + tweet.text)
    #        goat_list.append(tweet.text)

    print(goat_list)
    print("List is built")

    file = open('output'+'/'+input1+'.txt','a+')
    goat_set = set(goat_list)
    for tweet in goat_set:
        file.write(tweet)
        file.write('\n')
    file.close()
    print('Finished program')


run_bot(keyword,other_key)
