Aligns the frames of an input .xyz file so that 'atom1' is always at (0.0,0.0,0.0), that 'atom2' always lies along the x-axis and that 'atom3' always lies somewhere in the x-y plane. Good for, e.g. making torsional motions clearer for animation purposes. The program assumes that the atoms in each frame are always numbered in the same order (e.g. atom 5 is the 5th atom to appear in the .xyz frame coordinates in EVERY frame).

    > xyzalign -h
    xyzalign: Version 20181220.0001
    usage: xyzalign [-h] [--alignby ALIGNBY]
                    xyzfilein xyzfileout atom1name atom2name atom3name
    
    xyzalign
    
    positional arguments:
      xyzfilein          XYZ file to be aligned
      xyzfileout         Output XYZ file
      atom1name          Name/number of atom to place at origin
      atom2name          Name/number of atom to place on x-axis
      atom3name          Name/number of atom to define x-y plane
    
    optional arguments:
      -h, --help         show this help message and exit  
      --alignby ALIGNBY  Frame number in input, 'all' or single-frame XYZ
                         filename, to use as alignment reference (default: all)
