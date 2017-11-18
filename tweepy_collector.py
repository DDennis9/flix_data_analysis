#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "3300412775-SvHfqR5eewVZIhFrGNExiejLneYtYkm8tOrqjBM"
access_token_secret = "BWqGuI9bgAVKrDHS8N4dBJTtgV4vmz4iZS94SHGXunoiT"
consumer_key = "7ijOTBDcEqnS6Qp93ljzSFpRp"
consumer_secret = "O53v77xDGN9FT0PL5zbFXIITQmNCuMoTYBKURYqmv5x9ugkOrU"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self):
        self.counter = 0

    def on_data(self, data):
        print(data)
        self.counter = self.counter + 1
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['flixbus', 'bahn', 'fernbus'])