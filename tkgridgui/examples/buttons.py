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
class _buttons:
    def __init__(self, master):
    
        grid_frame = Frame( master )
        self.grid_frame = grid_frame
        grid_frame.pack(expand=1, fill=BOTH)
        self.master = master
        
        self.x, self.y, self.w, self.h = 10, 10, 805, 208

        self.master.title("buttons")

        self.make_Button_10( self.grid_frame )         #      Button:  at Main(7,1)
        self.make_Button_11( self.grid_frame )         #      Button:  at Main(0,6)
        self.make_Button_3( self.grid_frame )          #      Button:  at Main(1,6)
        self.make_Button_4( self.grid_frame )          #      Button:  at Main(1,5)
        self.make_Button_5( self.grid_frame )          #      Button:  at Main(2,4)
        self.make_Button_6( self.grid_frame )          #      Button:  at Main(3,3)
        self.make_Button_7( self.grid_frame )          #      Button:  at Main(4,2)
        self.make_Button_8( self.grid_frame )          #      Button:  at Main(5,1)
        self.make_Button_9( self.grid_frame )          #      Button:  at Main(6,0)


        # >>>>>>insert any user code below this comment for section "top_of_init"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_10"
    def make_Button_10(self, frame):
        """      Button:  at Main(7,1)"""
        self.Button_10 = Button( frame , text="Button_10", width="15")
        self.Button_10.grid(row=7, column=1)

        # >>>>>>insert any user code below this comment for section "make_Button_10"

        self.Button_10.bind("<ButtonRelease-1>", self.Button_10_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_11"
    def make_Button_11(self, frame):
        """      Button:  at Main(0,6)"""
        self.Button_11 = Button( frame , text="Button_11", width="15")
        self.Button_11.grid(row=0, column=6)

        # >>>>>>insert any user code below this comment for section "make_Button_11"

        self.Button_11.bind("<ButtonRelease-1>", self.Button_11_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_3"
    def make_Button_3(self, frame):
        """      Button:  at Main(1,6)"""
        self.Button_3 = Button( frame , text="Button_3", width="15")
        self.Button_3.grid(row=1, column=6)

        # >>>>>>insert any user code below this comment for section "make_Button_3"

        self.Button_3.bind("<ButtonRelease-1>", self.Button_3_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_4"
    def make_Button_4(self, frame):
        """      Button:  at Main(1,5)"""
        self.Button_4 = Button( frame , text="Button_4", width="15")
        self.Button_4.grid(row=1, column=5)

        # >>>>>>insert any user code below this comment for section "make_Button_4"

        self.Button_4.bind("<ButtonRelease-1>", self.Button_4_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_5"
    def make_Button_5(self, frame):
        """      Button:  at Main(2,4)"""
        self.Button_5 = Button( frame , text="Button_5", width="15")
        self.Button_5.grid(row=2, column=4)

        # >>>>>>insert any user code below this comment for section "make_Button_5"

        self.Button_5.bind("<ButtonRelease-1>", self.Button_5_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_6"
    def make_Button_6(self, frame):
        """      Button:  at Main(3,3)"""
        self.Button_6 = Button( frame , text="Button_6", width="15")
        self.Button_6.grid(row=3, column=3)

        # >>>>>>insert any user code below this comment for section "make_Button_6"

        self.Button_6.bind("<ButtonRelease-1>", self.Button_6_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_7"
    def make_Button_7(self, frame):
        """      Button:  at Main(4,2)"""
        self.Button_7 = Button( frame , text="Button_7", width="15")
        self.Button_7.grid(row=4, column=2)

        # >>>>>>insert any user code below this comment for section "make_Button_7"

        self.Button_7.bind("<ButtonRelease-1>", self.Button_7_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_8"
    def make_Button_8(self, frame):
        """      Button:  at Main(5,1)"""
        self.Button_8 = Button( frame , text="Button_8", width="15")
        self.Button_8.grid(row=5, column=1)

        # >>>>>>insert any user code below this comment for section "make_Button_8"

        self.Button_8.bind("<ButtonRelease-1>", self.Button_8_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Button_9"
    def make_Button_9(self, frame):
        """      Button:  at Main(6,0)"""
        self.Button_9 = Button( frame , text="Button_9", width="15")
        self.Button_9.grid(row=6, column=0)

        # >>>>>>insert any user code below this comment for section "make_Button_9"

        self.Button_9.bind("<ButtonRelease-1>", self.Button_9_Click)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_10_Click"
    def Button_10_Click(self, event): #bind method for component ID=Button_10
        """      Button:  at Main(7,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_10_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_10_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_11_Click"
    def Button_11_Click(self, event): #bind method for component ID=Button_11
        """      Button:  at Main(0,6)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_11_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_11_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_3_Click"
    def Button_3_Click(self, event): #bind method for component ID=Button_3
        """      Button:  at Main(1,6)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_3_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_3_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_4_Click"
    def Button_4_Click(self, event): #bind method for component ID=Button_4
        """      Button:  at Main(1,5)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_4_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_4_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_5_Click"
    def Button_5_Click(self, event): #bind method for component ID=Button_5
        """      Button:  at Main(2,4)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_5_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_5_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_6_Click"
    def Button_6_Click(self, event): #bind method for component ID=Button_6
        """      Button:  at Main(3,3)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_6_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_6_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_7_Click"
    def Button_7_Click(self, event): #bind method for component ID=Button_7
        """      Button:  at Main(4,2)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_7_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_7_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_8_Click"
    def Button_8_Click(self, event): #bind method for component ID=Button_8
        """      Button:  at Main(5,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_8_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_8_Click" )

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Button_9_Click"
    def Button_9_Click(self, event): #bind method for component ID=Button_9
        """      Button:  at Main(6,0)"""
        pass
        # >>>>>>insert any user code below this comment for section "Button_9_Click"
        # replace, delete, or comment-out the following
        print( "executed method Button_9_Click" )

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"

def main():
    root = Tk()
    app = _buttons(root)
    root.mainloop()

if __name__ == '__main__':
    main()
