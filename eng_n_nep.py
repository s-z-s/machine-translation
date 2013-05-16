import re
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()
eng_file = askopenfilename()

Tk().withdraw()
nep_file = askopenfilename()

infile = open(eng_file, 'r')
outfile = open('output_eng.txt', 'w')
file = infile.read()
eng = re.compile(r'(\S[0-9]+[.]+\s|[0-9]{0,9}[.]+\s|[a-z][.?!:][ ][a-z]|[.?!:][ ]|[A-Z][.]+\s|Adj[.]+\s|Adm[.]+\s|Adv[.]+\s|Asst[.]+\s|Bart[.]+\s|Bldg[.]+\s|Brig[.]+\s|Bros[.]+\s|Capt[.]+\s|Cmdr[.]+\s|Col[.]+\s|Comdr[.]+\s|Con[.]+\s|Corp[.]+\s|Cpl[.]+\s|DR[.]+\s|Dr[.]+\s|Drs[.]+\s|Ens[.]+\s|Gen[.]+\s|Gov[.]+\s|Hon[.]+\s|Hr[.]+\s|Hosp[.]+\s|i[.]e[.]+\s|Insp[.]+\s|Lt[.]+\s|MM[.]+\s|Mr[.]+\s |Mrs[.]+\s|Ms[.]+\s|Maj[.]+\s|Messrs[.]+\s|Mlle[.]+\s|Mme[.]+\s|Mr[.]+\s|Mrs[.]+\s|Ms[.]+\s|Msgr[.]+\s|Op[.]+\s|Ord[.]+\s|Pfc[.]+\s|Ph[.]+\s|Prof[.]+\s|Pvt[.]+\s|Rep[.]+\s|Reps[.]+\s|Res[.]+\s|Rev[.]+\s|Rt[.]+\s|Sen[.]+\s|Sens[.]+\s|Sfc[.]+\s|Sgt[.]+\s|Sr[.]+\s|St[.]+\s|Supt[.]+\s|Surg[.]+\s|v[.]+\s|vs[.]+\s|i[.]+\se[.]+\s|rev[.]+\s|e[.]g[.]+\s)')
split_eng = eng.split(file)
i = 0
while(i<len(split_eng)):
    outfile.write(split_eng[i])
    if (split_eng[i] == ". " or split_eng[i] == "! " or split_eng[i] == "? " or split_eng[i] == ": " or split_eng[i] == "^2. ") :
        outfile.write("\n")
    i = i + 1

infile = codecs.open(nep_file, "r", "utf8")
outfile = codecs.open("output_nep.txt", "w", "utf8")
file = infile.read()
nep = re.compile(ur'([\u0964]\s|[\u003F]\s|[\u0021]\s)', re.UNICODE)
split_nep = nep.split(file)

i = 0
while(i<len(split_nep)):
    outfile.write(split_nep[i])

    if (len(split_nep[i])<3):
        outfile.write("\n")
    i = i + 1

print("Done. Please check the file ouput.txt",i)
