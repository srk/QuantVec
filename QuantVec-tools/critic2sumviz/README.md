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
This program reads the output of the versatile CRITIC2 (https://github.com/aoterodelaroza/critic2) code, which can, among many other things, locate and evaluate critical points in fields produced by electronic structure codes, such as grids of electron density. It can also read the optional subsidiary output of CRITIC2 produced by the FLUXPRINT keyword within that program (and recorded in a file with suffix `_flux.txt`) , which can contain detailed information on bond-paths.

It produces a .sumviz-format molecular graph file which contains both details of the critical points *and* the bond-paths, together with a .path-format file for every section of every bond-path between nuclear attractors. For an example a bond path, complete with its bond-critical point (BCP), between attractors A and B might, schematically, look like:

```
A----BCP-------B
```
In this example, a separate .path file will be produced for each section (A----BCP and BCP------B) of the bond path. 
The .path files may then be used for visualization purposes using the `topviz` GUI program, or analysed further using the `pathtool` program. The files contain not only sequences of position coordinates defining each path, but also (optionally) scaled e<sub>1</sub> and e<sub>2</sub> eigenvectors of the Hessian of the electronic charge density at every point along the path. These are used within NG-QTAIM to define *p*,*p'*,*q*,*q'* - paths associated with each bond-path.
