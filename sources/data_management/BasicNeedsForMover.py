"""
Class Mover Specific Needs

Handling specific needs for Mover script
"""
# package to facilitate common operations
from data_management.BasicNeeds import os, BasicNeeds


class BasicNeedsForMover:
    lcl_bn = None

    def __init__(self):
        self.lcl_bn = BasicNeeds()

    def fn_check_inputs_specific(self, input_parameters):
            self.lcl_bn.fn_validate_single_value(os.path.dirname(input_parameters.output_directory),
                                                 'folder', 'output directory')
