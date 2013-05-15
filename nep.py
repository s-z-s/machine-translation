import codecs
import re
infile = codecs.open("nepali.txt", "r", "utf8")
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
