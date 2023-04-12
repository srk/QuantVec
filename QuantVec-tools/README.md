Essential Python modules (install these first):
========================
* beacon_utils - this contains a number of helper functions for mathematical operations and metadata generation
* molgraph - The central module containing the molecular graph class used by most of the tools.

Tools
=====
*	cpscalar   - extract (NG)QTAIM scalar measures for one or more .sumviz files.
*	drproject  - construct eigenvector-space (U-space) trajectories from sequences of .sumviz files.
*	framepath  - for a given BCP in an input .sumviz file (with accompanying wavefunction .wfx), compute bond-path framework. Currently requires a working [AIMAll](https://aim.tkgristmill.com) installation.
*	pathtool   - compute bond-path framework properties.
*	qtrama3    - calculate QTAIM-interpreted Ramachandran plots (based on [matplotlib](https://matplotlib.org/)).
*	sumviz2xyz 	- convert one (or more) .sumviz files to (multi-frame) .xyz format.
*	topviz 	   - visualize molecular graphs and bond-path frameworks (based on [Mayavi](https://github.com/enthought/mayavi)).
*	trajplot  - plot and filter eigenvector-space (U-space) trajectories (based on [matplotlib](https://matplotlib.org/)).

Utilities
=========
* clean_molden_wf - (Bash) script to clean up .wfx files produced by [MOLDEN2Aim](https://github.com/zorkzou/Molden2AIM).
* allbcpsframepath - (Bash) wrapper script around 'framepath': automates calculation of bond-path frameworks for every bond-path in a specified input molecular graph. Uses the same command line parameters as 'framepath', except that no BCP needs to be specified (they will all be discovered automatically).

Inputs
======
At the moment, .sumviz files (molecular graphs) and .wfx (wavefunction) files produced by [AIMAll](https://aim.tkgristmill.com) or QuantVec are required. MOLDEN-format files may be converted to .wfx using [MOLDEN2Aim](https://github.com/zorkzou/Molden2AIM) from wavefunctions produced by many electronic structure codes. The result of the conversion may need some manual editing before AIMAll will accept them: the supplementary shell script 'clean_molden_wf' in the 'utils' subdirectory can be used to automate the necessary cleanup editing.

Additional utility packages
===========================
These packages do not require the 'molgraph' or 'beacon_utils' Python modules.

* irc_to_xyz - extract intermediate sets of molecular coordinates from a Gaussian G09 output (.log) file produced by 1) tracing down an Intrinsic Reaction Coordinate (IRC) path from a transition state, or 2) performing a constrained optimization with a parameter scan (e.g. a PES scan of a torsion angle). The output is in .xyz format.  
If the input comes from an IRC calculation, the values of the reaction cordinate are included in the comment line of each 'frame' of the output .xyz file. Such multi-step xyz files can be visualized and animated in a number of molecular visualization codes, e.g. Avogadro.

* xyz_to_gjf - a very simple templating engine to generate G09 input files from a (possibly multi-step) .xyz file containing molecular geometries and a 
standard 'template' G09 input file containing 'tags' like \<xyz> (the atomic coordinates are substituted here) and \<name> (the basename of the input file).
Output files have numbered suffixes (e.g. \_0001.gjf, \_0002.gjf ...) corresponding to the step number in the input .xyz file.  
This simplifies generation of large numbers of G09 input files where all that differs between each generated file is the atomic coordinates - the common elements of each file are specified *once*, in the template. This is particularly useful for , e.g. generating many 'single-point' converged wavefunction calculations corresponding to each geometry held in the 'frames' of a multi-step.xyz file. Such multi-step .xyz files can be associated with time-ordered sequences (i.e. dynamics) or other types of sequence (e.g. IRC or parameter scans).

* xyzalign - syntax 'xyzalign input.xyz aligned.xyz N1 N2 N3'.  
Given a molecular structure file 'input.xyz', produce a reoriented version 'aligned.xyz' preserving all internal bond lengths, angles etc. where atom number N1 has been placed at the origin of the coordinates system (0.0, 0.0, 0.0), atom number N2 is placed on the positive x-axis, and atom number N3 lies in the x-y plane. N1,N2,N3 are integers, the first atom being atom 1.  
As this program can be used on multi-step .xyz input files, it can be to used to help clarify or better demonstrate intramolecular motions, with judicious choices of N1, N2 and N3. 
