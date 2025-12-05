```
$ cpscalar --help

cpscalar
========
Show the scalar values associated with a specific critical point, 
for one (or a list of) input .sumviz/.sum file(s).
Parameters for --vals:
            'rho'=Charge density, 'lap'=Laplacian, 'ellip'=ellipticity, 'metal'=metallicity
            'stiff' and 'stress_stiff' are the conventional and stress tensor stiffnesses
            'pol' and 'stress_pol' are the conventional and stress tensor polarizabilities
            'stress_ellip' and 'stress_ellip_hessrho' are the conventional and hessrho stress tensor ellipticities
            'H','V','G','K' and 'L' are the correspondingly named energy densities
            'bpl' and 'gbl' are the bond path length and the distance between nuclei (GBL_II)
            'curv' is bpl-gbl
            'stress_ellip' is stress tensor ellipticity = | lambda2/lambda1 |- 1
            'L1','L2','L3' and 'L1s','L2s','L3s' are raw eigenvalues of Hess(Rho) and the stress tensor
            'bcpcheck' activates recalculation of GBL (=GBL_II) and BPL for BCPs
            
Multiple parameters may appear, in any order, separated by spaces
Output columns are in the same order as the parameters.

Examples:
cpscalar myfile.sumviz C1 C2 --vals rho lap metal H
cpscalar filelist.txt C1 C2 --vals H stiff pol L3s

Full command line parameters may be shown by calling the program on the command line 
with the parameter '--help' 

Authors: Steven Kirk (stevenrkirk@gmail.com)
         Samantha Jenkins (samanthajsuman@gmail.com)
         Xu Tianlv (xutl@hunnu.edu.cn)
Bug fixes: 20171029 (discovered by Jiahui)
           20180518 (discovered by Alireza)
           20180706 (SRK)
           20181228 (Tianlv - stress tensor ellipticity added)
           20200511 (Added explicit L1,L2,L3,L1s,L2s,L3s eigenvalues)

usage: cpscalar [-h]
                [--vals {rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip,bcpcheck,L1,L2,L3,L1s,L2s,L3s} [{rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip,bcpcheck,L1,L2,L3,L1s,L2s,L3s} ...]]
                [--filter] [--filteredprefix FILTEREDPREFIX] [--minrho MINRHO] [--trackthresh TRACKTHRESH]
                [--outfile OUTFILE] [--pbc] [--verbose]
                infile atom_1_name atom_2_name

Show critical point scalar values

positional arguments:
  infile                Name of input file, or file containing list of input filenames
  atom_1_name           First atom specifying BCP of interest
  atom_2_name           Second atom specifying BCP of interest

options:
  -h, --help            show this help message and exit
  --vals {rho,lap,ellip,H,V,G,$ cpscalar naibp-h-em-zp-ssr-traj13-S1-0424.sumviz C3 N4 --outfile naibp_out.txt --vals ellip lap rho bpl metal
K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip,bcpcheck,L1,L2,L3,L1s,L2s,L3s} [{rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip,bcpcheck,L1,L2,L3,L1s,L2s,L3s} ...]
                        Scalar values to display
  --filter              Filter mode: creates a new sumviz file (default=off)
  --filteredprefix FILTEREDPREFIX
                        Prefix for filtered .sumviz files (default='filtered')
  --minrho MINRHO       Minimum value of charge density rho for filtered CPs (default=1e-10)
  --trackthresh TRACKTHRESH
                        CP tracking jump distance threshold (default=0.0)
  --outfile OUTFILE     Output results filename
  --pbc                 Periodic boundary conditions should be applied (default=off)
  --verbose             Verbose output
(venv3) srk@THINKPAD:~/physics/molgraph/cpscalar$ 
```

The `cpscalar` program may be applied to one or more molecular graphs in .sumviz format to extract per-CP properties. The main output is to standard output, but optionally an extra output file containing only the requested data in comma-separated text format may be created using the `--outfile` command line flag.

The program can also be used as a filter (see the command line parameters `--filter`, `--filterprefix` and `--nminrho`).

The program attempts to perform tracking across sequences of molecular graph to ensure that the identities of specific critical points are preserved.

