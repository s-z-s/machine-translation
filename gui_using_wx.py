import wx
import re
import codecs
from xml.dom import minidom



class mine(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Statistical Machine Translation',wx.DefaultPosition, wx.Size(600,400), wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetBackgroundColour("gray")
        status = self.CreateStatusBar()
        panel = wx.Panel(self)

        self.define_all(self)

        pic = wx.Image("image.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, pic, (0,0), (pic.GetWidth(), pic.GetHeight()))
        self.bitmap_is_there = True

        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        third = wx.Menu()
        eng_file = first.Append(wx.NewId(), "Open English File", "Click to open the English text file.")
        nep_file = first.Append(wx.NewId(), "Open Nepali File", "Click to open the Nepali text file.")
        exit = first.Append(wx.NewId(), "Exit", "Click to exit the program.")
        sentence_level = second.Append(wx.NewId(), "Sentence Level", "Aligns parallel texts in sentence level.")
        phrase_level = second.Append(wx.NewId(), "Phrase Level", "Aligns parallel texts in phrase level.")
        word_level = second.Append(wx.NewId(), "Word Level", "Aligns parallel texts in word level.")
        about_dev = third.Append(wx.NewId(), "About Developers", "Click to know about the developers.")
        how_to_use = third.Append(wx.NewId(), "How to Use", "Click to get help about how to use this application")
        menubar.Append(first,"File")
        menubar.Append(second,"Align")
        menubar.Append(third,"Help")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.open_eng_file, eng_file)
        self.Bind(wx.EVT_MENU, self.open_nep_file, nep_file)
        self.Bind(wx.EVT_MENU, self.exit_program, exit)
        self.Bind(wx.EVT_MENU, self.align_sentence, sentence_level)
        self.Bind(wx.EVT_MENU, self.align_phrase, phrase_level)
        self.Bind(wx.EVT_MENU, self.align_word, word_level)
        self.Bind(wx.EVT_MENU, self.developers, about_dev)
        self.Bind(wx.EVT_MENU, self.help, how_to_use)

    def define_all(self, event):
        self.bitmap_is_there = False
        self.eng_file_is_open = False
        self.nep_file_is_open = False
        self.eng_textbox_present = False
        self.nep_textbox_present = False
        self.sentences_are_aligned = False
        self.text_box_is_to_be_shown = False
        self.another_file = False
        print ("defined all")

    def open_eng_file(self,event):
        if (self.eng_textbox_present == True):
            self.textdisplay_eng.Destroy()
            self.eng_textbox_present = False

        filedialog = wx.FileDialog(self,
            message = 'Open English file',
            defaultDir = '.',
            defaultFile = 'input.txt',
            wildcard = 'Textfile (.txt .prn)|*.txt;*.prn|All (.*)|*.*', #!!!!
            style = wx.OPEN)
        if filedialog.ShowModal() == wx.ID_OK:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            self.eng_file_input = filedialog.GetPath()
            self.eng_file_is_open = True
            infile_for_eng = open(self.eng_file_input, 'r')
            read_out_eng = infile_for_eng.read()
            self.textdisplay_eng = wx.TextCtrl(self, -1, pos = (0,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (300,330))
            self.textdisplay_eng.SetValue(read_out_eng)
            self.eng_textbox_present = True
            self.another_file = True
            self.sentences_are_aligned = False
            infile_for_eng.close()

    def open_nep_file(self,event):
        if (self.nep_textbox_present == True):
            self.textdisplay_nep.Destroy()
            self.nep_textbox_present = False

        filedialog = wx.FileDialog(self,
            message = 'Open Nepali file',
            defaultDir = '.',
            defaultFile = 'inout2.txt',
            wildcard = 'Textfile (.txt .prn)|*.txt;*.prn|All (.*)|*.*', #!!!!
            style = wx.OPEN)
        if filedialog.ShowModal() == wx.ID_OK:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            self.nep_file_input = filedialog.GetPath()
            self.nep_file_is_open = True
            infile_for_nep = open(self.nep_file_input, 'r')
            read_out_nep = infile_for_nep.read()
            self.textdisplay_nep = wx.TextCtrl(self, -1, pos = (300,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (295,330))
            bytes = read_out_nep
            unicode_value = bytes.decode('utf-8')
            self.textdisplay_nep.SetValue(unicode_value)
            self.nep_textbox_present = True
            self.another_file = True
            self.sentences_are_aligned = False
            infile_for_nep.close()

    def exit_program(self,event):
        self.Close(True)

    def align_sentence(self,event):
        self.text_box_is_to_be_shown = True
        self.align_sentence_now(event)

    def align_sentence_now(self,event):
        if self.eng_file_is_open == True & self.nep_file_is_open == True:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            infile_for_eng = open(self.eng_file_input, 'r')
            eng_file_read = infile_for_eng.read()
            infile_for_nep = codecs.open(self.nep_file_input, "r", "utf8")
            nep_file_read = infile_for_nep.read()
            outfile_eng = open('output_eng.txt', 'w')
            eng = re.compile(r'([.]+\n+\n|[.:?!]+\s+[0-9]{0,9}[.]+\s|[a-z][.?!:][ ][a-z]|[.?!:][ ]|[A-Z][.]+\s|Adj[.]+\s|Adm[.]+\s|Adv[.]+\s|Asst[.]+\s|Bart[.]+\s|Bldg[.]+\s|Brig[.]+\s|Bros[.]+\s|Capt[.]+\s|Cmdr[.]+\s|Col[.]+\s|Comdr[.]+\s|Con[.]+\s|Corp[.]+\s|Cpl[.]+\s|DR[.]+\s|Dr[.]+\s|Drs[.]+\s|Ens[.]+\s|Gen[.]+\s|Gov[.]+\s|Hon[.]+\s|Hr[.]+\s|Hosp[.]+\s|i[.]e[.]+\s|Insp[.]+\s|Lt[.]+\s|MM[.]+\s|Mr[.]+\s |Mrs[.]+\s|Ms[.]+\s|Maj[.]+\s|Messrs[.]+\s|Mlle[.]+\s|Mme[.]+\s|Mr[.]+\s|Mrs[.]+\s|Ms[.]+\s|Msgr[.]+\s|Op[.]+\s|Ord[.]+\s|Pfc[.]+\s|Ph[.]+\s|Prof[.]+\s|Pvt[.]+\s|Rep[.]+\s|Reps[.]+\s|Res[.]+\s|Rev[.]+\s|Rt[.]+\s|Sen[.]+\s|Sens[.]+\s|Sfc[.]+\s|Sgt[.]+\s|Sr[.]+\s|St[.]+\s|Supt[.]+\s|Surg[.]+\s|v[.]+\s|vs[.]+\s|i[.]+\se[.]+\s|rev[.]+\s|e[.]g[.]+\s)')
            split_eng = eng.split(eng_file_read)
            i = 0
            j = 1
            p = 1
            if (self.eng_textbox_present == True):
                self.textdisplay_eng.Destroy()
                self.eng_textbox_present = False
            if (self.nep_textbox_present == True):
                self.textdisplay_nep.Destroy()
                self.nep_textbox_present = False
            while(i<len(split_eng)):
                if i == 0:
                    sep = "."
                    para = " "
                    sent_numbering = sep.join((str(j), ' '))
                    para_numbering = para.join(('Paragraph:', str(p),'\n'))
                    outfile_eng.write(para_numbering)
                    outfile_eng.write(sent_numbering)
                outfile_eng.write(split_eng[i])
                if (split_eng[i] == ". " or split_eng[i] == "! " or split_eng[i] == "? " or split_eng[i] == ".\n\n") :
                    if (split_eng[i] == ".\n\n"):
                        p = p + 1
                        para = " "
                        para_numbering = para.join(('Paragraph:', str(p)))
                        outfile_eng.write(para_numbering)
                    j = j + 1
                    sep = "."
                    sent_numbering = sep.join((str(j), ' '))
                    outfile_eng.write("\n\n")
                    outfile_eng.write(sent_numbering)
                i = i + 1
            outfile_eng.close()

            outfile_nep = codecs.open("output_nep.txt", "w", "utf8")
            nep = re.compile(ur'([\u0964]+\n+\n|[\u0964]\s|[\u003F]\s|[\u0021]\s)', re.UNICODE)
            split_nep = nep.split(nep_file_read)

            i = 0
            j = 1
            p = 1
            while(i<len(split_nep)):
                #if split_nep[i] == "
                if i == 0:
                    sep = "."
                    sent_numbering = sep.join((str(j), ' '))
                    outfile_nep.write(sent_numbering)
                outfile_nep.write(split_nep[i])
                if (len(split_nep[i])<3):
                    j=j+1
                    sep = "."
                    sent_numbering = sep.join((str(j), ' '))
                    outfile_nep.write("\n\n")
                    outfile_nep.write(sent_numbering)
                i = i + 1
            outfile_nep.close()
            self.sentences_are_aligned = True
            self.another_file = False

            if (self.text_box_is_to_be_shown == True):
                self.display_text_box(event)

        else:
            dlg = wx.MessageDialog(self, "Please select both parallel files from the file option.","File not selected", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
            dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok or cancel
            dlg.Destroy()

    def display_text_box(self,event):
        self.textdisplay_eng = wx.TextCtrl(self, -1, pos = (0,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (300,330))
        read_out_eng = open('output_eng.txt', 'r')
        disp_out_eng = read_out_eng.read()
        self.textdisplay_eng.SetValue(disp_out_eng)
        self.eng_textbox_present = True

        self.textdisplay_nep = wx.TextCtrl(self, -1, pos = (300,0), style = wx.TE_MULTILINE|wx.TE_READONLY | wx.TE_RICH2, size = (295,330))
        read_out_nep = open('output_nep.txt', 'r')
        disp_out_nep = read_out_nep.read()
        bytes = disp_out_nep
        unicode_value = bytes.decode('utf-8')
        self.textdisplay_nep.SetValue(unicode_value)
        self.nep_textbox_present = True

        self.text_box_is_to_be_shown = False

    def align_phrase(self,event):
        dlg = wx.MessageDialog(self, "This option is still under construction. Please check back after a few days.","Option not available", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
        dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok
        dlg.Destroy()

    def align_word(self,event):
        if (self.eng_textbox_present == True):
            self.textdisplay_eng.Destroy()
            self.eng_textbox_present = False
            print("destroy ta bhakai ho!!!")
        if (self.nep_textbox_present == True):
            self.textdisplay_nep.Destroy()
            self.nep_textbox_present = False
        if self.eng_file_is_open == True & self.nep_file_is_open == True:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            if  (self.another_file == False):
                if (self.sentences_are_aligned == True):
                    print("already aligned")
                    self.align_word_now(event)
                else:
                    self.align_sentence_now(event)
                    print("aligned just now")
                    self.align_word_now(event)
            else:
                self.align_sentence_now(event)
                print("naya lai sudda align garne bhaisakyo yar!!! :D")
                self.align_word_now(event)
        else:
            dlg = wx.MessageDialog(self, "Please select both parallel files from the file option.","File not selected", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
            dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok or cancel
            dlg.Destroy()

    def align_word_now(self,event):
        print("the word align begins")

        i = 0
        j = 0
        if self.eng_file_is_open == True & self.nep_file_is_open == True:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            if (self.eng_textbox_present == True):
                self.textdisplay_eng.Destroy()
                self.eng_textbox_present = False
                print("destroy ta bhakai ho!!!")
            if (self.nep_textbox_present == True):
                self.textdisplay_nep.Destroy()
                self.nep_textbox_present = False
            pic = wx.Image("loading.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
            self.bitmap = wx.StaticBitmap(self, -1, pic, (0,0), (pic.GetWidth(), pic.GetHeight()))

            xmldoc = minidom.parse('dictionary.xml')
            dictionary_eng = open('dictionary.txt', 'r')
            outfile_eng = open('output_eng.txt', 'w')
            outfile_nep = codecs.open("output_nep.txt", "w", "utf8")
            dictionary_eng_read = dictionary_eng.read()
            dictionary_compile = re.compile(r' ')
            word_list = dictionary_compile.split(dictionary_eng_read)

            eng_string = open(self.eng_file_input,'r')
            eng_string_read = eng_string.read()
            string_break = re.compile('[.]+\s|[ ]')
            string_split = string_break.split(eng_string_read)
            print ("start of loop")
            b = 1
            a = 0
            sep = "."
            while (j < (len(string_split))):
                string1 = string_split[j].lower()
                print j
                i = 0
                while (i < len(word_list)):
                    if a == 0:
                        sent_numbering = sep.join((str(b), ' '))
                        outfile_eng.write(sent_numbering)
                        outfile_nep.write(sent_numbering)
                        a = a + 1
                    if (string1 == word_list[i]):
                        b = b + 1
                        nep_translation = xmldoc.getElementsByTagName('nepali')[i].firstChild.data

                        outfile_eng.write(string_split[j])
                        outfile_eng.write("\n")
                        sent_numbering = sep.join((str(b),' '))
                        outfile_eng.write(sent_numbering)

                        outfile_nep.write(nep_translation)
                        outfile_nep.write("\n")
                        sent_numbering = sep.join((str(b),' '))
                        outfile_nep.write(sent_numbering)
                        break;
                    i = i+1
                    print i
                j = j+1
            outfile_eng.close()
            outfile_nep.close()
            self.bitmap.Destroy()

            self.textdisplay_eng = wx.TextCtrl(self, -1, pos = (0,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (300,330))
            read_out_eng = open('output_eng.txt', 'r')
            disp_out_eng = read_out_eng.read()
            self.textdisplay_eng.SetValue(disp_out_eng)

            self.textdisplay_nep = wx.TextCtrl(self, -1, pos = (300,0), style = wx.TE_MULTILINE|wx.TE_READONLY | wx.TE_RICH2, size = (295,330))
            read_out_nep = open('output_nep.txt', 'r')
            disp_out_nep = read_out_nep.read()
            bytes = disp_out_nep
            unicode_value = bytes.decode('utf-8')
            self.textdisplay_nep.SetValue(unicode_value)
        else:
            dlg = wx.MessageDialog(self, "Please select both parallel files from the file option.","File not selected", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
            dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok or cancel
            dlg.Destroy()


    def developers(self,event):
        dlg = wx.MessageDialog(self, "I am the developer!!! B) :P","About Developers", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
        dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok
        dlg.Destroy()

    def help(self,event):
        dlg = wx.MessageDialog(self, "From File, select two parallel files and then from align option, align them using the appropriate option.","How to Use", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
        dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok or cancel
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = mine(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
