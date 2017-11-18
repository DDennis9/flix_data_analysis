import pandas as pd

"""
Concatenates data collected from different sources.
"""

# load data from trustpilot and facebook
trustpilot_df = pd.DataFrame.from_csv("trustpilot.csv", sep="\t")
fb_df = pd.DataFrame.from_csv("facebook.csv", sep="\t")
fb_df['source'] = "facebook"

# concatenate and save data
trustpilot_fb = pd.concat([trustpilot_df, fb_df], ignore_index=True)
trustpilot_fb.to_csv("trustpilot_fb.csv", sep="\t")
trustpilot_fb = pd.DataFrame.from_csv("trustpilot_fb.csv", sep="\t")

