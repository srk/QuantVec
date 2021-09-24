Authors: Steven Kirk (stevenrkirk@gmail.com) and Samantha Jenkins (samanthajsuman@gmail.com)
BEACON Research Group, College of Chemistry and Chemical Engineering, Hunan Normal University
beacon_utils
============
Library of useful functions for Python programs
Currently contains:
* dotprod    : dot product of two lists of numbers
* modvec     : modulus of vector
* unitvec    : return unit vector
* vecangle   : accurate angle between input vectors
* project    : input vector v1 in coordinate system (v2,v3,v4)
* vectorproduct: Return vector cross product of input vectors a and b (expressed as lists)
* writhe     : writhe of 3-D polyline (list of [x,y,z] objects)
* dihedral   : Calculate dihedral angle (radians) for 4 ordered sets of 3-D coordinates r1,r2,r3,r4 (lists)
* normalvec  : Return the unit normal vector to the plane defined by a triplet of atom positions [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
* numbered_menu: Print a numbered menu of choices, enforce choice. Return an integer for chosen option or 99 (indicating break/exit)
* project    : Project vector v onto unit basis vectors a,b,c and return new vector v2 (expressed as lists)
* repheader  : return a list of strings describing run-time environment of a program
* csvdump    : Dump data as a .csv format file
* progfeed   : Spawn an external executable program, feed it the specified interactive input and
             return the results as a list of strings
