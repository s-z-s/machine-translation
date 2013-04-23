import re
infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
file = infile.read()
end = re.compile(r'([.?!]+\s)')
split_sent = end.split(file)
i = 0
while(i<len(split_sent)):
    outfile.write(split_sent[i])
    if (split_sent[i] == ". " or split_sent[i] == "! " or split_sent[i] == "? ") :
        outfile.write("\n")
    i = i + 1
print("Done. Please check the file ouput.txt")
