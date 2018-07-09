
import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token,config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
print('Succesfully Logged in.')


def clean_file(file_name):
    file = open(file_name,'r+')
    transport_file = open('tweets.txt','w')
    new_line = ''


    for line in file:
        for word in line.split():
            ''' line[-1] == '\n' '''
            if (word[0] == 'R' and word[1] == 'T') or word[0] == '@' or word[0:3] == 'http':
                word = word.replace(word,'')
            else:
                new_line += (word+' ')

        new_line += '\n'
    transport_file.write(new_line)



def tweet_it(file_name):
    with open(file_name,"r") as input:
        line = input.readline()
        print('Line to be tweeted: '+line)
        api.update_status(line)
        with open(file_name,'w') as output:
            for new_line in input:
                if new_line!=line+"\n":
                    output.write(new_line)
    #file = open(file_name,'r+')
    #line = file.readline()
    #print('line to be tweeted: '+line)
    #api.update_status(line)
    #print('tweeted')
    #file.close()
    #for line in open(file_name,'r+'):
    #    file.write(line)
    #line = line.replace(line,'Used')
    #file.write(line)
    #file.close()







if __name__ == '''__main__''':
    file_name = input('What file to use: ')
    direction = input('Cleaning or Tweeting: ')
    if direction[0].lower() == 'c':
        clean_file(file_name)
    if direction[0].lower() == 't':
        tweet_it(file_name)