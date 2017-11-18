import pandas as pd

twitter_df = pd.DataFrame.from_csv("twitter_stream_zw.csv", sep="\t")
print(twitter_df[twitter_df['flixbus']==1])