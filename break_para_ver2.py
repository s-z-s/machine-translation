import re
infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
file = infile.read()
end = re.compile(r'(\S[0-9]+[.]+\s|[0-9]{0,9}[.]+\s|[a-z][.?!:][ ][a-z]|[.?!:][ ]|[A-Z][.]+\s|Adj[.]+\s|Adm[.]+\s|Adv[.]+\s|Asst[.]+\s|Bart[.]+\s|Bldg[.]+\s|Brig[.]+\s|Bros[.]+\s|Capt[.]+\s|Cmdr[.]+\s|Col[.]+\s|Comdr[.]+\s|Con[.]+\s|Corp[.]+\s|Cpl[.]+\s|DR[.]+\s|Dr[.]+\s|Drs[.]+\s|Ens[.]+\s|Gen[.]+\s|Gov[.]+\s|Hon[.]+\s|Hr[.]+\s|Hosp[.]+\s|i[.]e[.]+\s|Insp[.]+\s|Lt[.]+\s|MM[.]+\s|Mr[.]+\s |Mrs[.]+\s|Ms[.]+\s|Maj[.]+\s|Messrs[.]+\s|Mlle[.]+\s|Mme[.]+\s|Mr[.]+\s|Mrs[.]+\s|Ms[.]+\s|Msgr[.]+\s|Op[.]+\s|Ord[.]+\s|Pfc[.]+\s|Ph[.]+\s|Prof[.]+\s|Pvt[.]+\s|Rep[.]+\s|Reps[.]+\s|Res[.]+\s|Rev[.]+\s|Rt[.]+\s|Sen[.]+\s|Sens[.]+\s|Sfc[.]+\s|Sgt[.]+\s|Sr[.]+\s|St[.]+\s|Supt[.]+\s|Surg[.]+\s|v[.]+\s|vs[.]+\s|i[.]+\se[.]+\s|rev[.]+\s|e[.]g[.]+\s)')
split_sent = end.split(file)
i = 0
while(i<len(split_sent)):
    outfile.write(split_sent[i])
    if (split_sent[i] == ". " or split_sent[i] == "! " or split_sent[i] == "? " or split_sent[i] == ": " or split_sent[i] == "^2. ") :
        outfile.write("\n")
    i = i + 1
print("Done. Please check the file ouput.txt",i)
