import time
import random
import requests
import os
import traceback

# Set number of pages to be downloaded
NO_OF_PAGES = 80
# Set path for saving html-files
DWLD_PATH = "/home/dennis/PycharmProjects/flix_data_analysis"
os.chdir(DWLD_PATH)
link = "https://de.trustpilot.com/review/flixbus.de"
page_no = 1
# make header for http-requests
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
responses = []
# Iterate over all review-pages and download them.
try:
    while(True):
        # make a pause between every request
        time.sleep(random.randint(3, 8))
        # get html-file and save it
        response = requests.get(link, headers=header)
        with open('response_' + str(page_no) + '.txt', 'wb') as file:
            file.write(response.content)
        # make link for next page
        link = link[:-len(str(page_no))]
        page_no = page_no + 1
        link = link + str(page_no)
        # check whether last page has been reached
        if page_no > NO_OF_PAGES:
            break
except Exception as e:
    print page_no
    print "except at " + str(page_no)
    print traceback.print_exc()