# TODO: Handle the case where it doesn't read through correctly (split on the \n and then split them up and recombine)

import camelot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geopy.geocoders import Nominatim
import datetime
from datetime import timedelta
from urllib.request import urlopen
import re
from matplotlib import pyplot as plt

# Set up a firebase instance
cred = credentials.Certificate('./hodp-scraping-f5c8cc1cd113.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

crimes_ref = db.collection(u"crime-logs")

# geolocater = Nominatim(user_agent = "harvardopendataproject")

#Extract, clean, and insert data into db
def scrape(url):
    # tables = camelot.read_pdf(url, pages = "1-end", flavor="stream", edge_tol=200, row_tol = 30)
    # tables = camelot.read_pdf("test.pdf", pages="1-end")
    tables = camelot.read_pdf(url, pages="1-end")
    row_num = 0

    for table in tables:
        for row in table.data[1:]:
            if row_num % 2 == 0:
                clean_row = [x for x in row if len(x) > 0]
                clean_row[3] = clean_row[3].replace("\n", " ")
                date_time_obj = datetime.datetime.strptime(clean_row[0], '%m/%d/%y\n%I:%M %p')
                report = {"reported": date_time_obj, "type": clean_row[1], "occurred": clean_row[2],
                          "address": clean_row[3], "status": clean_row[4]}
                row_num += 1
            else:
                clean_row = [x for x in row if len(x) > 0]
                report["description"] = clean_row[0]
                db.collection(u'crime-logs').add(report)
                row_num += 1

# Find latest date
query = crimes_ref.order_by(
    u'reported', direction=firestore.Query.DESCENDING).limit(1)
results = query.stream()
for doc in results:
    latest_time = (doc.to_dict ())["reported"]
    last_date = datetime.datetime(year=latest_time.year, month=latest_time.month, day=latest_time.day)
    last_date += timedelta(days = 1)
    cur_date = datetime.datetime.now()
    while(last_date < cur_date):
        day = str(last_date.day)
        month = str(last_date.month)
        year = str(last_date.year - 2000)
        if(len(month) < 2):
            month = "0" + month
        if(len(day) < 2):
            day = "0" + day
        url = "https://www.hupd.harvard.edu/files/hupd/files/" + month + day + year + ".pdf"
        # Scrape each url
        scrape(url)
        last_date += timedelta(days = 1)
