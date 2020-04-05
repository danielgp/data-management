# Data manipulation package


## What is this repository for?

Facilitate data management (aka manipulation).

## Who do I talk to?

Repository owner is: [Daniel Popiniuc](mailto:daniel.popiniuc@honeywell.com)


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
    $ git clone https://github.com/danielgp/tableau-hyper-management
```
* Create a Python Virtual Environment using following command executed from project root folder:
```
    $ python -m venv virtual_environment/
```
* Upgrade pip (PIP is a package manager for Python packages) and SetupTools using following command executed from newly created virtual environment and Scripts sub-folder:
```
    $ python -m pip install --upgrade pip --user
    $ pip install --upgrade setuptools --user
```
* Install project prerequisites using following command executed from project root folder:
```
    $ python setup.py install
```


## Usage

### Merging CSV files based on a matching pattern within a given folder to a single CSV file
```
    $ python <local_path_of_this_package>/sources/merger.py --input-directory <input_directory_full_path> --input-file-pattern "*.csv" --csv-field-separator ","|";"|"|" --output-file <full_path_and_file_base_name_to_generated_file>(.hyper) (--output-log-file <full_path_and_file_name_to_log_running_details>)
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

