import camelot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geopy.geocoders import Nominatim
import datetime

# Set up a firebase instance
cred = credentials.Certificate('./hodp-scraping-f5c8cc1cd113.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

crimes_ref = db.collection(u"crime-logs")

# geolocater = Nominatim(user_agent = "harvardopendataproject")

# Extract, clean, and insert data into db
tables = camelot.read_pdf("test.pdf", pages = "1-end")
row_num = 0

for table in tables:
    for row in table.data[1:]:
        if row_num % 2 == 0:
            clean_row = [x for x in row if len(x) > 0]
            clean_row[3] = clean_row[3].replace("\n", " ")
            # location = geolocater.geocode(clean_row[3])
            date_time_obj = datetime.datetime.strptime(clean_row[0], '%m/%d/%y\n%I:%M %p')
            report = {"reported": date_time_obj, "type": clean_row[1], "occurred": clean_row[2],
                        "address": clean_row[3], "status": clean_row[4]}
            row_num += 1
        else:
            clean_row = [x for x in row if len(x) > 0]
            report["description"] = clean_row[0]
            db.collection(u'crime-logs').add(report)
            row_num += 1

# Query db to get most recent date
query = crimes_ref.order_by(
    u'reported', direction=firestore.Query.DESCENDING).limit(1)
results = query.stream()
for doc in results:
    print(doc.to_dict())