#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import random
import time
import json
from HTMLParser import HTMLParser

#Variables that contains the user credentials to access Twitter API 
access_token = "1013974544862900224-OPAmsjG1LRZXTBvAoEA0vohqfnyNIN"
access_token_secret = "wy4JzyMbjJXpMmTpf8n7xIc8vM2hwsxI8682nthrpdfeV"
consumer_key = "b64HcVTXO8gEPQWC98Amool2m"
consumer_secret = "LivflElnpaAqeZzXdwB5Zqk5elIufBT4k9Zaohp8LtHoDYUtGK"

i = 0
j = 0
sair = 2000000
from pynput.keyboard import Key, Controller

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    # on_status
    def on_data(self, data):
        global i
        global j
        global sair
        j = 0
        i = i + 1
        # print(i)
        data = json.loads(HTMLParser().unescape(data))
        try:
            print(data['text'].encode('utf-8'))
        except:
            e = 0
        # print(data)
        if (i > sair):
            #print('saiu')
            keyboard1 = Controller()
            keyboard1.press(Key.ctrl)
            keyboard1.press('c')
        return True
        #print(data['coordinates'])
        #print(data)

    def on_error(self, status):
        print(status)


if (__name__ == '__main__'):

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    stream = Stream(auth=api.auth, listener=l)

    # stream.filter(languages=['pt'], track=['a','coisa','casa','tempo','ano','dia','vez','homem','senhor','senhora','bom','grande', 'melhor','pior','certo','ser', 'ir', 'estar','ter'])
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    while (1):
        try:
            stream.filter(languages=['pt'], track=['a','coisa','casa','tempo','ano','dia','vez','homem','senhor','senhora','bom','grande', 'melhor','pior','certo','ser', 'ir', 'estar','ter'])
            break
        except:
            j = j + 1
            #print(j)
            #print('excep123')
            if (j > 2 or i > sair):
                #print('saiu2')
                keyboard2 = Controller()
                keyboard2.press(Key.ctrl)
                keyboard2.press('c')
            nsecs=random.randint(10,15)
            time.sleep(nsecs)