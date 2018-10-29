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

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "top_of_init"
class _full_combo:
    def __init__(self, master):
    
        grid_frame = Frame( master )
        self.grid_frame = grid_frame
        grid_frame.pack(expand=1, fill=BOTH)
        self.master = master
        
        self.x, self.y, self.w, self.h = 10, 10, 519, 326

        self.master.title("full_combo")

        self.RadioGroup_1_StringVar = StringVar()

        self.make_Button_1( self.grid_frame )          #      Button:  at Main(1,1)
        self.make_Notebook_1( self.grid_frame )        #    Notebook:  at Main(1,2)
        self.make_Tab_1( self.Notebook_1 )             #         Tab: Small : at Notebook_1(1,1)
        self.make_Tab_2( self.Notebook_1 )             #         Tab: Medium : at Notebook_1(1,2)
        self.make_Tab_3( self.Notebook_1 )             #         Tab: Large : at Notebook_1(1,3)
        self.make_Canvas_1( self.Tab_1 )               #      Canvas:  at Tab_1(1,3)
        self.make_Frame_1( self.Tab_1 )                #       Frame:  at Tab_1(1,2)
        self.make_Checkbutton_2( self.Frame_1 )        # Checkbutton:  at Frame_1(1,1)
        self.make_Combobox_2( self.Frame_1 )           #    Combobox: Mine Yours Ours : at Frame_1(2,1)
        self.make_Entry_2( self.Frame_1 )              #       Entry:  at Frame_1(3,1)
        self.make_LabelFrame_1( self.Tab_2 )           #  LabelFrame: Left : at Tab_2(1,1)
        self.make_LabelFrame_2( self.Tab_2 )           #  LabelFrame: Right : at Tab_2(1,2)
        self.make_Listbox_1( self.LabelFrame_1 )       #     Listbox:  at LabelFrame_1(1,1)
        self.make_Message_1( self.LabelFrame_1 )       #     Message:  at LabelFrame_1(2,1)
        self.make_Menubutton_1( self.LabelFrame_2 )    #  Menubutton:  at LabelFrame_2(1,1)
        self.make_Notebook_2( self.LabelFrame_2 )      #    Notebook:  at LabelFrame_2(2,1)
        self.make_Tab_4( self.Notebook_2 )             #         Tab:  at Notebook_2(1,1)
        self.make_Tab_5( self.Notebook_2 )             #         Tab:  at Notebook_2(1,2)
        self.make_RadioGroup_1( self.Tab_4 )           #  RadioGroup:  at Tab_4(1,1)
        self.make_Radiobutton_1( self.RadioGroup_1 )   # Radiobutton: 1 : at RadioGroup_1(2,1)
        self.make_Radiobutton_2( self.RadioGroup_1 )   # Radiobutton: 2 : at RadioGroup_1(3,1)
        self.make_Radiobutton_3( self.RadioGroup_1 )   # Radiobutton: 3 : at RadioGroup_1(4,1)
        self.make_Radiobutton_4( self.RadioGroup_1 )   # Radiobutton: 4 : at RadioGroup_1(5,1)
        self.make_Scale_1( self.Tab_5 )                #       Scale:  at Tab_5(2,1)
        self.make_Spinbox_1( self.Tab_5 )              #     Spinbox: 1 to 10 : at Tab_5(3,1)
        self.make_Button_2( self.Tab_3 )               #      Button:  at Tab_3(3,1)
        self.make_Text_1( self.Tab_3 )                 #        Text:  at Tab_3(2,1)
        self.make_Treeview_1( self.Tab_3 )             #    Treeview:  at Tab_3(2,2)

        self.grid_frame.rowconfigure(1, weight=1)
        self.Tab_1.rowconfigure(1, weight=1)
        self.Tab_2.rowconfigure(1, weight=1)
        self.LabelFrame_1.columnconfigure(1, weight=1)
        self.grid_frame.columnconfigure(2, weight=1)
        self.Tab_2.columnconfigure(2, weight=1)
        self.Tab_1.columnconfigure(3, weight=1)
        self.Tab_2.columnconfigure(1, weight=1)

        self.RadioGroup_1_StringVar.set("1")
        self.RadioGroup_1_StringVar_traceName = self.RadioGroup_1_StringVar.trace_variable("w", self.RadioGroup_1_StringVar_Callback)
        # >>>>>>insert any user code below this comment for section "top_of_init"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_1"
    def make_Button_1(self, frame):
        """      Button:  at Main(1,1)"""
        self.Button_1 = Button( frame , text="Button_1", width="15", anchor="e")
        self.Button_1.grid(row=1, column=1, sticky="s")

        # >>>>>>insert any user code below this comment for section "make_Button_1"

        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Notebook_1"
    def make_Notebook_1(self, frame):
        """    Notebook:  at Main(1,2)"""
        self.Notebook_1 = Notebook ( frame , width="400", height="300")
        self.Notebook_1.grid(row=1, column=2, sticky="nsew")

        # >>>>>>insert any user code below this comment for section "make_Notebook_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Tab_1"
    def make_Tab_1(self, frame):
        """         Tab: Small : at Notebook_1(1,1)"""
        self.Tab_1 = Frame( frame )
        self.Notebook_1.add( self.Tab_1, text="Small" )
        # >>>>>>insert any user code below this comment for section "make_Tab_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Tab_2"
    def make_Tab_2(self, frame):
        """         Tab: Medium : at Notebook_1(1,2)"""
        self.Tab_2 = Frame( frame )
        self.Notebook_1.add( self.Tab_2, text="Medium" )
        # >>>>>>insert any user code below this comment for section "make_Tab_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Tab_3"
    def make_Tab_3(self, frame):
        """         Tab: Large : at Notebook_1(1,3)"""
        self.Tab_3 = Frame( frame )
        self.Notebook_1.add( self.Tab_3, text="Large" )
        # >>>>>>insert any user code below this comment for section "make_Tab_3"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Canvas_1"
    def make_Canvas_1(self, frame):
        """      Canvas:  at Tab_1(1,3)"""
        self.Canvas_1 = Canvas( frame , height="50", width="60")
        self.Canvas_1.grid(row=1, column=3, sticky="nsew")

        # >>>>>>insert any user code below this comment for section "make_Canvas_1"

        self.Canvas_1.config(bg='#ffffcc')
        self.Canvas_1.bind("<ButtonRelease-1>", self.Canvas_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Frame_1"
    def make_Frame_1(self, frame):
        """       Frame:  at Tab_1(1,2)"""
        self.Frame_1 = Frame( frame , width="60", height="50")
        self.Frame_1.grid(row=1, column=2, sticky="n")

        # >>>>>>insert any user code below this comment for section "make_Frame_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Checkbutton_2"
    def make_Checkbutton_2(self, frame):
        """ Checkbutton:  at Frame_1(1,1)"""
        self.Checkbutton_2 = Checkbutton( frame , text="Checkbutton_2", width="15", anchor="e")
        self.Checkbutton_2.grid(row=1, column=1)
        self.Checkbutton_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Checkbutton_2"

        self.Checkbutton_2.configure(variable=self.Checkbutton_2_StringVar, onvalue="yes", offvalue="no")
        self.Checkbutton_2_StringVar.set("no")
        self.Checkbutton_2_StringVar_traceName = self.Checkbutton_2_StringVar.trace_variable("w", self.Checkbutton_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Combobox_2"
    def make_Combobox_2(self, frame):
        """    Combobox: Mine Yours Ours : at Frame_1(2,1)"""
        self.Combobox_2 = Combobox( frame , text="Combobox_2", values="Mine Yours Ours")
        self.Combobox_2.grid(row=2, column=1)
        self.Combobox_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Combobox_2"

        self.Combobox_2.configure(textvariable=self.Combobox_2_StringVar)
        self.Combobox_2_StringVar.set( "Mine" )
        self.Combobox_2_StringVar_traceName = self.Combobox_2_StringVar.trace_variable("w", self.Combobox_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Entry_2"
    def make_Entry_2(self, frame):
        """       Entry:  at Frame_1(3,1)"""
        self.Entry_2 = Entry( frame , width="15")
        self.Entry_2.grid(row=3, column=1)
        self.Entry_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Entry_2"

        self.Entry_2.configure(textvariable=self.Entry_2_StringVar)
        self.Entry_2_StringVar_traceName = self.Entry_2_StringVar.trace_variable("w", self.Entry_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_LabelFrame_1"
    def make_LabelFrame_1(self, frame):
        """  LabelFrame: Left : at Tab_2(1,1)"""
        self.LabelFrame_1 = LabelFrame( frame , text="Left", width="60", height="50")
        self.LabelFrame_1.grid(row=1, column=1, sticky="nsew")

        # >>>>>>insert any user code below this comment for section "make_LabelFrame_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_LabelFrame_2"
    def make_LabelFrame_2(self, frame):
        """  LabelFrame: Right : at Tab_2(1,2)"""
        self.LabelFrame_2 = LabelFrame( frame , text="Right", width="60", height="50")
        self.LabelFrame_2.grid(row=1, column=2, sticky="nsew")

        # >>>>>>insert any user code below this comment for section "make_LabelFrame_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Listbox_1"
    def make_Listbox_1(self, frame):
        """     Listbox:  at LabelFrame_1(1,1)"""
        self.Listbox_1 = Listbox( frame , height="12", width="30")
        self.Listbox_1.grid(row=1, column=1)

        # >>>>>>insert any user code below this comment for section "make_Listbox_1"


        # Edit the Listbox Entries
        self.Listbox_1.insert(END, "apples")
        self.Listbox_1.insert(END, "oranges")
        self.Listbox_1.insert(END, "grapes")

        self.Listbox_1.bind("<ButtonRelease-1>", self.Listbox_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Message_1"
    def make_Message_1(self, frame):
        """     Message:  at LabelFrame_1(2,1)"""
        self.Message_1 = Message( frame , text="Message_1", width="55", anchor="e")
        self.Message_1.grid(row=2, column=1, sticky="ew")

        # >>>>>>insert any user code below this comment for section "make_Message_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Menubutton_1"
    def make_Menubutton_1(self, frame):
        """  Menubutton:  at LabelFrame_2(1,1)"""
        self.Menubutton_1 = Menubutton( frame , text="Menubutton_1", width="15", anchor="e")
        self.Menubutton_1.grid(row=1, column=1)
        self.Menubutton_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Menubutton_1"

        self.Menubutton_1.configure(textvariable=self.Menubutton_1_StringVar, text="Select")
        self.Menubutton_1_StringVar.set("Select")
        self.Menubutton_1_StringVar_traceName = self.Menubutton_1_StringVar.trace_variable("w", self.Menubutton_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Notebook_2"
    def make_Notebook_2(self, frame):
        """    Notebook:  at LabelFrame_2(2,1)"""
        self.Notebook_2 = Notebook ( frame , width="400", height="300")
        self.Notebook_2.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Notebook_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Tab_4"
    def make_Tab_4(self, frame):
        """         Tab:  at Notebook_2(1,1)"""
        self.Tab_4 = Frame( frame )
        self.Notebook_2.add( self.Tab_4, text="Tab_4" )
        # >>>>>>insert any user code below this comment for section "make_Tab_4"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Tab_5"
    def make_Tab_5(self, frame):
        """         Tab:  at Notebook_2(1,2)"""
        self.Tab_5 = Frame( frame )
        self.Notebook_2.add( self.Tab_5, text="Tab_5" )
        # >>>>>>insert any user code below this comment for section "make_Tab_5"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_RadioGroup_1"
    def make_RadioGroup_1(self, frame):
        """  RadioGroup:  at Tab_4(1,1)"""
        self.RadioGroup_1 = LabelFrame( frame , width="60", height="50")
        self.RadioGroup_1.grid(row=1, column=1)

        # >>>>>>insert any user code below this comment for section "make_RadioGroup_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_1"
    def make_Radiobutton_1(self, frame):
        """ Radiobutton: 1 : at RadioGroup_1(2,1)"""
        self.Radiobutton_1 = Radiobutton( frame , text="Radiobutton_1", value="1", width="15", anchor="e")
        self.Radiobutton_1.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_1"

        self.Radiobutton_1.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_2"
    def make_Radiobutton_2(self, frame):
        """ Radiobutton: 2 : at RadioGroup_1(3,1)"""
        self.Radiobutton_2 = Radiobutton( frame , text="Radiobutton_2", value="2", width="15")
        self.Radiobutton_2.grid(row=3, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_2"

        self.Radiobutton_2.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_3"
    def make_Radiobutton_3(self, frame):
        """ Radiobutton: 3 : at RadioGroup_1(4,1)"""
        self.Radiobutton_3 = Radiobutton( frame , text="Radiobutton_3", value="3", width="15")
        self.Radiobutton_3.grid(row=4, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_3"

        self.Radiobutton_3.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_4"
    def make_Radiobutton_4(self, frame):
        """ Radiobutton: 4 : at RadioGroup_1(5,1)"""
        self.Radiobutton_4 = Radiobutton( frame , text="Radiobutton_4", value="4", width="15")
        self.Radiobutton_4.grid(row=5, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_4"

        self.Radiobutton_4.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Scale_1"
    def make_Scale_1(self, frame):
        """       Scale:  at Tab_5(2,1)"""
        self.Scale_1 = Scale( frame )
        self.Scale_1.grid(row=2, column=1)
        self.Scale_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Scale_1"

        self.Scale_1.configure(variable=self.Scale_1_StringVar)
        self.Scale_1_StringVar_traceName = self.Scale_1_StringVar.trace_variable("w", self.Scale_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Spinbox_1"
    def make_Spinbox_1(self, frame):
        """     Spinbox: 1 to 10 : at Tab_5(3,1)"""
        self.Spinbox_1 = Spinbox( frame , to="10", text="Spinbox_1", width="15", from_="1")
        self.Spinbox_1.grid(row=3, column=1)
        self.Spinbox_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Spinbox_1"

        self.Spinbox_1.configure(textvariable=self.Spinbox_1_StringVar, to="10", from_="1")
        self.Spinbox_1_StringVar.set("1")
        self.Spinbox_1_StringVar_traceName = self.Spinbox_1_StringVar.trace_variable("w", self.Spinbox_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_2"
    def make_Button_2(self, frame):
        """      Button:  at Tab_3(3,1)"""
        self.Button_2 = Button( frame , text="Button_2", width="15")
        self.Button_2.grid(row=3, column=1)

        # >>>>>>insert any user code below this comment for section "make_Button_2"

        self.Button_2.bind("<ButtonRelease-1>", self.Button_2_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Text_1"
    def make_Text_1(self, frame):
        """        Text:  at Tab_3(2,1)"""

        lbframe = Frame( frame )
        self.Text_1_frame = lbframe
        vbar=Scrollbar(lbframe, orient=VERTICAL)
        self.Text_1 = Text(lbframe, width="40", height="12", yscrollcommand=vbar.set)
        vbar.config(command=self.Text_1.yview)
        
        vbar.grid(row=0, column=1, sticky='ns')        
        self.Text_1.grid(row=0, column=0)

        self.Text_1_frame.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Text_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Treeview_1"
    def make_Treeview_1(self, frame):
        """    Treeview:  at Tab_3(2,2)"""
        self.Treeview_1 = Treeview( frame )
        self.Treeview_1.grid(row=2, column=2)

        # >>>>>>insert any user code below this comment for section "make_Treeview_1"


        self.Treeview_1.insert('', 'end', 'widgets', text='Widget Tour')
        # Same thing, but inserted as first child:
        self.Treeview_1.insert('', 0, 'gallery', text='Treeview_1')
        # Inserted underneath an existing node:
        self.Treeview_1.insert('widgets', 'end', text='Button')
        self.Treeview_1.insert('widgets', 'end', text='Canvas')
        self.Treeview_1.insert('widgets', 'end', text='Checkbutton')
        self.Treeview_1.insert('widgets', 'end', text='Combobox')
        self.Treeview_1.insert('widgets', 'end', text='Entry')
        self.Treeview_1.insert('widgets', 'end', text='Frame')
        self.Treeview_1.insert('widgets', 'end', text='Label')
        self.Treeview_1.insert('widgets', 'end', text='LabelFrame')
        self.Treeview_1.insert('widgets', 'end', text='Listbox')
        self.Treeview_1.insert('widgets', 'end', text='Menubutton')
        self.Treeview_1.insert('widgets', 'end', text='Message')
        self.Treeview_1.insert('widgets', 'end', text='Notebook')
        self.Treeview_1.insert('widgets', 'end', text='OptionMenu')
        self.Treeview_1.insert('widgets', 'end', text='Progressbar')
        self.Treeview_1.insert('widgets', 'end', text='RadioGroup')
        self.Treeview_1.insert('widgets', 'end', text='Radiobutton')
        self.Treeview_1.insert('widgets', 'end', text='Scale')
        self.Treeview_1.insert('widgets', 'end', text='Separator')
        self.Treeview_1.insert('widgets', 'end', text='Spinbox')
        self.Treeview_1.insert('widgets', 'end', text='Tab')
        self.Treeview_1.insert('widgets', 'end', text='Text')
        self.Treeview_1.insert('widgets', 'end', text='Treeview')

        # Treeview chooses the id:
        id = self.Treeview_1.insert('', 'end', text='Tutorial')
        self.Treeview_1.insert(id, 'end', text='Tree')

        self.Treeview_1.bind("<ButtonRelease-1>", self.Treeview_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_1_Click"
    def Button_1_Click(self, event): #bind method for component ID=Button_1
        """      Button:  at Main(1,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_1_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_1_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Canvas_1_Click"
    def Canvas_1_Click(self, event): #bind method for component ID=Canvas_1
        """      Canvas:  at Tab_1(1,3)"""
        pass
        # >>>>>>insert any user code below this comment for section "Canvas_1_Click"
        # replace, delete, or comment-out the following
        print( "executed method Canvas_1_Click" )

        print( "clicked in canvas at x,y =",event.x,event.y )
        w = int(self.Canvas_1.cget("width"))
        h = int(self.Canvas_1.cget("height"))
        self.Canvas_1.create_rectangle((2, 2, w+1, h+1), outline="blue")
        self.Canvas_1.create_line(0, 0, w+2, h+2, fill="red")
        x = int(event.x)
        y = int(event.y)
        print( "event x,y=",x,y )
        self.Canvas_1.create_text(x,y, text="NE", fill="green", anchor=NE)
        self.Canvas_1.create_text(x,y, text="SW", fill="magenta", anchor=SW)
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Listbox_1_Click"
    def Listbox_1_Click(self, event): #bind method for component ID=Listbox_1
        """     Listbox:  at LabelFrame_1(1,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Listbox_1_Click"
        # replace, delete, or comment-out the following
        print( "executed method Listbox_1_Click" )

        print( "current selection(s) =",self.Listbox_1.curselection() )
        labelL = []
        for i in self.Listbox_1.curselection():
            labelL.append( self.Listbox_1.get(i))
        print( "current label(s) =",labelL )
        # use self.Listbox_1.insert(0, "item zero")
        #     self.Listbox_1.insert(index, "item i")
        #            OR
        #     self.Listbox_1.insert(END, "item end")
        #   to insert items into the list box
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_2_Click"
    def Button_2_Click(self, event): #bind method for component ID=Button_2
        """      Button:  at Tab_3(3,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_2_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_2_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Treeview_1_Click"
    def Treeview_1_Click(self, event): #bind method for component ID=Treeview_1
        """    Treeview:  at Tab_3(2,2)"""
        pass
        # >>>>>>insert any user code below this comment for section "Treeview_1_Click"
        # replace, delete, or comment-out the following
        print( "executed method Treeview_1_Click" )

        curItem = self.Treeview_1.focus()
        print( "current Treeview item(s) =",self.Treeview_1.item( curItem ) )
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Checkbutton_2_StringVar_traceName"
    def Checkbutton_2_StringVar_Callback(self, varName, index, mode):
        """ Checkbutton:  at Frame_1(1,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Checkbutton_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Checkbutton_2_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Checkbutton_2_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Combobox_2_StringVar_traceName"
    def Combobox_2_StringVar_Callback(self, varName, index, mode):
        """    Combobox: Mine Yours Ours : at Frame_1(2,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Combobox_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Combobox_2_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Combobox_2_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Entry_2_StringVar_traceName"
    def Entry_2_StringVar_Callback(self, varName, index, mode):
        """       Entry:  at Frame_1(3,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Entry_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Entry_2_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Entry_2_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Menubutton_1_StringVar_traceName"
    def Menubutton_1_StringVar_Callback(self, varName, index, mode):
        """  Menubutton:  at LabelFrame_2(1,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Menubutton_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Menubutton_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Menubutton_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Scale_1_StringVar_traceName"
    def Scale_1_StringVar_Callback(self, varName, index, mode):
        """       Scale:  at Tab_5(2,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Scale_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Scale_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Scale_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Spinbox_1_StringVar_traceName"
    def Spinbox_1_StringVar_Callback(self, varName, index, mode):
        """     Spinbox: 1 to 10 : at Tab_5(3,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Spinbox_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Spinbox_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Spinbox_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "RadioGroup_1_StringVar_traceName"
    def RadioGroup_1_StringVar_Callback(self, varName, index, mode):
        """  RadioGroup:  at Tab_4(1,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "RadioGroup_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "RadioGroup_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.RadioGroup_1_StringVar.get() )



# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"

def main():
    root = Tk()
    app = _full_combo(root)
    root.mainloop()

if __name__ == '__main__':
    main()
