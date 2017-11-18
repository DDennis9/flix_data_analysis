#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import json
import datetime
import os

# Variables that contains the user credentials to access Twitter API
access_token = "3300412775-SvHfqR5eewVZIhFrGNExiejLneYtYkm8tOrqjBM"
access_token_secret = "BWqGuI9bgAVKrDHS8N4dBJTtgV4vmz4iZS94SHGXunoiT"
consumer_key = "7ijOTBDcEqnS6Qp93ljzSFpRp"
consumer_secret = "O53v77xDGN9FT0PL5zbFXIITQmNCuMoTYBKURYqmv5x9ugkOrU"
headers = ["username", "time", "date", "city", "tweet", "flixbus", "bahn", "blablacar", "country"]


class Listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        loc = all_data["user"]["location"]
        username = all_data["user"]["screen_name"]
        time = str(datetime.datetime.fromtimestamp(float(all_data["timestamp_ms"])/1000).time()).split('.')[0]
        date = datetime.datetime.fromtimestamp(float(all_data["timestamp_ms"])/1000).date().strftime("%d.%m.%Y")

        # check company mentioned
        flixbus = self.check_keywords(["fernbus", "flixbus"], str(all_data).lower())
        blablacar = self.check_keywords(["mitfahrgelegenheit", "blablacar"], str(all_data).lower())
        bahn = self.check_keywords(["bahn", "zug", "db", "diebahn", "deutschebahn"], str(all_data).lower())

        if "," in str(loc):
            city, country = str(loc).split(",")
        else:
            city = ""
            country = loc

        self.write_to_csv([username, time, date, city, tweet, flixbus, bahn, blablacar, country])

        return True

    @ staticmethod
    def check_keywords(keywords, text):
        for word in keywords:
            if word in text.lower():
                return 1
        return 0

    @ staticmethod
    def write_to_csv(data):
        if not "twitter_stream.csv" in os.listdir("/home/dennis/PycharmProjects/flix_data_analysis"):
            with open("/home/dennis/PycharmProjects/flix_data_analysis/twitter_stream.csv", "a") as stream_csv:
                csv_writer = csv.writer(stream_csv, delimiter='\t')
                csv_writer.writerow(headers)
        with open("/home/dennis/PycharmProjects/flix_data_analysis/twitter_stream.csv", "a") as stream_csv:
            csv_writer = csv.writer(stream_csv, delimiter='\t')
            csv_writer.writerow(data)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["flixbus", "bahn", "fernbus", "zug", "db", "mitfahrgelegenheit", "blablacar", "diebahn",
                            "deutschebahn"])
