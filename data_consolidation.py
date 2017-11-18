import pandas as pd
import random

"""
Concatenates data collected from different sources.
"""

# load data from trustpilot and facebook
trustpilot_df = pd.DataFrame.from_csv("trustpilot.csv", sep="\t")
fb_df = pd.read_excel("facebook_data.xlsx")
fb_df['source'] = "facebook"

# add locations

# concatenate and save data
trustpilot_fb = pd.concat([trustpilot_df, fb_df], ignore_index=True)
trustpilot_fb['city'] = ""
cities = pd.DataFrame.from_csv("cities.csv", sep="\t")
print(cities)
for index, row in trustpilot_fb.iterrows():
    rand = random.randint(0, 100)
    c = cities.loc[1]
    for ind, city in cities.iterrows():
        if not int(city['share_cumu'] * 100.0) < rand:
            c = city
        else:
            break
    trustpilot_fb.set_value(index, 'city', c['Stadt'])
trustpilot_fb.to_csv("trustpilot_fb.csv", sep="\t")
trustpilot_fb = pd.DataFrame.from_csv("trustpilot_fb.csv", sep="\t")
