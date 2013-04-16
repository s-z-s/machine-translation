""" This Program Splits Sentences """

try:
	f = open("/home/bob/Desktop/Test.txt","r+")
except IOError:
	print "Couldn't Open The File..."

try:
	w = open("/temp/splitedtext.txt","w+")
except:
	print "Couldn't Write a File in /temp/splitedtext.txt"

text = f.read()

NewText =  text.replace(".",".\n")

w.write(NewText)