Example:
```
$ cpscalar naibp-h-em-zp-ssr-traj13-S1-0424.sumviz C3 N4 --outfile naibp_out.txt --vals ellip lap rho bpl metal

cpscalar
========
Show the scalar values associated with a specific critical point, 
for one (or a list of) input .sumviz/.sum file(s).
Parameters for --vals:
            'rho'=Charge density, 'lap'=Laplacian, 'ellip'=ellipticity, 'metal'=metallicity
            'stiff' and 'stress_stiff' are the conventional and stress tensor stiffnesses
            'pol' and 'stress_pol' are the conventional and stress tensor polarizabilities
            'stress_ellip' and 'stress_ellip_hessrho' are the conventional and hessrho stress tensor ellipticities
            'H','V','G','K' and 'L' are the correspondingly named energy densities
            'bpl' and 'gbl' are the bond path length and the distance between nuclei (GBL_II)
            'curv' is bpl-gbl
            'stress_ellip' is stress tensor ellipticity = | lambda2/lambda1 |- 1
            'L1','L2','L3' and 'L1s','L2s','L3s' are raw eigenvalues of Hess(Rho) and the stress tensor
            'bcpcheck' activates recalculation of GBL (=GBL_II) and BPL for BCPs
            
Multiple parameters may appear, in any order, separated by spaces
Output columns are in the same order as the parameters.

Examples:
cpscalar myfile.sumviz C1 C2 --vals rho lap metal H
cpscalar filelist.txt C1 C2 --vals H stiff pol L3s

Full command line parameters may be shown by calling the program on the command line 
with the parameter '--help' 

Authors: Steven Kirk (stevenrkirk@gmail.com)
         Samantha Jenkins (samanthajsuman@gmail.com)
         Xu Tianlv (xutl@hunnu.edu.cn)
Bug fixes: 20171029 (discovered by Jiahui)
           20180518 (discovered by Alireza)
           20180706 (SRK)
           20181228 (Tianlv - stress tensor ellipticity added)
           20200511 (Added explicit L1,L2,L3,L1s,L2s,L3s eigenvalues)

Input file = naibp-h-em-zp-ssr-traj13-S1-0424.sumviz
Output file =naibp_out.txt
Specified CP = C3-N4
Periodic boundary : False
Tracking: False, tracking threshold = 0.0
Minimum Rho for filtering: 1e-10
Running /home/srk/venv3/bin/cpscalar on linux using Python 3.12.3 (main, Nov  6 2025, 13:44:16) [GCC 13.3.0]
Current working directory: /home/srk/physics/molgraph/cpscalar
/home/srk/venv3/bin/cpscalar naibp-h-em-zp-ssr-traj13-S1-0424.sumviz C3 N4 --outfile naibp_out.txt --vals ellip lap rho bpl metal
Found molgraph module version 20250919.0001
Found beacon_utils module version 20170808.0001
VERSION 20151126.001

Input file extension is .sumviz
Input file naibp-h-em-zp-ssr-traj13-S1-0424.sumviz is a .sumviz/.sum file, calculating for this file only
Searching for BCP C3-N4
=================
Filename : CP_name: Coords (X,Y,Z): ellip: lap: rho: bpl: metal
Wfx Title:  NAIBP motor trajectory 013 EM->ZP                                              

Found 1 matches
Found the matching CP C3-N4
=============
Filename : CP_name: Coords (X,Y,Z): ellip: lap: rho: bpl: metal
naibp-h-em-zp-ssr-traj13-S1-0424.sumviz :C3-N4 C3-N4: Cart. (-2.5406621436, -0.6660883712, -0.7382772382): 0.11757156364: -0.39142843579: 0.15496682388: 2.6065944376: -0.3959007821371955
Program exiting
```
resulting in the additional output in `naibp.out`:
```
# Generated by cpscalar
# Input file is: /home/srk/physics/molgraph/cpscalar/naibp-h-em-zp-ssr-traj13-S1-0424.sumviz
# Searched CP AS TYPED is C3-N4
# Output variables:
# Filename: CP name: CP position: ellip: lap: rho: bpl: metal
naibp-h-em-zp-ssr-traj13-S1-0424.sumviz :C3-N4 C3-N4: Cart. (-2.5406621436, -0.6660883712, -0.7382772382): 0.11757156364: -0.39142843579: 0.15496682388: 2.6065944376: -0.3959007821371955
```

