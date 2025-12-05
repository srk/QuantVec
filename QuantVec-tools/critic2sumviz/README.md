```
$ critic2sumviz --help

critic2sumviz
========
Convert CRITIC2 output files to sumviz format for visualization

20251205.0001
Molgraph module version: 20250919.0001
beacon_utils module version: 20170808.0001
usage: critic2sumviz [-h] [--scaling SCALING] [--celllabels] infile

critic2sumviz

positional arguments:
  infile             CRITIC2 output file to convert

options:
  -h, --help         show this help message and exit
  --scaling SCALING  Optional scaling to apply to bondvectors ['ellipticity','none']
  --celllabels       Generate cell index labels on the atoms
```
This program reads the output of the versatile [CRITIC2](https://github.com/aoterodelaroza/critic2) code, which can, among many other things, locate and evaluate critical points in fields produced by electronic structure codes, such as grids of electron density. It can also read the optional subsidiary output of CRITIC2 produced by the FLUXPRINT keyword within that program (and recorded in a file with suffix `_flux.txt`) , which can contain detailed information on bond-paths.

It produces a .sumviz-format molecular graph file which contains both details of the critical points *and* the bond-paths, together with a .path-format file for every section of every bond-path between nuclear attractors. For an example a bond path, complete with its bond-critical point (BCP), between attractors A and B might, schematically, look like:

```
A----BCP-------B
```
In this example, a separate .path file will be produced for each section (A----BCP and BCP------B) of the bond path. 
The .path files may then be used for visualization purposes using the `topviz` GUI program, or analysed further using the `pathtool` program. The files contain not only sequences of position coordinates defining each path, but also (optionally) scaled e<sub>1</sub> and e<sub>2</sub> eigenvectors of the Hessian of the electronic charge density at every point along the path. These are used within NG-QTAIM to define *p*,*p'*,*q*,*q'* - paths associated with each bond-path.

Systems with periodic boundaries
================================
If CRITIC2 is informed that the wavefunctions or gridded densities supplied to it are for a *crystal* (i.e. with periodic boundaries), then the crystal graph (analogous to the molecular graph) produced, by default, is for the irreducible cell - the keyword NOSYMM can be used to prevent this.  In this case, the `--celllabels` command-line parameter for `critic2sumviz` should be supplied. `critic2sumviz` then makes copies of any nuclei and critical points located on each corner, edge or face of the primitive cell. This also changes the output .sumviz file in two ways:
1. It encodes the crystal cell parameter information in the text `Wfx Title` field of the .sumviz file, thus:
```
Wfx Title:  density.cube CRYSTAL {0.0,0.0,0.0} {5.6445,0.0,0.0} {0.0,5.6445,0.0} {0.0,0.0,5.6445}
```
for compatibility with other programs which read .sumviz files. For example, the `topviz` program will, by default, use this information to draw the boundaries of the unit cell.

2. Each nucleus and nuclear attractor critical point, including all the generated periodic copies, created in the .sumviz file will have a 4-character code attached to its name, of the form '_ABC'. Each of the characters ABC in this cell label will either be '0' (associated with the original cell), 'p' ('plus 1') or 'm'('minus 1'). So for example, a nuclear critical point called **H1_0pm** will be the periodic copy of the H1 nucleus in the original cell (hence H1_000) which is shifted by a vector (0*a)+(1*b)+(-1*c), where a,b,and c are the cell lattice vectors. Consequently, BCP names (as they link two nuclear attractors) also expand. When the .sumviz file is visualized using `topviz`, the cell labels are suppressed by default. This helps to keep track of critical points on the cell edges and bondpaths which cross the boundaries of the unit cell.
