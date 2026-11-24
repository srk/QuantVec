Generator for text files containing columns of t (time), E_x (field in x-direction), E_y(field in y-direction), E_z (field in Z-direction). 
Created for use with the Octopus code, but will work for other codes too. Uses the Numpy library.

Supplied as a .tar.gz for easy installation using 'pip'.

* Syntax:
*  ```
   octopus_laser <.cfg file> <output file> [--verbose] [--onefile]
   ```

   Running an nonsense command line, e.g.
   ```
   octopus-laser blah blah
   ```
   will generate an example template for the .cfg file.

   The --onefile option creates a single output file. If this option is omitted, 3 separate output files for the X,Y,Z components will be generated. In the case,
   the columns in each file will be: time, real part, imaginary part.

   Multiple fields can be specified in a config file, and the output will be the sum of all the defined fields. This allows experimentation with
   pulse trains, multicolor pulses, superimposed fields, etc.
   
