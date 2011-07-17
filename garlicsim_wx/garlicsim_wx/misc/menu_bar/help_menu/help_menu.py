# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
Defines the `HelpMenu` class.

See its documentation for more info.
'''

import wx

from garlicsim_wx.general_misc.cute_menu import CuteMenu

import garlicsim_wx

from .online_resources_menu import OnlineResourcesMenu


class HelpMenu(CuteMenu):
    '''Menu for getting help on GarlicSim.'''
    def __init__(self, frame):
        super(HelpMenu, self).__init__()
        self.frame = frame
        self._build()
    
    def _build(self):
        
        frame = self.frame                
        
        
        self.garlicsim_help_button = self.Append(
            wx.ID_HELP_CONTENTS,
            'GarlicSim &Help...\tF1',
            ' Display the help documents for GarlicSim'
        )
        self.garlicsim_help_button.Enable(False)
        
        
        self.welcome_screen_button = self.Append(
            -1,
            '&Welcome screen',
            ' Show the welcome screen'
        )
        self.welcome_screen_button.Enable(False)
        
        
        self.AppendSeparator()
                
 
        self.online_resources_menu = OnlineResourcesMenu(frame)
        self.online_resources_menu_button = self.AppendMenu(
            -1,
            '&Online resources',
            self.online_resources_menu,
            ' Use resources that require an internet connection'
        )       
        
        
        self.AppendSeparator()
        
                
        self.about_button = self.Append(
            wx.ID_ABOUT,
            '&About GarlicSim',
            ' Tell me a little bit about the GarlicSim software'
        )
        frame.Bind(
            wx.EVT_MENU,
            lambda event: garlicsim_wx.widgets.misc.AboutDialog.\
                          create_and_show_modal(frame),
            self.about_button
        )
 