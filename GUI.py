import sys
import string
import Tkinter
import Pmw
from Tkinter import *
from tkFileDialog import askopenfilename

class mainFrame:
	def __init__(self,root):
		frame=Frame(root)
		self.makeMenuBar(frame)
		self.txtfr(frame)
		frame.pack()
		return
	#defines the text area
	def txtfr(self,frame):
		textfr = Frame(frame)
		self.text = Text(textfr,height = 10,width = 50,background='white')
		scroll = Scrollbar(textfr)#Adding Scroll Bar
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return
	#defines menubar
	def makeMenuBar(self,frame):
		menubar = Frame(frame,relief = RAISED,borderwidth = 1)
		menubar.pack()
		mb_file = Menubutton(menubar,text = 'file')
		mb_file.pack(side = LEFT)
		mb_file.menu = Menu(mb_file)
		mb_file.menu.add_command(label = 'Open',command = self.file_open)
                mb_file.menu.add_command(label = 'Exit')#,command = destroy)
		mb_edit = Menubutton(menubar,text = 'edit')
		mb_edit.pack(side = LEFT)
		mb_edit.menu = Menu(mb_edit)
		mb_edit.menu.add_command(label = 'copy')
		mb_help = Menubutton(menubar,text = 'help')
		mb_help.pack(padx = 25,side = RIGHT)
		mb_file['menu'] = mb_file.menu
 		mb_edit['menu'] = mb_edit.menu
		return
	
        def convert(self,frame):
            print "File Successfully converted"

        #defines file_open which is called when file option openis choosen
	#displays the files giving the user choice to choose  file
	def file_open(self):
		root = Tk()
		filename =askopenfilename(filetypes=[("textfiles","*.txt")])
		print filename

              #create button to convert file:
                convertButton = Button(text='Convert') # change to Button(text='Convert',command = self.convert)
                convertButton.pack(side = BOTTOM)
 
"""
 self.dialog = 

"""

                

       


def main():
	root = Tk()
	k = mainFrame(root)
	root.title('Sentence Spliting Tool')
	root.mainloop()

if __name__ == '__main__':
    main()
