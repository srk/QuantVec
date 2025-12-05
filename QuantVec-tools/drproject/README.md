```
$ drproject3 --help
Running /home/srk/venv3/bin/drproject3 on linux using Python 3.12.3 (main, Nov  6 2025, 13:44:16) [GCC 13.3.0]
Current working directory: /home/srk/physics/molgraph/drproject/test_data/vtk
Found molgraph module version 20250919.0001
Found beacon_utils module version 20170808.0001

drproject3
==========
Evaluate projections of nuclear and CP positions shifts, and general vectors evaluated
either analytically or by interpolation into VTK-format gridded data
for a general sequence of structures(time sequence, IRC path etc.), onto QTAIM critical point eigenvectors.
A subset of the critical points in each molecular graph are selected for analysis. 

Usage: drproject3 <file containing list of files in desired sequence>

Written in Python 3
NOTE: All displayed CP labels will be alphabetically sorted for ease of comparison
NOTE: Support for Vector fields from VTK files currently incomplete - under development

Modified 20160225: Option to select specific atom as origin, position coordinates changed
Modified 20170203: Can now selecte specified file from list as source of projection axes
Modified 20170402: Aligned output .xyz file now named using selected atom names
Modified 20170409: Now strips path information from CPs to save memory
Modified 20240624: Allow for wider CP names to accomodate annotated BCP names in crystals
Modified 20250601: Allow projection axes and dr shifts to come from different CPs (hybrids)
Modified 20250915: Trap a possible ZeroDivisionError


VERSION 202501205.001

***** NOTE! ***** 
This code ONLY tracks CPs whose connection information is the same
between successive IRC steps!


usage: drproject3 [-h] [--ignorenew] [--verbose] [--fieldprefix FIELDPREFIX] filelist

Projection of CP eigenvectors onto CP shifts ===========================================

positional arguments:
  filelist              File containing list of data files to plot

options:
  -h, --help            show this help message and exit
  --ignorenew           Ignore BCPs that don't exist in the reference
  --verbose             Be verbose in standard output
  --fieldprefix FIELDPREFIX
                        Field vector VTK dataset filename prefix for projection
```
`drproject3` performs projections onto critical point eigenvectors of nuclear or BCP positions shifts or arbitrary external field vectors (IN PROGRESS), given a sequence of .sumviz format molecular graph files, specified as a list of filenames in `filelist`.

The program, presenting the user with text menus to choose options, is intended to be interactive, however it can be scripted using commands piped into standard input.

Outputs
=======
The code outputs a (text) trajectory file with filename extension .traj for the selected critical point. The name of the file varies based on the options selected interactively. The trajectory file contains the eigenvector projections as columns in the file annd may then be further processed using the `trajplot` program.

Examples of usage
=================
* `drproject3 sumviz_filelist.txt | tee drproject_out.txt`
* An example of usage of the program, with .sumviz molecular graph files created for ethane (with Gaussian G09 and AIMAll): (https://github.com/srk/example_datasets_eigenvector_directed_ethane/tree/main/angleminus/singlepoints) and subdirectory `trajectory`.
* [Example data set for NG-QTAIM eigenvector-following trajectories](https://DOI.org/10.5281/zenodo.7830375)
* [Example_datasets:_eigenvector_directed_ethane](DOI.org/10.5281/zenodo.7830375)
