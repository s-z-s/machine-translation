""" This Program Splits Sentences """

f = open("/home/bob/Desktop/Test.txt","r+")
w = open("/home/bob/Desktop/TestNew.txt","w+")

text = f.read()

NewText =  text.replace(".",".\n")

w.write(NewText)
