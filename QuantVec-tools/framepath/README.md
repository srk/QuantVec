
This program calculates eigenvectors along bond paths and creates .path files to hold this data. Currently it depends on the availability of AIMExt from the AIMStudio suite (https://aim.tkgristmill.com), which it spawns as a calculation 'engine' for the necessary eigenvectors. On first run, it will create a file 'framepath.cfg', if this file does not already exist in the current directory.
The 'framepath.cfg' file is a simple text configuration file, whose main purpose is to allow the user to specify the full filesystem path to the AIMExt executable.
After installing the pip-installable package (and its other prerequisites), type

framepath --help

for a complete list of command-line parameters
