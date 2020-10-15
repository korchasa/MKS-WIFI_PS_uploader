#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Oct 13, 2020 12:38:19 AM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import mks_ass_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    mks_ass_gui_support.set_Tk_var()
    top = Main (root)
    mks_ass_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Main(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    mks_ass_gui_support.set_Tk_var()
    top = Main (w)
    mks_ass_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("640x360+683+373")
        top.minsize(640, 320)
        top.maxsize(2948, 1181)
        top.resizable(0, 0)
        top.title("MKS ASS")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.btn_Connect = ttk.Button(top)
        self.btn_Connect.place(relx=0.369, rely=0.022, height=25, width=70)
        self.btn_Connect.configure(takefocus="")
        self.btn_Connect.configure(text='''Connect''')

        self.prg_UploadStatus = ttk.Progressbar(top)
        self.prg_UploadStatus.place(relx=0.141, rely=0.344, relwidth=0.603
                , relheight=0.0, height=26)
        self.prg_UploadStatus.configure(length="390")
        self.prg_UploadStatus.configure(value="0")
        self.prg_UploadStatus.configure(cursor="fleur")

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.chk_PrintUploaded = ttk.Checkbutton(top)
        self.chk_PrintUploaded.place(relx=0.766, rely=0.25, relwidth=0.219
                , relheight=0.0, height=23)
        self.chk_PrintUploaded.configure(variable=mks_ass_gui_support.tch52)
        self.chk_PrintUploaded.configure(takefocus="")
        self.chk_PrintUploaded.configure(text='''Print after uploading''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.117, relwidth=0.998)

        self.ent_IP = ttk.Entry(top)
        self.ent_IP.place(relx=0.169, rely=0.025, relheight=0.064
                , relwidth=0.192)
        self.ent_IP.configure(font="-family {Segoe UI} -size 9 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ent_IP.configure(takefocus="")
        self.ent_IP.configure(cursor="ibeam")
        self.tooltip_font = "TkDefaultFont"
        self.ent_IP_tooltip = \
        ToolTip(self.ent_IP, self.tooltip_font, '''Printer IP Address''')

        self.lbl_IP = ttk.Label(top)
        self.lbl_IP.place(relx=0.014, rely=0.028, height=21, width=99)
        self.lbl_IP.configure(background="#d9d9d9")
        self.lbl_IP.configure(foreground="#000000")
        self.lbl_IP.configure(font="TkDefaultFont")
        self.lbl_IP.configure(relief="flat")
        self.lbl_IP.configure(anchor='w')
        self.lbl_IP.configure(justify='left')
        self.lbl_IP.configure(text='''Printer IP Address''')

        self.lbl_Con = ttk.Label(top)
        self.lbl_Con.place(relx=0.522, rely=0.028, height=21, width=99)
        self.lbl_Con.configure(background="#d9d9d9")
        self.lbl_Con.configure(foreground="#000000")
        self.lbl_Con.configure(font="TkDefaultFont")
        self.lbl_Con.configure(relief="flat")
        self.lbl_Con.configure(anchor='w')
        self.lbl_Con.configure(justify='left')
        self.lbl_Con.configure(text='''Connection State''')

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.506, rely=0.0, relheight=0.117)
        self.TSeparator2.configure(orient="vertical")

        self.lbl_Connection_state = ttk.Label(top)
        self.lbl_Connection_state.place(relx=0.716, rely=0.017, height=31
                , width=160)
        self.lbl_Connection_state.configure(background="#d9d9d9")
        self.lbl_Connection_state.configure(foreground="#ff0000")
        self.lbl_Connection_state.configure(font="-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.lbl_Connection_state.configure(relief="flat")
        self.lbl_Connection_state.configure(anchor='w')
        self.lbl_Connection_state.configure(justify='center')
        self.lbl_Connection_state.configure(text='''NOT CONNECTED''')

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.ent_LocalFile = ttk.Entry(top)
        self.ent_LocalFile.place(relx=0.125, rely=0.156, relheight=0.056
                , relwidth=0.713)
        self.ent_LocalFile.configure(takefocus="")
        self.ent_LocalFile.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.016, rely=0.156, height=21, width=55)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Local File''')

        self.btn_FileSel = ttk.Button(top)
        self.btn_FileSel.place(relx=0.859, rely=0.147, height=25, width=76)
        self.btn_FileSel.configure(takefocus="")
        self.btn_FileSel.configure(text='''Select File''')

        self.ent_NewName = ttk.Entry(top)
        self.ent_NewName.place(relx=0.125, rely=0.25, relheight=0.056
                , relwidth=0.619)
        self.ent_NewName.configure(takefocus="")
        self.ent_NewName.configure(cursor="ibeam")

        self.lbl_NewName = ttk.Label(top)
        self.lbl_NewName.place(relx=0.016, rely=0.25, height=21, width=66)
        self.lbl_NewName.configure(background="#d9d9d9")
        self.lbl_NewName.configure(foreground="#000000")
        self.lbl_NewName.configure(font="TkDefaultFont")
        self.lbl_NewName.configure(relief="flat")
        self.lbl_NewName.configure(anchor='w')
        self.lbl_NewName.configure(justify='left')
        self.lbl_NewName.configure(text='''New Name''')
        self.lbl_NewName.configure(cursor="fleur")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btn_Upload = ttk.Button(top)
        self.btn_Upload.place(relx=0.016, rely=0.344, height=25, width=76)
        self.btn_Upload.configure(takefocus="")
        self.btn_Upload.configure(text='''UPLOAD''')

        self.lbl_UploadStatus = ttk.Label(top)
        self.lbl_UploadStatus.place(relx=0.766, rely=0.353, height=23, width=135)

        self.lbl_UploadStatus.configure(background="#d9d9d9")
        self.lbl_UploadStatus.configure(foreground="#000000")
        self.lbl_UploadStatus.configure(font="TkDefaultFont")
        self.lbl_UploadStatus.configure(relief="flat")
        self.lbl_UploadStatus.configure(anchor='w')
        self.lbl_UploadStatus.configure(justify='left')
        self.lbl_UploadStatus.configure(text='''Upload Status''')

# ======================================================
# Support code for Balloon Help (also called tooltips).
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()




