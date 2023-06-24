# Import the required Module
import tabula
# Read a PDF File
# make sure your pdf file is in the same directory as your notebook
df = tabula.read_pdf("./pdfFiles/IPLmatch.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("./pdfFiles/IPLmatch.pdf", "./pdfFiles/iplmatch.csv", output_format="csv", pages='all')