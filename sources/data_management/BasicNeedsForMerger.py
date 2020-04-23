"""
Class Merger Specific Needs

Handling specific needs for Merger script
"""
# package to facilitate common operations
from common.BasicNeeds import os, BasicNeeds


class BasicNeedsForMerger():
    lcl_bn = None

    def __init__(self):
        self.lcl_bn = BasicNeeds()

    def fn_check_inputs_specific(self, input_parameters):
            self.lcl_bn.fn_validate_single_value(os.path.dirname(input_parameters.output_file),
                                                 'folder', 'output file')
