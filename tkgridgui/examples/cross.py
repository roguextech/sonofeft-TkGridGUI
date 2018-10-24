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
class _cross:
    def __init__(self, master):
    
        grid_frame = Frame( master )
        self.grid_frame = grid_frame
        grid_frame.pack(expand=1, fill=BOTH)
        self.master = master
        
        self.x, self.y, self.w, self.h = 10, 10, 345, 78

        self.master.title("cross")

        self.make_Button_1( self.grid_frame )          #      Button:  at Main(2,1)
        self.make_Button_2( self.grid_frame )          #      Button:  at Main(3,2)
        self.make_Button_3( self.grid_frame )          #      Button:  at Main(4,3)
        self.make_Entry_1( self.grid_frame )           #       Entry:  at Main(2,3)
        self.make_Entry_2( self.grid_frame )           #       Entry:  at Main(4,1)


        # >>>>>>insert any user code below this comment for section "top_of_init"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_1"
    def make_Button_1(self, frame):
        """      Button:  at Main(2,1)"""
        self.Button_1 = Button( frame , text="Button_1", width="15")
        self.Button_1.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Button_1"

        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_2"
    def make_Button_2(self, frame):
        """      Button:  at Main(3,2)"""
        self.Button_2 = Button( frame , text="Button_2", width="15")
        self.Button_2.grid(row=3, column=2)

        # >>>>>>insert any user code below this comment for section "make_Button_2"

        self.Button_2.bind("<ButtonRelease-1>", self.Button_2_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_3"
    def make_Button_3(self, frame):
        """      Button:  at Main(4,3)"""
        self.Button_3 = Button( frame , text="Button_3", width="15")
        self.Button_3.grid(row=4, column=3)

        # >>>>>>insert any user code below this comment for section "make_Button_3"

        self.Button_3.bind("<ButtonRelease-1>", self.Button_3_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Entry_1"
    def make_Entry_1(self, frame):
        """       Entry:  at Main(2,3)"""
        self.Entry_1 = Entry( frame , width="15")
        self.Entry_1.grid(row=2, column=3)
        self.Entry_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Entry_1"

        self.Entry_1.configure(textvariable=self.Entry_1_StringVar)
        self.Entry_1_StringVar_traceName = self.Entry_1_StringVar.trace_variable("w", self.Entry_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Entry_2"
    def make_Entry_2(self, frame):
        """       Entry:  at Main(4,1)"""
        self.Entry_2 = Entry( frame , width="15")
        self.Entry_2.grid(row=4, column=1)
        self.Entry_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Entry_2"

        self.Entry_2.configure(textvariable=self.Entry_2_StringVar)
        self.Entry_2_StringVar_traceName = self.Entry_2_StringVar.trace_variable("w", self.Entry_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_1_Click"
    def Button_1_Click(self, event): #bind method for component ID=Button_1
        """      Button:  at Main(2,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_1_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_1_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_2_Click"
    def Button_2_Click(self, event): #bind method for component ID=Button_2
        """      Button:  at Main(3,2)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_2_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_2_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_3_Click"
    def Button_3_Click(self, event): #bind method for component ID=Button_3
        """      Button:  at Main(4,3)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_3_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_3_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Entry_1_StringVar_traceName"
    def Entry_1_StringVar_Callback(self, varName, index, mode):
        """       Entry:  at Main(2,3)"""
        pass

        # >>>>>>insert any user code below this comment for section "Entry_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Entry_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Entry_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Entry_2_StringVar_traceName"
    def Entry_2_StringVar_Callback(self, varName, index, mode):
        """       Entry:  at Main(4,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Entry_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Entry_2_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Entry_2_StringVar.get() )



# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"

def main():
    root = Tk()
    app = _cross(root)
    root.mainloop()

if __name__ == '__main__':
    main()
