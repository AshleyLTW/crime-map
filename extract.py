import camelot

tables = camelot.read_pdf('test.pdf', pages='1-end')

# Export all tables at once
# tables.export('output.csv', f='csv')

# Export one table at a time
tables[1].to_csv('output.csv')

# Things to consider:
# Export all of the tables at once in a zip file and then unzip
# Export them one by one and then manipulate them?