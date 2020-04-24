"""
Facilitates moving files from a specified directory and matching pattern to a destination directory
"""
# useful methods to measure time performance by small pieces of code
from codetiming import Timer
# Custom classes specific to this package
from common.FileOperations import FileOperations
from common.BasicNeeds import os, BasicNeeds
from common.CommandLineArgumentsManagement import CommandLineArgumentsManagement
from common.LoggingNeeds import LoggingNeeds
from common.DataManipulator import DataManipulator
from data_management.BasicNeedsForMover import BasicNeedsForMover
# get current script name
CURRENT_SCRIPT_NAME = os.path.basename(__file__).replace('.py', '')

# main execution logic
if __name__ == '__main__':
    # instantiate File Operations class
    c_fo = FileOperations()
    # load application configuration (inputs are defined into a json file)
    crt_folder = os.path.dirname(__file__)
    configuration_file = os.path.join(crt_folder, 'config/data-management.json').replace('\\', '/')
    configuration_details = c_fo.fn_open_file_and_get_content(configuration_file)
    input_options = configuration_details['input_options'][CURRENT_SCRIPT_NAME]
    # instantiate Basic Needs class
    c_bn = BasicNeeds()
    # instantiate Command Line Arguments class
    c_clam = CommandLineArgumentsManagement()
    parameters_in = c_clam.parse_arguments(input_options)
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bn.fn_check_inputs(parameters_in)
    # instantiate Extractor Specific Needs class
    c_bnfm = BasicNeedsForMover()
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bnfm.fn_check_inputs_specific(parameters_in)
    # instantiate Logger class
    c_ln = LoggingNeeds()
    # initiate logger
    c_ln.initiate_logger(parameters_in.output_log_file, 'dm_' + CURRENT_SCRIPT_NAME)
    # define global timer to use
    t = Timer('dm_' + CURRENT_SCRIPT_NAME, text='Time spent is {seconds} ',
              logger=c_ln.logger.debug)
    # reflect title and input parameters given values in the log
    c_clam.listing_parameter_values(c_ln.logger, t, 'Data Rename or Move', input_options,
                                    parameters_in)
    # instantiate Basic Needs class
    c_dm = DataManipulator()
    # build list of file based on pattern provided
    csv_file_names = c_fo.build_file_list(c_ln.logger, t, parameters_in.input_file)
    if len(csv_file_names) == 0:
        c_ln.logger.warning('No files were found with given criteria')
    else:
        # exposing statistic for each file identified
        c_fo.fn_store_file_statistics(c_ln.logger, t, csv_file_names, 'Input')
        # making the actual rename or move
        new_files = c_fo.fn_move_files(c_ln.logger, t, csv_file_names,
                                       parameters_in.output_directory)
        # exposing statistic for each file identified
        c_fo.fn_store_file_statistics(c_ln.logger, t, new_files, 'Output')
    # just final message
    c_bn.fn_final_message(c_ln.logger, parameters_in.output_log_file,
                          t.timers.total('dm_' + CURRENT_SCRIPT_NAME))
