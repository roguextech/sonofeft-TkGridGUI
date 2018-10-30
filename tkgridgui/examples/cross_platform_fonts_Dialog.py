#!/usr/bin/env python
# -*- coding: ascii -*-
from __future__ import print_function

# NOTICE... this file is generated by TkGridGUI.
# Any code or comments added by the user must be in designated areas ONLY.
# User additions will be lost if they are placed in code-generated areas.
# (i.e. Saving from TkGridGUI will over-write code-generated areas.)

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "imports"


from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

from tkinter.ttk import Combobox, Progressbar, Separator, Treeview, Notebook

from tkinter import *
from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, LabelFrame
from tkinter import Listbox, Message, Radiobutton, Spinbox, Text
from tkinter import OptionMenu
import tkinter.filedialog
from tkinter import _setit as set_command


# >>>>>>insert any user code below this comment for section "imports"
# Place any user import statements here
from tkinter.font import families, Font

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "top_of_init"

if sys.version_info < (3,):
    from tkSimpleDialog import Dialog
else:
    from tkinter.simpledialog import Dialog

class _Dialog(Dialog):
    # use dialogOptions dictionary to set any values in the dialog
    def __init__(self, parent, title = None, dialogOptions=None):
    
        self.dialogOptions = dialogOptions
        Dialog.__init__(self, parent, title)

