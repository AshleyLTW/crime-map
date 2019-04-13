import camelot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geopy.geocoders import Nominatim

# Set up a firebase instance
cred = credentials.Certificate('./hodp-scraping-f5c8cc1cd113.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

crimes_ref = db.collection(u"crime-logs")


report = {"address": "test_address", "description": "nothing happened", "occurred": "1/1/1999 9:41pm",
            "reported": "13/3/1978 3:50pm", "status": "CLOSED", "type": "test"}
db.collection(u'crime-logs').add(report)


geolocater = Nominatim(user_agent = "harvardopendataproject")



# Extract and clean data
tables = camelot.read_pdf("test.pdf", pages = "1-end")
print(tables)

row_num = 0
cleaned_rows = []

for table in tables:
    for row in table.data[1:]:
        if row_num % 2 == 0:
            clean_row = [x for x in row if len(x) > 0]
            clean_row[3] = clean_row[3].replace("\n", " ")
            location = geolocater.geocode(clean_row[3])
            row_dict = {"reported": clean_row[0], "type": clean_row[1], "occurred": clean_row[2],
                        "address": clean_row[3], "status": clean_row[4], "location" : (location.latitude, location.longitude) if location != None else (0, 0)}
            cleaned_rows.append(row_dict)
            row_num += 1
        else:
            clean_row = [x for x in row if len(x) > 0]
            cleaned_rows[-1]["description"] = clean_row[0]
            row_num += 1

print(cleaned_rows)
