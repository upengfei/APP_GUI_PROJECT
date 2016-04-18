import wkhtmltopdf
import pdfkit
import os

pdfkit.from_file(os.getcwd() + r"/report/test_api.html", r"d:/test.pdf")