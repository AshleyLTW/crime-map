import camelot
tables = camelot.read_pdf('https://www.hupd.harvard.edu/files/hupd/files/040219.pdf')
tables.export('foo.csv', f='csv')
