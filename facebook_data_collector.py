import json
import urllib
import csv
import datetime


pageid = {'Facebook':'248371251877349', 'Blablacar':'347775881990178', 'Bahn':'152033178165965'}
# pageid = {'Facebook':'248371251877349'}
for page in pageid:
    url = 'https://graph.facebook.com/v2.11/' + pageid[page] + '/feed?access_token=EAACEdEose0cBAMEmor4nUpmZCYWxZAEZB43IfxonkiN22vekDB7k5ZAEkH1ZBSPFHoN31WzC3uSC9C7lPG9Am51Tq0zzzMVaqwGDwCo3KgZBZCNqVZCFSzVgkWMcp8TItrHBRRov9a5AS5I2elC5x0aUa2uK3yDrwU7foYrNLrmPuO2Yb4kqhTtuIyxPzZBuv7WuQH3Itfwq4ggZDZD&fields=place,message,created_time&limit=100'
    resp = urllib.request.urlopen(url).read()
    obj = str(resp.decode('utf-8'))
    data = json.loads(obj)
    data_only = data['data']
    f = csv.writer(open("{}_v02_hackathon.csv".format(page), 'w'))
    # user_name | time | date | stadt | text | unternehmen | land |
    f.writerow(['user_name', 'time' , 'date', 'stadt', 'text', 'latitude' 'flixbus', 'bahn', 'blablacar', 'land'])
    for item in data_only:
        f.writerow([item['id'],
                    datetime.datetime.strptime(item['created_time'], '%Y-%m-%dT%H:%M:%S+0000').time(),
                    datetime.datetime.strptime(item['created_time'], '%Y-%m-%dT%H:%M:%S+0000').date().strftime("%d.%m.%Y"),
                    '',
                    item['message'],
                    #item['place']['location']['latitude'],
                    '{}'.format(1 if page == 'Facebook' else 0),
                    '{}'.format(1 if page == 'Bahn' else 0),
                    '{}'.format(1 if page == 'Blablacar' else 0),
                    'DE'])