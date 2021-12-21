Interactive visualization GUI for molecular graphs and optional IAS paths (AIMAll .sumviz format) with optional associated paths in .path format from 'framepath' or the 'extreme' program from the AIMPAC2 Fortran package. This code can save rendered screenshots and 3-D models in X3D format.

Depends on: Traits, TraitsUI, mayavi2, PyQT5, VTK.

Some environment variables may need to be set to get Mayavi to display the structures (see Mayavi documentation and examples). There appears to be some issues with Mayavi and the exact version of VTK used, but if the Mayavi examples work for you then this should, too.

To see the full set of command line parameters: topviz --help

For a simple display of a .sumviz molecular graph : topviz --input mysumvizfile.sumviz

Eigenvector path data may be included using the --bondvectors option.
