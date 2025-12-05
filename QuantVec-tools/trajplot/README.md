```

trajplot --help
usage: trajplot [-h] [--matrix {hessian,stress,ask=default}] [--modulus {no,yes,ask}] [--zerothresh ZEROTHRESH]
                [--maxturn MAXTURN] [--csvfile CSVFILE] [--title TITLE] [--autoscale] [--viewpoint VIEWPOINT]
                [--nograph]
                filelist

Trajectory plotter for drproject3 results
==========================================

positional arguments:
  filelist              File containing list of data files to plot

options:
  -h, --help            show this help message and exit
  --matrix {hessian,stress,ask=default}
                        Matrix used to provide projection eigenvectors
  --modulus {no,yes,ask}
                        Whether or not to use the modulus of the projected coordinates to plot: yes,no,ask(default)
  --zerothresh ZEROTHRESH
                        Integer N, where projection coordinates smaller than 10^(-N) are forced to zero: (default N=14)
  --maxturn MAXTURN     Maximum turn angle to allow in filtered path, degrees: (default 60.0)
  --csvfile CSVFILE     Name of .csv file to dump trajectories, multiple sets will have suffix _1,_2 etc.: (default=datafile_n_trj.csv)
  --title TITLE         Title for plot (auto, none, 'requested title string') 
  --autoscale            Autoscale plot on all axes (default: off) 
  --viewpoint VIEWPOINT
                         View orientation as elevation:azimuth:roll (default 30:135:0)
  --nograph             Suppress generation of trajectory graphs

VERSION: 20251101.0001

trajplot
========
Usage: trajplot <file containing list of files in desired sequence>
Input file format: each line has the format
              datafilename linecolour linestyle markersymbol markerfill markersize filterstring
              e.g. data.txt red - o full 5 avg+avg+avg
              Blank lines or lines starting with # are ignored. filterstring = 'none' or sequences of filter operations e.g. 'avg','turn'
              If a header line of the form '# curvelabelstring' is found in the input data header, it is used to set the curve label
```
`trajplot` is run on the output files from `drproject`, specifically the trajectory files (with filename extension .traj). It applies optional filtering as specified for every trajectory data file listed in its input file , as described the program header above. It then produces:
* an interactive 3-D graph GUI using 'Matplotlib' containing the U-space trajectories for each trajectory data file. Several of the command line flags allow this interactive view to be customized, and trajectory colors, markers etc. are specified in the input file. This interactive graph can also be entirely suppressed with the `--nograph` command line option, making the program scriptable.
* A CSV-format file of the U-space projections for each input trajectory, to allow plotting and processing of trajectories using other graphing software
* A summary at the end of the standard output containing the 'drmax' values for each trajectory, i.e. the sizes of the 'bounding box' of the trajectory in each U-space dimension. This information may be used within NG-QTAIM to calculate the F,C and A parameters (when calculated for both clockwise and counterclockwise circularly polarized laser pulses, for example).
* IN PROGRESS: HTML+JavaScript output, with the Plotly graphics library, providing a single HTML file that can be easily distributed and loaded by Web browsers, to give an alternative web-based GUI.

Example
```
trajplot plot.txt --matrix hessian --modulus no --title 'CW C1-C2' --autoscale | tee C1-C2_trajplot_ouput_drmax.txt
```
The `filterstring` specified in the input file, applied to reduce noise in the trajectory consists of either `none`, or one or more repetitions of the 'turn' filter or 'av' (2-point averaging) filter, applied successively and joined by the '+' character. For instance, the most commonly-used filter string, i.e. the standard Kolmogorov-Zurbenko data filter is equivalent to the filter string 'av+av+av', i.e. 3 averaging passes.
