# Data Management package


## What is this repository for?

Facilitate data management (aka manipulation).

## Who do I talk to?

Repository owner is: [Daniel Popiniuc](mailto:danielpopiniuc@gmail.com)


## Installation

Installation can be completed in few steps as follows:
* Ensure you have git available to your system:
```
    $ git --version
```
> If you get an error depending on your system you need to install it.
>> For Windows you can do so from [Git for Windows](https://github.com/git-for-windows/git/releases/);
* Download this project from Github:
```
    $ git clone https://github.com/danielgp/data-management <local_folder_on_your_computer>
```
> conventions used:
>> <content_within_html_tags> = variables to be replaced with user values relevant strings
* Create a Python Virtual Environment using following command executed from project root folder:
```
    $ python -m venv virtual_environment/
```
* Upgrade pip (PIP is a package manager for Python packages) and SetupTools using following command executed from newly created virtual environment and Scripts sub-folder:
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) -m pip install --upgrade pip
    $ <local_path_of_this_package>/virtual_environment/Scripts/pip(.exe) install --upgrade setuptools --user
```
* Install project prerequisites using following command executed from project root folder:
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) <local_path_of_this_package>/setup.py install
```


## Maintaining local package up-to-date

Once the package is installed is quite important to keep up with latest releases as such are addressing important code improvements and potential security issues, and this can be achieved by following command:
```
    $ git --work-tree=<local_folder_on_your_computer> --git-dir=<local_folder_on_your_computer>/.git/ --no-pager pull origin master
```
- conventions used:
    - <content_within_html_tags> = variables to be replaced with user values relevant strings


## Usage


### Columns Eliminator
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) <local_path_of_this_package>/sources/columns_eliminator.py --input-file <input_file_name__specific_or_with_pattern> --csv-field-separator ","|";"|"|" --columns-to-eliminate-expression <json_list_of_columns_to_eliminate> (--output-log-file <full_path_and_file_name_to_log_running_details>)
```
- conventions used:
    - (content_within_round_parenthesis) = optional
    - <content_within_html_tags> = variables to be replaced with user values relevant strings
    - single vertical pipeline = separator for alternative options

### Filter 
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) <local_path_of_this_package>/sources/filter.py --input-file <input_file_name__specific_or_with_pattern> --csv-field-separator ","|";"|"|" --filter-expression <json_filter_expression> (--output-log-file <full_path_and_file_name_to_log_running_details>)
```
- conventions used:
    - (content_within_round_parenthesis) = optional
    - <content_within_html_tags> = variables to be replaced with user values relevant strings
    - single vertical pipeline = separator for alternative options

### Merging CSV files based on a matching pattern within a given folder to a single CSV file
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) <local_path_of_this_package>/sources/merger.py --input-file <input_file_name__specific_or_with_pattern> --csv-field-separator ","|";"|"|" --output-file <full_path_and_file_base_name_to_generated_file>(.csv) (--output-log-file <full_path_and_file_name_to_log_running_details>)
```
- conventions used:
    - (content_within_round_parenthesis) = optional
    - <content_within_html_tags> = variables to be replaced with user values relevant strings
    - single vertical pipeline = separator for alternative options

### Moving based on a matching pattern from a given folder to another folder
```
    $ <local_path_of_this_package>/virtual_environment/Scripts/python(.exe) <local_path_of_this_package>/sources/mover.py --input-file <input_file_name__specific_or_with_pattern> --output-directory <output_directory_full_path> (--output-log-file <full_path_and_file_name_to_log_running_details>)
```
- conventions used:
    - (content_within_round_parenthesis) = optional
    - <content_within_html_tags> = variables to be replaced with user values relevant strings
    - single vertical pipeline = separator for alternative options

## Change Log / Releases detailed

see [CHANGE_LOG.md](CHANGE_LOG.md)

## Code of conduct

Use [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md)

## Features to request template

Use [feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md)

## Bug report template

Use [bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md)

## Code quality analysis
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/danielgp/data-management/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/danielgp/data-management/?branch=master)

## Build Status
[![Build Status](https://scrutinizer-ci.com/g/danielgp/data-management/badges/build.png?b=master)](https://scrutinizer-ci.com/g/danielgp/data-management/build-status/master)

