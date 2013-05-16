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
		self.english_viewer(frame,root,'filename.txt')
		self.nepali_viewer(frame,root,'filename.txt')
		frame.pack()
		return
	#defines menubar

	def makeMenuBar(self,frame,root):
		menubar = Frame(frame,relief = RAISED,borderwidth = 1)
		menubar.pack()
		mb_file = Menubutton(menubar,text = 'File')
		mb_file.pack(side = LEFT)
		mb_file.menu = Menu(mb_file)
		mb_file.menu.add_command(label = 'Open English File',command = self.file_open_english(frame,root))
		mb_file.menu.add_command(label = 'Open Nepali  File',command = self.file_open_nepali(frame,root))
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



	def file_open_english(self,frame,root):
		
		root = Tk()
		filename =askopenfilename(filetypes=[("textfiles","*.txt")])
		self.english_viewer(frame,root,filename)
	def english_viewer(self,frame,root,filename):
		root = Tk()
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
		self.st.pack(padx = 5, pady = 5, expand = 1,side = RIGHT)
	
		Pmw.initialise(root)


	def file_open_nepali(self,frame,root):
		
		root = Tk()
		filename =askopenfilename(filetypes=[("textfiles","*.txt")])
		self.nepali_viewer(frame,root,filename)

	def nepali_viewer(self,frame,root,filename):

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
		self.st.pack(padx = 5, pady = 5, expand = 1,side = RIGHT)
		
		Pmw.initialise(root)

''' Class ends here '''

def main():
	root = Tk()
	k = mainFrame(root)
	root.title('Sentence Spliting Tool')

	#create button to convert file:
       	root.mainloop()

 
if __name__ == '__main__':
    main()
