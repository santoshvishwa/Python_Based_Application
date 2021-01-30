# -*- coding: utf-8 -*-
"""
To Install PDf Minor - pip install pdfminer.six
"""
# pdf _text Details (coord,x,y) and text

from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
#from Highlighter import createHighlight, addHighlightToPage

fp = open('D:\SD-8P-ST3\SD-8P-ST3 110818 DDR 16.pdf' , 'rb')

rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)

for page in pages:
    interpreter.process_page(page)
    layout = device.get_result()
    p = page.mediabox
    print("pdf_ccoordinates Size:",p) 
    for lobj in layout:
        if isinstance(lobj, LTTextBox):
            x0, y0, x1, y1, text = lobj.bbox[0],lobj.bbox[1],lobj.bbox[2], lobj.bbox[3], lobj.get_text()
            #print(x0, y0, x1, y1, text)
