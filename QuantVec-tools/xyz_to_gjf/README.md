A very simple templating engine to generate G09 input files from a (possibly multi-step) .xyz file containing molecular geometries and a standard 'template' G09 input file containing 'tags' like <xyz> (the atomic coordinates are substituted here) and <name> (the basename of the input file). Output files have numbered suffixes (e.g. _0001.gjf, _0002.gjf ...) corresponding to the step number in the input .xyz file.

 
This simplifies generation of large numbers of G09 input files where all that differs between each generated file is the atomic coordinates - the common elements of each file are specified once, in the template. This is particularly useful for , e.g. generating many 'single-point' converged wavefunction calculations corresponding to each geometry held in the 'frames' of a multi-step.xyz file. Such multi-step .xyz files can be associated with time-ordered sequences (i.e. dynamics) or other types of sequence (e.g. IRC or parameter scans).

