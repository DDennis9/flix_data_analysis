import pandas as pd
import numpy as np

"""
Script for analyzing the collected data. Checks for every available post, whether one of the given keywords is 
included. With these results, the categories' scores are calculated.
"""

# load available data
df = pd.DataFrame.from_csv("trustpilot_fb.csv", sep="\t")
df = df.drop_duplicates()
df['source'] = 'trustpilot'

# load keywords with related categories and impact (negative/positive)
df_words = pd.DataFrame.from_csv("/home/dennis/PycharmProjects/flix_data_analysis/schlagworte_kategorien.csv", sep=",")
df_words = pd.DataFrame(df_words.values, columns=["Word", "Category", "Sentiment"])
categories = np.unique(df_words['Category'])

# create neutral entries for each category and post
for category in categories:
    df[category] = 0

# do word analysis and calculate scores
for index, word in df_words.iterrows():
    word_list = []
    for ind, review in df.iterrows():
        if str(" " + word['Word'] + " ") in str(review['tweet']).lower():
            word_list.append(1)
            if word['Sentiment'] == "Negative":
                df.set_value(ind, word['Category'], review[word['Category']] - 1)
            else:
                df.set_value(ind, word['Category'], review[word['Category']] + 1)
        else:
            word_list.append(0)
    df[word['Word']] = word_list

# save file
df.to_csv("trustpilot_fb.csv", sep="\t")
