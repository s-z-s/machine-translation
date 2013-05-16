import codecs
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
infile = codecs.open(filename, "r", "utf8")
outfile = codecs.open("output.txt", "w", "utf8")
file = infile.read()
end = re.compile(ur'([\u0964]\s|[\u003F]\s|[\u0021]\s)', re.UNICODE)
split_sent = end.split(file)
i = 0
while(i<len(split_sent)):
    outfile.write(split_sent[i])
    if (len(split_sent[i])<3):
        outfile.write("\n")
    i = i + 1
print("Done. Please check the file output.txt",i)
