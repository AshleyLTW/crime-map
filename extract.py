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
#
# Clean csv
fileList = []
for file in listdir('.'):
    if fnmatch(file, '*.csv'):
        fileList.append(file)

with open('output.csv', 'a', newline='') as outputFile:
    fieldnames = ['Date/Time Reported', 'Incident Type', 'Date/Time Occurred', 'Location', 'Disposition', 'Description']
    # writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
    # writer.writeheader()
    writer = csv.writer(outputFile)
    writer.writerow(fieldnames)
    row_num = 0
    for file in fileList:
        with open(file, newline='') as csvFile:
            # reader = csv.DictReader(csvFile, fieldnames=fieldnames)
            reader = csv.reader(csvFile)
            # Ignore first row (faulty headers)
            csvFile.seek(0)
            next(reader)
            # Check if second row is description or new incident
            # row2 = next(reader)
            # print(row2)
            # if re.search(r'\d/\d/\d\d', row2['Date/Time Reported']):
            # if re.search(r'\d/\d/\d\d', row2[0]):
            #     mod = 0
            # else:
            #     mod = 1
            # Iterate through pairs of rows and condense them into single row
            temp_row = []
            for row in reader:
                if len(row) == 0:
                    continue
                elif row[0] == 'Date/Time Reported':
                    continue
                else:
                    if row_num % 2 == 0:
                        temp_row = row
                    else:
                        temp_row.append(row[0])
                        writer.writerow(temp_row)
                    row_num += 1
                    print(row)

                # row_write = []
                # print(row)
                # if reader.line_num % 2 == 0:
                #     # data line
                #     # row_write = [row['Date/Time Reported'], row['Incident Type'],
                #     #              row['Date/Time Occurred'], row['Location'], row['Disposition']]
                #     row_write = row
                # else:
                #     row_write.append(row[0])
                # # print(write_row)