class _cross_platform_fonts(_Dialog):

    def body(self, master):
        dialogframe = Frame(master, width=523, height=346)
        self.dialogframe = dialogframe
        dialogframe.pack()


        self.RadioGroup_1_StringVar = StringVar()

        self.make_Entry_2( self.dialogframe )          #       Entry:  at Main(1,2)
        self.make_LabelFrame_1( self.dialogframe )     #  LabelFrame: Attributes : at Main(2,4)
        self.make_Label_2( self.dialogframe )          #       Label:  at Main(4,1)
        self.make_Label_3( self.dialogframe )          #       Label: (see sample text above) : at Main(9,1)
        self.make_Label_4( self.dialogframe )          #       Label: ABCD efg 123.0 : at Main(8,1)
        self.make_Label_6( self.dialogframe )          #       Label: Courier 10 normal italic underline overstrike : at Main(0,1)
        self.make_Label_7( self.dialogframe )          #       Label:  at Main(2,3)
        self.make_Label_8( self.dialogframe )          #       Label: System Fonts : at Main(0,5)
        self.make_Listbox_1( self.dialogframe )        #     Listbox:  at Main(2,2)
        self.make_Listbox_2( self.dialogframe )        #     Listbox:  at Main(1,5)
        self.make_RadioGroup_1( self.dialogframe )     #  RadioGroup: Cross Platform Fonts : at Main(2,1)
        self.make_Checkbutton_1( self.LabelFrame_1 )   # Checkbutton: Bold : at LabelFrame_1(1,1)
        self.make_Checkbutton_2( self.LabelFrame_1 )   # Checkbutton: Italic : at LabelFrame_1(2,1)
        self.make_Checkbutton_3( self.LabelFrame_1 )   # Checkbutton: Underline : at LabelFrame_1(3,1)
        self.make_Checkbutton_4( self.LabelFrame_1 )   # Checkbutton: Overstrike : at LabelFrame_1(4,1)
        self.make_Radiobutton_1( self.RadioGroup_1 )   # Radiobutton: Courier : at RadioGroup_1(1,0)
        self.make_Radiobutton_2( self.RadioGroup_1 )   # Radiobutton: Helvetica : at RadioGroup_1(2,0)
        self.make_Radiobutton_3( self.RadioGroup_1 )   # Radiobutton: Times : at RadioGroup_1(3,0)
        self.make_Radiobutton_4( self.RadioGroup_1 )   # Radiobutton: TkDefaultFont : at RadioGroup_1(4,0)
        self.make_Radiobutton_5( self.RadioGroup_1 )   # Radiobutton: Platform Specific : at RadioGroup_1(6,0)
        self.make_Radiobutton_6( self.RadioGroup_1 )   # Radiobutton: Symbol : at RadioGroup_1(5,0)


        self.RadioGroup_1_StringVar.set("1")
        self.RadioGroup_1_StringVar_traceName = self.RadioGroup_1_StringVar.trace_variable("w", self.RadioGroup_1_StringVar_Callback)
        # >>>>>>insert any user code below this comment for section "top_of_init"

        self.RadioGroup_1_StringVar.set("2") # make Helvetica the default
        self.current_font_name = 'Helvetica'


        self.ignore_entry_change = False # used when Listbox sets Entry
        self.Entry_2_StringVar.set( '10' )
        
    def set_current_state(self):
        
        sL = [self.current_font_name]
        
        points = self.Entry_2_StringVar.get().strip()
        try:
            points = int( points.strip() )
        except:
            points = 10
        if points:
            sL.append( points )
        else:
            sL.append( 10 )
        
        if self.Checkbutton_1_StringVar.get() == 'yes':
            sL.append( 'bold' )
        else:
            sL.append( 'normal' )
        
        if self.Checkbutton_2_StringVar.get() == 'yes':
            sL.append( 'italic' )
        else:
            sL.append( 'roman' )
        
        if self.Checkbutton_3_StringVar.get() == 'yes':
            sL.append( 'underline' )
        
        if self.Checkbutton_4_StringVar.get() == 'yes':
            sL.append( 'overstrike' )

        self.full_font_desc = tuple( sL )
        self.Label_6.configure(text=self.full_font_desc)
        
        self.Label_4.configure(font=self.full_font_desc)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Entry_2"
    def make_Entry_2(self, frame):
        """       Entry:  at Main(1,2)"""
        self.Entry_2 = Entry( frame , width="4")
        self.Entry_2.grid(row=1, column=2, sticky="w")
        self.Entry_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Entry_2"

        self.Entry_2.configure(textvariable=self.Entry_2_StringVar)
        self.Entry_2_StringVar_traceName = self.Entry_2_StringVar.trace_variable("w", self.Entry_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_LabelFrame_1"
    def make_LabelFrame_1(self, frame):
        """  LabelFrame: Attributes : at Main(2,4)"""
        self.LabelFrame_1 = LabelFrame( frame , text="Attributes", width="60", height="50")
        self.LabelFrame_1.grid(row=2, column=4, sticky="n", rowspan="2")

        # >>>>>>insert any user code below this comment for section "make_LabelFrame_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_2"
    def make_Label_2(self, frame):
        """       Label:  at Main(4,1)"""
        self.Label_2 = Label( frame , text="", width="15")
        self.Label_2.grid(row=4, column=1)

        # >>>>>>insert any user code below this comment for section "make_Label_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_3"
    def make_Label_3(self, frame):
        """       Label: (see sample text above) : at Main(9,1)"""
        self.Label_3 = Label( frame , text="(see sample text above)", width="30")
        self.Label_3.grid(row=9, column=1, columnspan="5")

        # >>>>>>insert any user code below this comment for section "make_Label_3"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_4"
    def make_Label_4(self, frame):
        """       Label: ABCD efg 123.0 : at Main(8,1)"""
        self.Label_4 = Label( frame , text="ABCD efg 123.0", width="14")
        self.Label_4.grid(row=8, column=1, sticky="ew", columnspan="5")

        # >>>>>>insert any user code below this comment for section "make_Label_4"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_6"
    def make_Label_6(self, frame):
        """       Label: Courier 10 normal italic underline overstrike : at Main(0,1)"""
        self.Label_6 = Label( frame , text="Courier 10 normal italic underline overstrike", width="30", font="TkDefaultFont 12")
        self.Label_6.grid(row=0, column=1, sticky="ew", columnspan="4")

        # >>>>>>insert any user code below this comment for section "make_Label_6"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_7"
    def make_Label_7(self, frame):
        """       Label:  at Main(2,3)"""
        self.Label_7 = Label( frame , text="", width="3")
        self.Label_7.grid(row=2, column=3)

        # >>>>>>insert any user code below this comment for section "make_Label_7"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_8"
    def make_Label_8(self, frame):
        """       Label: System Fonts : at Main(0,5)"""
        self.Label_8 = Label( frame , text="System Fonts", width="15")
        self.Label_8.grid(row=0, column=5, sticky="s")

        # >>>>>>insert any user code below this comment for section "make_Label_8"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Listbox_1"
    def make_Listbox_1(self, frame):
        """     Listbox:  at Main(2,2)"""

        lbframe = Frame( frame )
        self.Listbox_1_frame = lbframe
        vbar=Scrollbar(lbframe, orient=VERTICAL)
        self.Listbox_1 = Listbox(lbframe, width="4", borderwidth="4", height="10", yscrollcommand=vbar.set)
        vbar.config(command=self.Listbox_1.yview)
        
        vbar.grid(row=0, column=1, sticky='ns')        
        self.Listbox_1.grid(row=0, column=0)

        self.Listbox_1_frame.grid(row=2, column=2, sticky="nsw")

        # >>>>>>insert any user code below this comment for section "make_Listbox_1"
        self.Listbox_1.configure( exportselection=False ) # stay highlighted after focus leaves


        # Edit the Listbox Entries
        self.font_sizeL = ["%i"%i for i in (list(range(6, 17)) + list(range(18, 32, 2)) + [42, 48, 54, 60, 72]  )]
        
        for s in self.font_sizeL:
            self.Listbox_1.insert(END, s)

        self.Listbox_1.bind("<ButtonRelease-1>", self.Listbox_1_Click)
        self.Listbox_1.bind('<<ListboxSelect>>', self.Listbox_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Listbox_2"
    def make_Listbox_2(self, frame):
        """     Listbox:  at Main(1,5)"""

        lbframe = Frame( frame )
        self.Listbox_2_frame = lbframe
        vbar=Scrollbar(lbframe, orient=VERTICAL)
        self.Listbox_2 = Listbox(lbframe, width="25", height="15", yscrollcommand=vbar.set)
        vbar.config(command=self.Listbox_2.yview)
        
        vbar.grid(row=0, column=1, sticky='ns')        
        self.Listbox_2.grid(row=0, column=0)

        self.Listbox_2_frame.grid(row=1, column=5, sticky="ns", rowspan="7")

        # >>>>>>insert any user code below this comment for section "make_Listbox_2"
        self.Listbox_2.configure( exportselection=False ) # stay highlighted after focus leaves

        self.sys_fonts = list(set(families()))
        self.sys_fonts.sort()

        for s in self.sys_fonts:
            self.Listbox_2.insert(END, s)

        self.Listbox_2.bind("<ButtonRelease-1>", self.Listbox_2_Click)
        self.Listbox_2.bind('<<ListboxSelect>>', self.Listbox_2_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_RadioGroup_1"
    def make_RadioGroup_1(self, frame):
        """  RadioGroup: Cross Platform Fonts : at Main(2,1)"""
        self.RadioGroup_1 = LabelFrame( frame , text="Cross Platform Fonts", width="60", height="50")
        self.RadioGroup_1.grid(row=2, column=1, sticky="n", rowspan="2")

        # >>>>>>insert any user code below this comment for section "make_RadioGroup_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Checkbutton_1"
    def make_Checkbutton_1(self, frame):
        """ Checkbutton: Bold : at LabelFrame_1(1,1)"""
        self.Checkbutton_1 = Checkbutton( frame , text="Bold", width="15", anchor="w")
        self.Checkbutton_1.grid(row=1, column=1)
        self.Checkbutton_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Checkbutton_1"

        self.Checkbutton_1.configure(variable=self.Checkbutton_1_StringVar, onvalue="yes", offvalue="no")
        self.Checkbutton_1_StringVar.set("no")
        self.Checkbutton_1_StringVar_traceName = self.Checkbutton_1_StringVar.trace_variable("w", self.Checkbutton_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Checkbutton_2"
    def make_Checkbutton_2(self, frame):
        """ Checkbutton: Italic : at LabelFrame_1(2,1)"""
        self.Checkbutton_2 = Checkbutton( frame , text="Italic", width="15", anchor="w")
        self.Checkbutton_2.grid(row=2, column=1)
        self.Checkbutton_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Checkbutton_2"

        self.Checkbutton_2.configure(variable=self.Checkbutton_2_StringVar, onvalue="yes", offvalue="no")
        self.Checkbutton_2_StringVar.set("no")
        self.Checkbutton_2_StringVar_traceName = self.Checkbutton_2_StringVar.trace_variable("w", self.Checkbutton_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Checkbutton_3"
    def make_Checkbutton_3(self, frame):
        """ Checkbutton: Underline : at LabelFrame_1(3,1)"""
        self.Checkbutton_3 = Checkbutton( frame , text="Underline", width="15", anchor="w")
        self.Checkbutton_3.grid(row=3, column=1)
        self.Checkbutton_3_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Checkbutton_3"

        self.Checkbutton_3.configure(variable=self.Checkbutton_3_StringVar, onvalue="yes", offvalue="no")
        self.Checkbutton_3_StringVar.set("no")
        self.Checkbutton_3_StringVar_traceName = self.Checkbutton_3_StringVar.trace_variable("w", self.Checkbutton_3_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Checkbutton_4"
    def make_Checkbutton_4(self, frame):
        """ Checkbutton: Overstrike : at LabelFrame_1(4,1)"""
        self.Checkbutton_4 = Checkbutton( frame , text="Overstrike", width="15", anchor="w")
        self.Checkbutton_4.grid(row=4, column=1)
        self.Checkbutton_4_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Checkbutton_4"

        self.Checkbutton_4.configure(variable=self.Checkbutton_4_StringVar, onvalue="yes", offvalue="no")
        self.Checkbutton_4_StringVar.set("no")
        self.Checkbutton_4_StringVar_traceName = self.Checkbutton_4_StringVar.trace_variable("w", self.Checkbutton_4_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_1"
    def make_Radiobutton_1(self, frame):
        """ Radiobutton: Courier : at RadioGroup_1(1,0)"""
        self.Radiobutton_1 = Radiobutton( frame , text="Courier", value="1", width="15", anchor="w")
        self.Radiobutton_1.grid(row=1, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_1"

        self.Radiobutton_1.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_2"
    def make_Radiobutton_2(self, frame):
        """ Radiobutton: Helvetica : at RadioGroup_1(2,0)"""
        self.Radiobutton_2 = Radiobutton( frame , text="Helvetica", value="2", width="15", anchor="w")
        self.Radiobutton_2.grid(row=2, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_2"

        self.Radiobutton_2.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_3"
    def make_Radiobutton_3(self, frame):
        """ Radiobutton: Times : at RadioGroup_1(3,0)"""
        self.Radiobutton_3 = Radiobutton( frame , text="Times", value="3", width="15", anchor="w")
        self.Radiobutton_3.grid(row=3, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_3"

        self.Radiobutton_3.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_4"
    def make_Radiobutton_4(self, frame):
        """ Radiobutton: TkDefaultFont : at RadioGroup_1(4,0)"""
        self.Radiobutton_4 = Radiobutton( frame , text="TkDefaultFont", value="4", width="15", anchor="w")
        self.Radiobutton_4.grid(row=4, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_4"

        self.Radiobutton_4.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_5"
    def make_Radiobutton_5(self, frame):
        """ Radiobutton: Platform Specific : at RadioGroup_1(6,0)"""
        self.Radiobutton_5 = Radiobutton( frame , text="Platform Specific", value="6", width="15", anchor="e")
        self.Radiobutton_5.grid(row=6, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_5"

        self.Radiobutton_5.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_6"
    def make_Radiobutton_6(self, frame):
        """ Radiobutton: Symbol : at RadioGroup_1(5,0)"""
        self.Radiobutton_6 = Radiobutton( frame , text="Symbol", value="5", width="15", anchor="w")
        self.Radiobutton_6.grid(row=5, column=0)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_6"

        self.Radiobutton_6.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Listbox_1_Click"
    def Listbox_1_Click(self, event): #bind method for component ID=Listbox_1
        """     Listbox:  at Main(2,2)"""
        pass
        # >>>>>>insert any user code below this comment for section "Listbox_1_Click"
        # replace, delete, or comment-out the following
        #print( "executed method Listbox_1_Click" )

        #print( "current selection(s) =",self.Listbox_1.curselection() )
        labelL = []
        for i in self.Listbox_1.curselection():
            labelL.append( self.Listbox_1.get(i))
        #print( "current label(s) =",labelL )
        
        if labelL:
            self.ignore_entry_change = True
            self.Entry_2_StringVar.set( labelL[0] )
            self.ignore_entry_change = False
        
        # use self.Listbox_1.insert(0, "item zero")
        #     self.Listbox_1.insert(index, "item i")
        #            OR
        #     self.Listbox_1.insert(END, "item end")
        #   to insert items into the list box
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Listbox_2_Click"
    def Listbox_2_Click(self, event): #bind method for component ID=Listbox_2
        """     Listbox:  at Main(1,5)"""
        pass
        # >>>>>>insert any user code below this comment for section "Listbox_2_Click"
        # replace, delete, or comment-out the following
        #print( "executed method Listbox_2_Click" )

        #print( "current selection(s) =",self.Listbox_2.curselection() )
        labelL = []
        for i in self.Listbox_2.curselection():
            labelL.append( self.Listbox_2.get(i))
        #print( "current label(s) =",labelL )
        # use self.Listbox_2.insert(0, "item zero")
        #     self.Listbox_2.insert(index, "item i")
        #            OR
        #     self.Listbox_2.insert(END, "item end")
        #   to insert items into the list box
        
        self.RadioGroup_1_StringVar.set("6") # make Helvetica the default
        if labelL:
            self.current_font_name = labelL[0]
            
        self.set_current_state()
        
        
        
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Entry_2_StringVar_traceName"
    def Entry_2_StringVar_Callback(self, varName, index, mode):
        """       Entry:  at Main(1,2)"""
        pass

        # >>>>>>insert any user code below this comment for section "Entry_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Entry_2_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Entry_2_StringVar.get() )

        self.set_current_state()

        if self.ignore_entry_change:
            return
            
        # Looks like a manual change, so try to change Listbox
        sval = self.Entry_2_StringVar.get().strip()
        try:
            ival = int( sval )
        except:
            ival = 0
            
        if ival and (sval in self.font_sizeL):
            index = self.font_sizeL.index( sval )
            
            self.Listbox_1.selection_clear(0, "end")
            self.Listbox_1.select_set( index )
            self.Listbox_1.see( index )


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Checkbutton_1_StringVar_traceName"
    def Checkbutton_1_StringVar_Callback(self, varName, index, mode):
        """ Checkbutton: Bold : at LabelFrame_1(1,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Checkbutton_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Checkbutton_1_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Checkbutton_1_StringVar.get() )

        self.set_current_state()

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Checkbutton_2_StringVar_traceName"
    def Checkbutton_2_StringVar_Callback(self, varName, index, mode):
        """ Checkbutton: Italic : at LabelFrame_1(2,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Checkbutton_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Checkbutton_2_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Checkbutton_2_StringVar.get() )
        self.set_current_state()



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Checkbutton_3_StringVar_traceName"
    def Checkbutton_3_StringVar_Callback(self, varName, index, mode):
        """ Checkbutton: Underline : at LabelFrame_1(3,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Checkbutton_3_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Checkbutton_3_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Checkbutton_3_StringVar.get() )
        self.set_current_state()



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Checkbutton_4_StringVar_traceName"
    def Checkbutton_4_StringVar_Callback(self, varName, index, mode):
        """ Checkbutton: Overstrike : at LabelFrame_1(4,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Checkbutton_4_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Checkbutton_4_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Checkbutton_4_StringVar.get() )
        self.set_current_state()



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "RadioGroup_1_StringVar_traceName"
    def RadioGroup_1_StringVar_Callback(self, varName, index, mode):
        """  RadioGroup: Cross Platform Fonts : at Main(2,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "RadioGroup_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "RadioGroup_1_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.RadioGroup_1_StringVar.get() )
        
        svar = self.RadioGroup_1_StringVar.get()
        
        if svar=='1':
            self.current_font_name = 'Courier'
        elif svar=='2':
            self.current_font_name = 'Helvetica'
        elif svar=='3':
            self.current_font_name = 'Times'
        elif svar=='4':
            self.current_font_name = 'TkDefaultFont'
        elif svar=='5':
            self.current_font_name = 'Symbol'

        elif svar=='6':
            labelL = []
            for i in self.Listbox_2.curselection():
                labelL.append( self.Listbox_2.get(i))
            if labelL:
                self.current_font_name = labelL[0]
            
        self.set_current_state()


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "dialog_validate"
    def validate(self):
        self.result = {} # return a dictionary of results
    

        self.result["Entry_2"] = self.Entry_2_StringVar.get()
        self.result["Checkbutton_1"] = self.Checkbutton_1_StringVar.get()
        self.result["Checkbutton_2"] = self.Checkbutton_2_StringVar.get()
        self.result["Checkbutton_3"] = self.Checkbutton_3_StringVar.get()
        self.result["Checkbutton_4"] = self.Checkbutton_4_StringVar.get()
        self.result["RadioGroup_1"] = self.RadioGroup_1_StringVar.get()

        # >>>>>>insert any user code below this comment for section "dialog_validate"
        # set values in "self.result" dictionary for return
        # for example...
        # self.result["age"] = self.Entry_2_StringVar.get() 

        self.result = {}
        t = self.full_font_desc
        self.result["full_font_desc"] = t # return the tuple
        self.result["full_font_str"] = t[0].replace(' ','\ ') + ' %i '%t[1] + ' '.join(t[2:])
        
        return 1
# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"


    def apply(self):
        pass
        #print( 'apply called' )

class _Testdialog:
    def __init__(self, master):
        frame = Frame(master, width=300, height=300)
        frame.pack()
        self.master = master
        self.x, self.y, self.w, self.h = -1,-1,-1,-1
        
        self.Button_1 = Button(text="Test Dialog", relief="raised", width="15")
        self.Button_1.place(x=84, y=36)
        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    def Button_1_Click(self, event): #click method for component ID=1
        dialog = _cross_platform_fonts(self.master, "Test Dialog")
        print( '===============Result from Dialog====================' )
        print( dialog.result )
        print( '=====================================================' )

def main():
    root = Tk()
    app = _Testdialog(root)
    root.mainloop()

if __name__ == '__main__':
    main()
