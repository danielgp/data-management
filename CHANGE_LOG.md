# Change Log for Data Management package


## Version 0.4.4 release on 2020-04-24
- internal code re-organizations;

## Version 0.4.3 release on 2020-04-16
- just internal code optimizations;

## Version 0.4.2 release on 2020-04-15
- corrected main configuration file (JSON format);

## Version 0.4.1 release on 2020-04-14
- corrected an input check for mover;

## Version 0.4.0 release on 2020-04-14
- new script named columns_eliminator has been added to facilitate elimination of a single or multiple columns from a single or multiple CSV files (is specified columns does not exist in one or multiple files no error will be generated and files will be overwritten if at least one columns specified to be removed has been found); 
- filter, merger and mover are now accepting either a specific input file or a match pattern based on which multiple files will be considered;

## Version 0.3.5 release on 2020-04-14
- mover is now capable of overwrite if file already exists, instead of failing;

## Version 0.3.4 release on 2020-04-07
- ensured README file is properly recognized within same directory sa setup script;
- internal code tweak (switch to relative package name);

## Version 0.3.3 release on 2020-04-07
- added an optional log parameter to mover as well;
- internal code tweak (switch to relative package name);

## Version 0.3.2 release on 2020-04-06
- tweaked documentation to ensure accuracy;
- added header information to main scripts;

## Version 0.3.1 release on 2020-04-06
- bringing documentation up-to-date;

## Version 0.3.0 release on 2020-04-06
- added feature to filter CSV file based on JSON expression given rule;

## Version 0.2.2 release on 2020-04-05
- related documentation added;

## Version 0.2.1 release on 2020-04-05
- internal project structure changed;

## Version 0.2.0 release on 2020-04-05
- added feature to move multiple files to a destination folder;

## Version 0.1.0 release on 2020-04-05
- added feature to merge multiple CSV files into a consolidated CSV;

