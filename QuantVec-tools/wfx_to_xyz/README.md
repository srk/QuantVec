Reads a  .wfx file (nuclear coordinates in atomic units), or text file containing a list of names of .wfx files (one per line) and produces 
an .xyz file containing the extracted molecular geometry (i.e. nuclear coordinates in Angstrom units), with the extracted total energy placed in the
.xyz file comment line.


A typical .xyz file consists of the following lines:

Number of Atoms (integer)

Comment line (arbitrary string)




followed by lines (one per atom) with the format:




Atom_element_name X_coordinate Y_coordinate Z_coordinate




If a text file containing names of .wfx files is used as input, the output .xyz file will contain one 'frame' of nuclear coordinate data for each
.wfx file, with the geometry data written in the same order as listed in the text file. The resulting 'multi-step' .xyz file may then be read by other tools or 
visualized/animated using, e.g. the Avogadro GUI program. 


Usage: wfx_to_xyz <inputfile/text_filelist> <output XYZ file name>
