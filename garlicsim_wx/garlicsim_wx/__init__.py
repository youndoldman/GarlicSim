# Copyright 2009-2010 Ram Rachum. No part of this program may be used, copied
# or distributed without explicit written permission from Ram Rachum.

'''
garlicsim_wx, a wxPython GUI for garlicsim.

The final goal of this project is to become a fully-fledged application for
working with simulations, friendly enough that it may be used by
non-programmers.

This program is intended for Python versions 2.5 and 2.6.
'''

import bootstrap

import wx

import misc

from frame import Frame
from gui_project import GuiProject

__all__ = ['Frame', 'GuiProject', 'start', 'editing_interface']

__version__ = '0.3'

def start():
    '''Start the gui.'''
    app = wx.PySimpleApp()
    my_app_win = Frame(None, -1, "GarlicSim", size=(600, 600))
    app.SetTopWindow(my_app_win)

    """
    import cProfile
    cProfile.run("app.MainLoop()")
    """
    app.MainLoop()
    
if __name__ == "__main__":
    start()