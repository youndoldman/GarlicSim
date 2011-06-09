# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the `` class.

See its documentation for more information.
'''

import wx

from garlicsim.general_misc import caching

from .event_codes import get_event_code_of_component, get_event_code_from_name


class EventHandlerGrokker(object):
    def __init__(self, name, event_handler):
        assert name.startswith('_on_')
        self.name = name
        self.event_handler = event_handler # blocktodo: should we even save this?
        
    cleaned_name = caching.CachedProperty(
        lambda self: self.name[4:],
        doc=''' '''
    )
        
    def bind(self, window):
        assert isinstance(window, wx.Window)
        if hasattr(window, self.cleaned_name):
            component = getattr(window, self.cleaned_name)
            return window.Bind(
                get_event_code_of_component(component),
                getattr(window, self.name), #self.event_handler,
                source=component
            )
        else:
            return window.Bind(
                get_event_code_from_name(self.cleaned_name),
                getattr(window, self.name) #self.event_handler,
            )
                
            
        
        
        