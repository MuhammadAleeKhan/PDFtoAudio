#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install pyttsx3
# pip install pdfminer
# pip install tkfilebrowser
# pip install PyPDF2 (optional)


# In[1]:


import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


# In[2]:


book = askopenfilename() # choose your PDF file


# In[3]:


def convert_pdf_to_txt():
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    FileReader = open(book, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0
    caching = True
    pagenos=set()
    
    for page in PDFPage.get_pages(FileReader, pagenos, maxpages=maxpages, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    FileReader.close()
    device.close()
    retstr.close()
    return text


# In[4]:


pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print("There are {} pages in this book.".format(pages))


# In[5]:


text = convert_pdf_to_txt()


# In[ ]:


audioplayer = pyttsx3.init()
audioplayer.say(text)
audioplayer.runAndWait()


# In[ ]:




