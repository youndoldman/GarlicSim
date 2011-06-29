# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the `NameParser` class.

See its documentation for more information.
'''

from garlicsim.general_misc import sequence_tools
from garlicsim.general_misc import string_tools

class CaseStyleType(type):
    pass

class BaseCaseStyle(object):
    __metaclass__ = CaseStyleType
    
class LowerCase(BaseCaseStyle):
    pass

class CamelCase(BaseCaseStyle):
    pass


class NameParser(object):
    def __init__(self, case_style_possibilites=(LowerCase,),
                 n_preceding_underscores_possibilites=(1,)):
        
        self.case_style_possibilites = sequence_tools.to_tuple(
            case_style_possibilites,
            member_type=CaseStyleType
        )
        
        self.n_preceding_underscores_possibilites = sequence_tools.to_tuple(
            n_preceding_underscores_possibilites
        )
        
        
        assert all(isinstance(case_style, CaseStyleType) for case_style in 
                   self.case_style_possibilites)       
        assert all(isinstance(n_preceding_underscores, int) for
                   n_preceding_underscores in
                   self.n_preceding_underscores_possibilites)
        
                
    def match(self, name):
        n_preceding_underscores = string_tools.get_n_identical_edge_characters(
            name,
            character='_',
            head=True
        )
        if n_preceding_underscores not in \
           self.n_preceding_underscores_possibilites:
            return False
        cleaned_name = name[n_preceding_underscores:] # blocktodo: What about the 'on' part?
        for case_style in self.case_style_possibilites:
            try:
                case_style.match(cleaned_name) 
    