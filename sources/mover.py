# package to facilitate operating system operations
import os
# useful methods to measure time performance by small pieces of code
from codetiming import Timer
# Custom classes specific to this package
from data_management.BasicNeeds import BasicNeeds
from data_management.CommandLineArgumentsManagement import CommandLineArgumentsManagement
from data_management.LoggingNeeds import LoggingNeeds
from data_management.DataManipulator import DataManipulator

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
    parameters_in = c_clam.parse_arguments(c_bn.cfg_dtls['input_options']['mover'])
    # checking inputs, if anything is invalid an exit(1) will take place
    c_bn.fn_check_inputs(parameters_in, current_script_name)
    # instantiate Logger class
    c_ln = LoggingNeeds()
    # initiate logger
    c_ln.initiate_logger(parameters_in.output_log_file, 'dm_mover')
    # define global timer to use
    t = Timer('dm_mover', text='Time spent is {seconds} ', logger=c_ln.logger.debug)
    # reflect title and input parameters given values in the log
    c_clam.listing_parameter_values(c_ln.logger, t, 'Data Rename or Move',
                                    c_bn.cfg_dtls['input_options']['mover'], parameters_in)
    # instantiate Basic Needs class
    c_dm = DataManipulator()
    # making the actual rename or move
    c_dm.fn_rename_or_move_files(c_ln.logger, t, parameters_in.input_directory,
                                 parameters_in.input_file_pattern, parameters_in.output_directory)
    # store statistics about output file
    c_bn.fn_store_file_statistics(c_ln.logger, t, parameters_in.output_log_file, 'Generated')
    # just final message
    c_bn.fn_final_message(c_ln.logger, parameters_in.output_log_file, t.timers.total('dm_mover'))
