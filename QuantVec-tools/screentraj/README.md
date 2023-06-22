The 'screentraj' utility for examining the step-length profile of trajectories calculated using 'drproject3'. 


Usage: screentraj \<trajectory data file from drproject3\>


This tool plots the magnitude of the 'dr' step at each point in the trajectory (y-axis), against the trajectory step number.
Hovering the mouse over any data point deemed 'noisy' shows the number of the .sumviz file associated with that step. The line 
in the trajectory input file containing that numbered .sumviz file may then be removed from the trajectory by placing a \# character
at the beginning of the corresponding line in the trajectory data file, causing this point to be ignored in any further processing
by e.g. the 'trajplot' tool.
