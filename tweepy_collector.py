#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import json
import datetime

# Variables that contains the user credentials to access Twitter API
access_token = "3300412775-SvHfqR5eewVZIhFrGNExiejLneYtYkm8tOrqjBM"
access_token_secret = "BWqGuI9bgAVKrDHS8N4dBJTtgV4vmz4iZS94SHGXunoiT"
consumer_key = "7ijOTBDcEqnS6Qp93ljzSFpRp"
consumer_secret = "O53v77xDGN9FT0PL5zbFXIITQmNCuMoTYBKURYqmv5x9ugkOrU"


class Listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        print(all_data)
        tweet = all_data["text"]
        loc = all_data["user"]["location"]
        username = all_data["user"]["screen_name"]
        time = str(datetime.datetime.fromtimestamp(float(all_data["timestamp_ms"])/1000).time()).split('.')[0]
        date = datetime.datetime.fromtimestamp(float(all_data["timestamp_ms"])/1000).date().strftime("%d.%m.%Y")
        print(time)
        print(date)

        # check company mentioned
        flixbus = self.check_keywords(["fernbus", "flixbus"], str(all_data).lower())
        blablacar = self.check_keywords(["mitfahrgelegenheit", "blablacar"], str(all_data).lower())
        bahn = self.check_keywords(["bahn", "zug", "db", "diebahn", "deutschebahn"], str(all_data).lower())

        if "," in str(loc):
            city, country = str(loc).split(",")

        return True

    @ staticmethod
    def check_keywords(keywords, text):
        for word in keywords:
            if word in text.lower():
                return True
        return False


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["ich"])
