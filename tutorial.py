# # https://automatetheboringstuff.com/chapter13/
# # https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
#
# # import PyPDF2
# import textract
# #
# # pdfFileObj = open('test.pdf', 'rb')
# # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # pageObj = pdfReader.getPage(0)
# # pageObj.extractText()
#
# text = textract.process('./test.pdf')
#

# https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302
# from tabula import read_pdf

# df = read_pdf("test.pdf")

from tabula import convert_into

convert_into("test.pdf", "output.csv", output_format="csv")
