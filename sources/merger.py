"""
Facilitates merging multiple CSV files into a consolidated CSV
"""
# useful methods to measure time performance by small pieces of code
from codetiming import Timer
# Custom classes specific to this package
from common.FileOperations import FileOperations
from common.BasicNeeds import os, BasicNeeds
from common.CommandLineArgumentsManagement import CommandLineArgumentsManagement
from common.LoggingNeeds import LoggingNeeds
from common.DataManipulator import DataManipulator
from data_management.BasicNeedsForMerger import BasicNeedsForMerger
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
    # instantiate Command Line Arguments class
    c_clam = CommandLineArgumentsManagement()
    parameters_in = c_clam.parse_arguments(configuration_details['input_options']['merger'])
    input_options = configuration_details['input_options'][CURRENT_SCRIPT_NAME]
    # instantiate Basic Needs class
    c_bn = BasicNeeds()
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bn.fn_check_inputs(parameters_in)
    # instantiate Extractor Specific Needs class
    c_bnfm = BasicNeedsForMerger()
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bnfm.fn_check_inputs_specific(parameters_in)
    # instantiate Logger class
    c_ln = LoggingNeeds()
    # initiate logger
    c_ln.initiate_logger(parameters_in.output_log_file, 'dm_' + CURRENT_SCRIPT_NAME)
    # define global timer to use
    t = Timer('dm_' + CURRENT_SCRIPT_NAME, text='Time spent is {seconds}', logger=c_ln.logger.debug)
    # reflect title and input parameters given values in the log
    c_clam.listing_parameter_values(c_ln.logger, t, 'Data Merger', input_options, parameters_in)
    # instantiate Data Manipulator class
    c_dm = DataManipulator()
    # loading from a specific folder all files matching a given pattern into a file list
    relevant_files_list = c_fo.build_file_list(c_ln.logger, t, parameters_in.input_file)
    # exposing statistic for each file identified
    c_fo.fn_store_file_statistics(c_ln.logger, t, relevant_files_list, 'Input')
    # loading from a specific folder all files matching a given pattern into a data frame
    working_data_frame = c_dm.fn_load_file_list_to_data_frame(c_ln.logger, t,
                                                              relevant_files_list,
                                                              parameters_in.csv_field_separator)
    # store data frame into single CSV file
    c_dm.fn_store_data_frame_to_file(c_ln.logger, t, working_data_frame, {
        'field_delimiter': parameters_in.csv_field_separator,
        'format': 'csv',
        'name': parameters_in.output_file,
    })
    # store statistics about output file
    c_fo.fn_store_file_statistics(c_ln.logger, t, parameters_in.output_file, 'Generated')
    # just final message
    c_bn.fn_final_message(c_ln.logger, parameters_in.output_log_file, t.timers.total('dm_merger'))
