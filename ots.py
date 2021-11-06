import PyPDF2
import re
import glob
from pdfrw import PdfReader, PdfWriter
import os
try:
    os.mkdir('o')
except FileExistsError:
    print("delete folder o")
a = input("enter sachivalayam code :")
d = int(input("enter number of volunteers :"))
arr=[f for f in glob.glob("*.pdf")]
for i in arr:
	object = PyPDF2.PdfFileReader(open(i,'rb'))
umPages = object.getNumPages()
print("total pages:"+str(umPages))
for b in range(1,d+1):

    pa = []
    if b<10:
        String = a+"00"+str(b)
    else:
        String = a+"0"+str(b)
    print("volunteer"+String)
    for i in range(umPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        if re.search(String,Text):
             print("volunteer ID Found on Page: " + str(i+1))
             pa.append(i)

    for i in arr:
    	pages = PdfReader(i).pages
    	outdata = PdfWriter(f'o/{String}.pdf')
    	for part in pa:
    		outdata.addpage(pages[part])
    	outdata.write()
   
   
   




