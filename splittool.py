""" This Program Splits Sentences, works only with Linux OS """

filepath = raw_input("Type the text file with the full path")

try:
	fileName, fileExt = filepath.split('.')	

except IndexError:
	print "No File Included"




if fileExt != '.txt':
	print "The File is Not .txt"


else:

	try:
		f = open(filepath,"r+")
	except IOError:
		print "Couldn't Open The File..."


	try:
		w = open("/tmp/splitedtext.txt","w+")
	except IOError:
		print "Couldn't Write a File /temp/splitedtext.txt"

	text = f.read()

	NewText =  text.replace(". ",".\n")

	w.write(NewText)

	print "Splited text file saved in /tmp/splitedtext.txt"
