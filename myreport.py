from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

import csv

data_file = "data.csv"

def import_data(data_file):
    participant = csv.reader(open(data_file, 'rb'))
    for row in participant:
        first_name = row[0]
        last_name = row[1]
        position = row[2]
        pdf_file_name = first_name + last_name + '.pdf'
        generate_certificate(first_name, last_name, position, pdf_file_name)

def generate_certificate(first_name, last_name, position, pdf_file_name):
    participant_name = first_name + ' ' + last_name
    c= canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

    #Header Image
    c.drawImage("GCHeader1.jpeg", 0, 761, width=600, height=80)

    #header text
    c.setFont('Helvetica', 48, leading = None)
    c.drawCentredString(415, 500, 'Certificate of Completion')
    c.setFont('Helvetica', 24, leading = None)
    c.drawCentredString(415, 450, 'This Certificate is Presented to:')

    #participant name
    c.setFont('Helvetica-Bold', 34, leading = None)
    c.drawCentredString(415, 395, participant_name)

    #For participanting in.....
    c.setFont('Helvetica', 24, leading = None)
    c.drawCentredString(415, 350, 'For participating in the development of LMIS as the:')

    #position
    c.setFont('Helvetica', 20, leading = None)
    c.drawCentredString(415, 310, position)

    c.showPage()
    print 'writing'
    c.save()

import_data(data_file)

# def hello(c):
#     c.drawImage("GCHeader1.jpeg", 0, 761, width=600, height=80)
#     c.drawString(200, 700, "Welcome to GoodCitizen!")
# c = canvas.Canvas("hello.pdf")
# hello(c)





