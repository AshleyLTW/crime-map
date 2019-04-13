import camelot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Set up a firebase instance
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

# Extract and clean data
tables = camelot.read_pdf("test.pdf", pages = "1-end")
print(tables)

row_num = 0
cleaned_rows = []

for table in tables:
    for row in table.data[1:]:
        if row_num % 2 == 0:
            clean_row = [x for x in row if len(x) > 0]
            row_dict = {"t_reported": clean_row[0], "type": clean_row[1], "t_occurred": clean_row[2],
                        "location": clean_row[3], "status": clean_row[4]}
            cleaned_rows.append(row_dict)
            row_num += 1
        else:
            clean_row = [x for x in row if len(x) > 0]
            cleaned_rows[-1]["description"] = clean_row[0]
            row_num += 1

print(cleaned_rows)
