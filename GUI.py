import sys
import string
import Tkinter
import Pmw
from Tkinter import *
from tkFileDialog import askopenfilename

class mainFrame:


	def __init__(self,root):
		frame=Frame(root)
		self.makeMenuBar(frame,root)
#		self.txtfr(frame)
		frame.pack()
		return
	#defines menubar

	def makeMenuBar(self,frame,root):
		menubar = Frame(frame,relief = RAISED,borderwidth = 1)
		menubar.pack()
		mb_file = Menubutton(menubar,text = 'File')
		mb_file.pack(side = LEFT)
		mb_file.menu = Menu(mb_file)
		mb_file.menu.add_command(label = 'Open',command = self.file_open(frame))
                mb_file.menu.add_command(label = 'Exit',command = root.destroy)
		mb_edit = Menubutton(menubar,text = 'Edit')
		mb_edit.pack(side = LEFT)
		mb_edit.menu = Menu(mb_edit)
		mb_edit.menu.add_command(label = 'Copy')
		mb_help = Menubutton(menubar,text = 'Help')
		mb_help.pack(padx = 25,side = RIGHT)
		mb_file['menu'] = mb_file.menu
 		mb_edit['menu'] = mb_edit.menu
		return
	

        def convert(self):
            print "File Successfully converted"

	#displays the files giving the user choice to choose  file
	def file_open(self,frame):
		
		root = Tk()
		filename =askopenfilename(filetypes=[("textfiles","*.txt")])

		fixedFont = Pmw.logicalfont('Fixed')
		self.st = Pmw.ScrolledText(frame,
			  labelpos = 'n',
			  label_text=filename,


		          usehullsize = 1,
		          hull_width = 700,
		          hull_height = 500,
		          text_wrap='none',
		          text_font = fixedFont,

		           text_padx = 4,
		           text_pady = 4,)
	   
		self.st.importfile(filename);
		self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

		Pmw.initialise(root)
   

        # Prevent users' modifying text and headers
#	self.st.configure(text_state = 'disabled')

 





"""
 self.dialog = 

"""

                

       


def main():
	root = Tk()
	k = mainFrame(root)
	root.title('Sentence Spliting Tool')

	             #create button to convert file:
        convertButton = Tkinter.Button(root,text='Convert') # change to Button(text='Convert',command = self.convert)
        convertButton.pack(side = BOTTOM)
	root.mainloop()

 
if __name__ == '__main__':
    main()






""" 
    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)

---------------------------------------------------------------------------------
#This Is Not Needed For Now,

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

"""


