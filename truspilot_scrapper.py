import time
import random
import requests
import os
import traceback
from bs4 import BeautifulSoup
import csv

"""
Script for scraping and persisting data from trustpilot.
"""

headers = ["username", "time", "date", "city", "tweet", "flixbus", "bahn", "blablacar", "country", "rating"]


def write_to_csv(review):
    """
    Writes relevant data to a .csv-File.
    """
    if not "trustpilot.csv" in os.listdir("/home/dennis/PycharmProjects/flix_data_analysis/Trustpilot_Responses"):
        with open("/home/dennis/PycharmProjects/flix_data_analysis/Trustpilot_Responses/trustpilot.csv", "a") as review_csv:
            csv_writer = csv.writer(review_csv, delimiter='\t')
            csv_writer.writerow(headers)
    with open("/home/dennis/PycharmProjects/flix_data_analysis/Trustpilot_Responses/trustpilot.csv", "a") as review_csv:
        csv_writer = csv.writer(review_csv, delimiter='\t')
        csv_writer.writerow(review)


def extract_review(response):
    """
    Separates the single reviews from one html-Page from trustpilot.com. Extracts relevant fields from each review and
    persists the data in a .csv-File.
    """
    soup = BeautifulSoup(response, 'html.parser')
    review_list = soup.find_all("div", class_="review pageable-item-js item  user-has-image   clearfix") + \
                  soup.find_all("div", class_="review pageable-item-js item   clearfix")
    print(len(review_list))
    for review in review_list:
        user_name = review.find("a", class_="user-review-name-link").get_text().strip()
        time = review.time.attrs['datetime'].split("T")[1].split(".")[0]
        year, month, day = review.time.attrs['datetime'].split("T")[0].split("-")
        date = str(day) + "." + str(month) + "." + str(year)
        text = review.find("div", class_="review-body").get_text().strip()
        rating = int(str(review).split("star-rating count-")[1][:1])
        if rating == 3:
            rating = 0
        elif rating < 3:
            rating = 2
        else:
            rating = 1
        country = "Deutschland"
        write_to_csv([user_name, time, date, "", text, "0", "1", "0", "Deutschland", rating])

# Set path for saving html-files
DWLD_PATH = "/home/dennis/PycharmProjects/flix_data_analysis/Trustpilot_Responses"
os.chdir(DWLD_PATH)
link = "https://de.trustpilot.com/review/www.bahn.de"
page_no = 1
# make header for http-requests
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/39.0.2171.95 Safari/537.36'}
responses = []
has_next = True

# Iterate over all review-pages and download them.
try:
    while has_next:
        # make a pause between every request
        time.sleep(random.randint(1, 2))
        # get html-file and save it
        response = requests.get(link, headers=header)
        extract_review(response.content)
        has_next = 'data-page-number="next-page"' in str(response.content)
        if has_next:
            link = str(response.content).split('" data-page-number="next-page"')[0].split('<a href="')[-1]
            link = "https://de.trustpilot.com" + link
            print(link)
            page_no = page_no + 1

except Exception as e:
    print("except at " + str(page_no))
    print(traceback.print_exc())



