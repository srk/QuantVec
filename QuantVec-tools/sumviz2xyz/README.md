Convert a named .sumviz file (or list of .sumviz filenames, one per line, in a text filelist) to a multi-frame .xyz file. This code is mostly used for round-tripping calculated structures. It attempts to preserve at least some of the original metadata in the comment line of each frame of the .xyz file.


    > sumviz2xyz -h
    usage: sumviz2xyz [-h] [--verbose] inputfile outputfile
    
    Convert all molecular graph data files to simple XYZ format
    ===========================================================
    
    positional arguments:
      inputfile   Input file or filelist(.txt)
      outputfile  XYZ file name for output
    
    optional arguments:
      -h, --help  show this help message and exit
      --verbose   Show more verbose screen output
