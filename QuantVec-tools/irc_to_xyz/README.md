This program parses the Gaussian output (.log) file produced during either 1) an IRC calculation along a reaction pathway, or 2) a constrained geometric optimization 
using a parameter scan carried out using the Opt(ModRedundant) keyword (e.g. dihedral scan). It produces a multi-step (multi-frame, in the dynamics or animation sense)
.xyz file, with one frame for each new geometrical structure, and the corresponding value of the reaction coordinate in the comment line of each frame.  
