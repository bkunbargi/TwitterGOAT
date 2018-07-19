
import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token,config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
print('Succesfully Logged in.')


def clean_file(file_name):
    file = open(file_name,'r+')
    transport_file = open('output.txt','w')
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
    with open('output/'+file_name,"r") as input:
        line = input.readline()
        line = line.replace('lineskip','\n')
        print('Line to be tweeted: '+line)
        try:
            api.update_status(line)
        except:
            print('Did not work')
        with open('output/'+file_name,'w') as output:
            for new_line in input:
                if new_line!=line+"\n":
                    output.write(new_line)




if __name__ == '''__main__''':
    file_name = input('What file to use: ')
    direction = input('Cleaning or Tweeting: ')
    if direction[0].lower() == 'c':
        clean_file(file_name)
    if direction[0].lower() == 't':
        tweet_it(file_name)
