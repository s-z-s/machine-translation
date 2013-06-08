import wx
import re
import codecs

class mine(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Statistical Machine Translation',wx.DefaultPosition, wx.Size(600,400), wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetBackgroundColour("gray")
        status = self.CreateStatusBar()
        panel = wx.Panel(self)

        self.eng_fileisopen = False
        self.nep_fileisopen = False

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

    def open_eng_file(self,event):
        filedialog = wx.FileDialog(self,
            message = 'Open English file',
            defaultDir = '.',
            defaultFile = 'TestTOC.txt',
            wildcard = 'Textfile (.txt .prn)|*.txt;*.prn|All (.*)|*.*', #!!!!
            style = wx.OPEN)
        if filedialog.ShowModal() == wx.ID_OK:
            self.eng_file_input = filedialog.GetPath()
            self.eng_fileisopen = True
        infile_for_eng = open(self.eng_file_input, 'r')
        read_out_eng = infile_for_eng.read()
        self.textdisplay_eng = wx.TextCtrl(self, -1, pos = (0,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (292,320))
        self.textdisplay_eng.SetValue(read_out_eng)
        infile_for_eng.close()

    def open_nep_file(self,event):
        filedialog = wx.FileDialog(self,
            message = 'Open Nepali file',
            defaultDir = '.',
            defaultFile = 'TestTOC.txt',
            wildcard = 'Textfile (.txt .prn)|*.txt;*.prn|All (.*)|*.*', #!!!!
            style = wx.OPEN)
        if filedialog.ShowModal() == wx.ID_OK:
            self.nep_file_input = filedialog.GetPath()
            self.nep_fileisopen = True
        infile_for_nep = open(self.nep_file_input, 'r')
        read_out_nep = infile_for_nep.read()
        self.textdisplay_nep = wx.TextCtrl(self, -1, pos = (293,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (292,320))
        bytes = read_out_nep
        unicode_value = bytes.decode('utf-8')
        self.textdisplay_nep.SetValue(unicode_value)
        infile_for_nep.close()

    def exit_program(self,event):
        self.Close(True)

    def align_sentence(self,event):
        if self.eng_fileisopen == True & self.nep_fileisopen == True:
            if self.bitmap_is_there == True:
                self.bitmap.Destroy()
                self.bitmap_is_there = False
            infile_for_eng = open(self.eng_file_input, 'r')
            eng_file_read = infile_for_eng.read()
            infile_for_nep = codecs.open(self.nep_file_input, "r", "utf8")
            nep_file_read = infile_for_nep.read()
            outfile_eng = open('output_eng.txt', 'w')
            eng = re.compile(r'([.:?!]+\s+[0-9]{0,9}[.]+\s|[a-z][.?!:][ ][a-z]|[.?!:][ ]|[A-Z][.]+\s|Adj[.]+\s|Adm[.]+\s|Adv[.]+\s|Asst[.]+\s|Bart[.]+\s|Bldg[.]+\s|Brig[.]+\s|Bros[.]+\s|Capt[.]+\s|Cmdr[.]+\s|Col[.]+\s|Comdr[.]+\s|Con[.]+\s|Corp[.]+\s|Cpl[.]+\s|DR[.]+\s|Dr[.]+\s|Drs[.]+\s|Ens[.]+\s|Gen[.]+\s|Gov[.]+\s|Hon[.]+\s|Hr[.]+\s|Hosp[.]+\s|i[.]e[.]+\s|Insp[.]+\s|Lt[.]+\s|MM[.]+\s|Mr[.]+\s |Mrs[.]+\s|Ms[.]+\s|Maj[.]+\s|Messrs[.]+\s|Mlle[.]+\s|Mme[.]+\s|Mr[.]+\s|Mrs[.]+\s|Ms[.]+\s|Msgr[.]+\s|Op[.]+\s|Ord[.]+\s|Pfc[.]+\s|Ph[.]+\s|Prof[.]+\s|Pvt[.]+\s|Rep[.]+\s|Reps[.]+\s|Res[.]+\s|Rev[.]+\s|Rt[.]+\s|Sen[.]+\s|Sens[.]+\s|Sfc[.]+\s|Sgt[.]+\s|Sr[.]+\s|St[.]+\s|Supt[.]+\s|Surg[.]+\s|v[.]+\s|vs[.]+\s|i[.]+\se[.]+\s|rev[.]+\s|e[.]g[.]+\s)')
            split_eng = eng.split(eng_file_read)
            i = 0
            j = 1
            self.textdisplay_eng.Destroy()
            self.textdisplay_nep.Destroy()
            while(i<len(split_eng)):
                if i == 0:
                    sep = "."
                    numbering = sep.join((str(j), ' '))
                    outfile_eng.write(numbering)
                outfile_eng.write(split_eng[i])
                if (split_eng[i] == ". " or split_eng[i] == "! " or split_eng[i] == "? ") :
                    j=j+1
                    sep = "."
                    numbering = sep.join((str(j), ' '))
                    outfile_eng.write("\n\n")
                    outfile_eng.write(numbering)
                i = i + 1
            outfile_eng.close()

            self.textdisplay_eng = wx.TextCtrl(self, -1, pos = (0,0), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size = (292,320))
            read_out_eng = open('output_eng.txt', 'r')
            disp_out_eng = read_out_eng.read()
            self.textdisplay_eng.SetValue(disp_out_eng)

            outfile_nep = codecs.open("output_nep.txt", "w", "utf8")
            nep = re.compile(ur'([\u0964]\s|[\u003F]\s|[\u0021]\s)', re.UNICODE)
            split_nep = nep.split(nep_file_read)

            i = 0
            j = 1
            while(i<len(split_nep)):
                if i == 0:
                    sep = "."
                    numbering = sep.join((str(j), ' '))
                    outfile_nep.write(numbering)
                outfile_nep.write(split_nep[i])
                if (len(split_nep[i])<3):
                    j=j+1
                    sep = "."
                    numbering = sep.join((str(j), ' '))
                    outfile_nep.write("\n\n")
                    outfile_nep.write(numbering)
                i = i + 1
            outfile_nep.close()

            self.textdisplay_nep = wx.TextCtrl(self, -1, pos = (293,0), style = wx.TE_MULTILINE|wx.TE_READONLY | wx.TE_RICH2, size = (292,320))
            read_out_nep = open('output_nep.txt', 'r')
            disp_out_nep = read_out_nep.read()
            bytes = disp_out_nep
            unicode_value = bytes.decode('utf-8')
            self.textdisplay_nep.SetValue(unicode_value)
        else:
            dlg = wx.MessageDialog(self, "Please select both parallel files from the file option.","File not selected", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
            dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok or cancel
            dlg.Destroy()

    def align_phrase(self,event):
        dlg = wx.MessageDialog(self, "This option is still under construction. Please check back after a few days.","Option not available", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
        dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok
        dlg.Destroy()

    def align_word(self,event):
        dlg = wx.MessageDialog(self, "This option is still under construction. Please check back after a few days.","Option not available", wx.OK)  # create a dialog (dlg) box to display the message, and ok button
        dlg.ShowModal()  # show the dialog box, modal means cannot do anything on the program until clicks ok
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
