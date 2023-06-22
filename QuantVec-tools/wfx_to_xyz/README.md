Reads a  .wfx file (nuclear coordinates in atomic units), or text file containing a list of names of .wfx files (one per line) and produces 
an .xyz file containing the molecular geometry (i.e. nuclear positions in Angstrom units), with the extracted total energy placed in the
.xyz file comment line. If a list of names of .wfx files is provided as input, a multi-step .xyz file is produced with the 'frames' of coordinate
data written in the same order as listed in the text file. The .xyz file may then be read by other tools or visualized/animated using, e.g. 
the Avogadro GUI program. 

Usage: wfx_to_xyz <inputfile/filelist> <output XYZ file name>
