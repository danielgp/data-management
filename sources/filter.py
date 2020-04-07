"""
Facilitates filtering CSV files based on a carefully constructed JSON expression
"""
import ast
# package to facilitate operating system operations
import os
# useful methods to measure time performance by small pieces of code
from codetiming import Timer
# Custom classes specific to this package
from sources.data_management.BasicNeeds import BasicNeeds
from sources.data_management.CommandLineArgumentsManagement import CommandLineArgumentsManagement
from sources.data_management.LoggingNeeds import LoggingNeeds
from sources.data_management.DataManipulator import DataManipulator

# get current script name
current_script_name = os.path.basename(__file__).replace('.py', '')

# main execution logic
if __name__ == '__main__':
    # instantiate Basic Needs class
    c_bn = BasicNeeds()
    # load application configuration (inputs are defined into a json file)
    c_bn.fn_load_configuration()
    # instantiate Command Line Arguments class
    c_clam = CommandLineArgumentsManagement()
    parameters_in = c_clam.parse_arguments(c_bn.cfg_dtls['input_options']['filter'])
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bn.fn_check_inputs(parameters_in, current_script_name)
    # instantiate Logger class
    c_ln = LoggingNeeds()
    # initiate logger
    c_ln.initiate_logger(parameters_in.output_log_file, 'dm_filter')
    # define global timer to use
    t = Timer('dm_filter', text='Time spent is {seconds} ', logger=c_ln.logger.debug)
    # reflect title and input parameters given values in the log
    c_clam.listing_parameter_values(c_ln.logger, t, 'Filter',
                                    c_bn.cfg_dtls['input_options']['filter'], parameters_in)
    # instantiate Basic Needs class
    c_dm = DataManipulator()
    # build a list of file based on provided file pattern applied to given input directory
    relevant_files = c_dm.fn_build_relevant_file_list(c_ln.logger, t,
                                                      parameters_in.input_directory,
                                                      parameters_in.input_file_pattern)
    # load all relevant files into a single data frame
    relevant_data_frame = c_dm.fn_load_file_list_to_data_frame(c_ln.logger, t, relevant_files,
                                                               parameters_in.csv_field_separator)
    # build relevant filter dictionary based on an input JSON expression
    relevant_filters = ast.literal_eval(parameters_in.filter_expression)
    # perform the filter logic
    resulted_data_frame = c_dm.fn_apply_query_to_data_frame(c_ln.logger, t, relevant_data_frame, {
        'column_to_filter': relevant_filters['column_to_filter'],
        'filter_to_apply': relevant_filters['filter_to_apply'],
        'filter_values': relevant_filters['filter_values'],
    })
    # storing resulted data frame into a local file
    c_dm.fn_store_data_frame_to_file(c_ln.logger, t, resulted_data_frame,
                                     parameters_in.output_directory
                                     + parameters_in.output_relative_file,
                                     parameters_in.csv_field_separator)
    # store statistics about output file
    c_bn.fn_store_file_statistics(c_ln.logger, t, parameters_in.output_log_file, 'Generated')
    # just final message
    c_bn.fn_final_message(c_ln.logger, parameters_in.output_log_file, t.timers.total('dm_filter'))
