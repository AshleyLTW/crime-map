from typing import List

import camelot
import csv
from os import listdir
from fnmatch import fnmatch
import re

# # Convert pdf to csv
# tables = camelot.read_pdf('test.pdf', pages='1-end')
#
# # Export all tables at once
# tables.export('output.csv', f='csv')
#
# # Export one table at a time
# # tables[1].to_csv('output.csv')

# Clean csv
fileList = []
for file in listdir('.'):
    if fnmatch(file, '*.csv'):
        fileList.append(file)

with open('output.csv', 'a', newline='') as outputFile:
    fieldnames = ['Date/Time Reported', 'Incident Type', 'Date/Time Occurred', 'Location', 'Disposition', 'Description']
    # writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
    writer = csv.writer(outputFile)
    # writer.writeheader()
    writer.writerow(fieldnames)

    # for file in fileList:
    #     with open(file, newline='') as csvFile:
    #         reader = csv.DictReader(csvFile, fieldnames=fieldnames)
    #         # Ignore first row (faulty headers)
    #         next(reader)
    #         # Check if second row is description or new incident
    #         row2 = next(reader)
    #         if re.search(r'\d/\d/\d\d', row2['Date/Time Reported']):
    #             mod = 0
    #         else:
    #             mod = 1
    #         # Iterate through pairs of rows and condense them into single row
    #         for row in reader:
    #             row_write = []
    #             if reader.line_num % 2 == mod:
    #                 # data line
    #                 row_write = [row['Date/Time Reported'], row['Incident Type'],
    #                              row['Date/Time Occurred'], row['Location'], row['Disposition']]
    #             else:
    #                 row_write.append(row['Date/Time Reported'])
    #                 writer.writerow(row_write)
    #             # print(write_row)