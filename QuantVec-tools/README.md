Essential Python modules (install these first):

* beacon_utils - this contains a number of helper functions for mathematical operations and metadata generation
* molgraph - The central module containing the molecular graph class used by most of the tools.

Tools
=====
*	cpscalar   - extract (NG)QTAIM scalar measures for one or more .sumviz files.
*	drproject  - construct eigenvector-space (U-space) trajectories from sequences of .sumviz files.
*	framepath  - for a given BCP in an input .sumviz file (with accompanying wavefunction .wfx), compute bond-path framework. Currently requires a working [AIMAll](https://aim.tkgristmill.com) installation.
*	pathtool   - compute bond-path framework properties.
*	qtrama3    - calculate QTAIM-interpreted Ramachandran plots.
*	sumviz2xyz 	- convert one (or more) .sumviz files to (multi-frame) .xyz format.
*	topviz 	   - visualize molecular graphs and bond-path frameworks (based on [Mayavi](https://github.com/enthought/mayavi)).
*	trajplot  - plot and filter eigenvector-space (U-space) trajectories (based on [matplotlib](https://matplotlib.org/)).

Inputs
======
At the moment, .sumviz files (molecular graphs) and .wfx (wavefunction) files produced by [AIMAll](https://aim.tkgristmill.com) or AIMPAC2 are required. MOLDEN-format files may be converted to .wfx using [MOLDEN2Aim](https://github.com/zorkzou/Molden2AIM) from wavefunctions produced by many electronic structure codes. The result of the conversion may need some manual editing before AIMAll will accept them: the supplementary shell script 'clean_molden_wf' in the 'utils' subdirectory can be used to automate the necessary cleanup editing.
