"""
This is the main Python script for generating a PDF file using ReportLab
"""

# Imports
import sys
from pathlib import Path

# import the reportlab canvas object
from reportlab.pdfgen import canvas
# import pagesizes you might need
from reportlab.lib.pagesizes import A4
# we need these for importing TrueType Fonts (TTF)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Global variables

# Class declarations

# Function declarations

def main():
    # create a Canvas object with a filename
    c = canvas.Canvas("hello_world.pdf", pagesize=A4) 
    
    # location of our TTF file
    ttf = Path('fonts/Inter-ExtraBold.ttf')
    
    # Register a font before we use drawString
    pdfmetrics.registerFont(TTFont('Inter-ExtraBold', ttf))
    
    # Set the canvas font
    c.setFont('Inter-ExtraBold', 18)
    
    # Write text on the canvas
    c.drawString(50, 780, "Hello World")
    
    # What else can we do?
    # draw all kinds of shapes
    # a line
    c.line(60,750,500,750)
    
    # an arc
    c.arc(160, 700, 360, 550)
    
    # a circle
    c.circle(300, 500, 50, stroke=1, fill=0)
    
    # Save the current page of the canvas
    c.showPage()
    # Save the file to disk
    c.save()

# Main body
if __name__ == '__main__':
    main()