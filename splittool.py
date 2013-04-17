""" This Program Splits Sentences, works only with Linux OS """

import sys, getopt

def main(argv):
    filepath = ''
    outputfile = ''

    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'USAGE: test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'USAGE: test.py -i <inputfile> -o <outputfile>'
         print 'Alternatively, use test.py --ifile <inputfile> --ofile <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print 'Reading file ', inputfile;
    print 'Checking if output file ', outputfile, ' can be created'

    filepath = inputfile

    try:
	    fileName, fileExt = filepath.split('.')

    except IndexError:
	    print "No File Included"


    if fileExt != 'txt':
	    print "The input file must be a text file, ending in .txt"

    else:

	    try:
		    f = open(filepath,"r+")
	    except IOError:
		    print "Couldn't Open The File..."


	    try:
		    w = open(outputfile, "w")
	    except IOError:
		    print "Couldn't Write a File", outputfile

	    text = f.read()

	    NewText =  text.replace(". ",".\n")

	    w.write(NewText)

	    print "Splited text file saved in ", outputfile
	    
if __name__ == "__main__":
   main(sys.argv[1:])
