# -*- coding: utf-8 -*-
"""
Authors: Steven Kirk (stevenrkirk@gmail.com) and Samantha Jenkins (samanthajsuman@gmail.com)
BEACON Research Group, College of Chemistry and Chemical Engineering, Hunan Normal University

beacon_utils
============

Library of useful functions for Python programs
Currently contains:

dotprod    : dot product of two lists of numbers
modvec     : modulus of vector
unitvec    : return unit vector
vecangle   : accurate angle between input vectors
project    : input vector v1 in coordinate system (v2,v3,v4)
vectorproduct: Return vector cross product of input vectors a and b (expressed as lists)
writhe     : writhe of 3-D polyline (list of [x,y,z] objects)
dihedral   : Calculate dihedral angle (radians) for 4 ordered sets of 3-D coordinates r1,r2,r3,r4 (lists)
normalvec  : Return the unit normal vector to the plane defined by a triplet of atom positions [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
numbered_menu: Print a numbered menu of choices, enforce choice. Return an integer for chosen option or 99 (indicating break/exit)
project    : Project vector v onto unit basis vectors a,b,c and return new vector v2 (expressed as lists)
repheader  : return a list of strings describing run-time environment of a program
csvdump    : Dump data as a .csv format file
progfeed   : Spawn an external executable program, feed it the specified interactive input and
             return the results as a list of strings
 
"""
from __future__ import print_function, division  # originally for Python 2 compatibility
from builtins import input
import io,math,sys,os,csv,subprocess

__version__ = "20200708.0001"

def dotprod(u,v):
    """
    Simple dot (scalar) product of two lists of numbers (assumed to be the same length)
    """
    result = 0.0
    for i in range (0,len(u)):
        result = result + (u[i]*v[i])
    return result

def modvec(u):
    """
    Modulus (magnitude) of an input vector u (provided as a list)
    """
    import math
    return(math.sqrt(dotprod(u,u)))

def unitvec(u):
    """
    Given a vector u, return the unit vector
    """
    modulus = math.sqrt((u[0]*u[0])+(u[1]*u[1])+(u[2]*u[2]))
    return([u[0]/modulus, u[1]/modulus, u[2]/modulus])

def vecangle(u,v):
    """
    Calculate as accurately as possible the angle between two 3-component vectors u and v.
    This formula comes from W. Kahan's advice in his paper "How Futile are Mindless Assessments
    of Roundoff in Floating-Point Computation?" (https://www.cs.berkeley.edu/~wkahan/Mindless.pdf),
    section 12 "Mangled Angles."
    θ=2 atan2(|| ||v||u−||u||v ||, || ||v||u+||u||v ||)
    """
    modu = modvec(u)
    modv = modvec(v)
    vmodu = [modu*v[0] , modu*v[1], modu*v[2] ]
    umodv = [modv*u[0] , modv*u[1], modv*u[2] ]
    term1 = [umodv[0]-vmodu[0], umodv[1]-vmodu[1], umodv[2]-vmodu[2]]
    modterm1 = modvec(term1)
    term2 = [umodv[0]+vmodu[0], umodv[1]+vmodu[1], umodv[2]+vmodu[2]]
    modterm2 = modvec(term2)
    return (2.0*math.atan2(modterm1,modterm2))
    

def project(v,ua,ub,uc):
    """
    Project vector v onto unit basis a,b,c and return new vector v2
    """
    v2x = dotprod(v,ua)
    v2y = dotprod(v,ub)
    v2z = dotprod(v,uc)
    return [v2x,v2y,v2z]
    
def vectorproduct(a,b):
    """
    Return vector cross product of input vectors a and b
    """
    a1, a2, a3 = a
    b1, b2, b3 = b
    return [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1]

def writhe(r):
    """
    Writhe of a 3D space polyline, coordinates in
    a list r
    https://en.wikipedia.org/wiki/Writhe
    """
    n = len(r)-1  # number of line segments
    wr = 0.0
    for i in range(2, n+1):  # line segment i , 2->n inclusive
        for j in range(1,i): # line segment j, j<i
            r1 = r[i-1]
            r2 = r[i]
            r3 = r[j-1]
            r4 = r[j]
            r12 = [ r2[0]-r1[0],r2[1]-r1[1],r2[2]-r1[2] ]
            r13 = [ r3[0]-r1[0],r3[1]-r1[1],r3[2]-r1[2] ]
            r14 = [ r4[0]-r1[0],r4[1]-r1[1],r4[2]-r1[2] ]
            r23 = [ r3[0]-r2[0],r3[1]-r2[1],r3[2]-r2[2] ]
            r24 = [ r4[0]-r2[0],r4[1]-r2[1],r4[2]-r2[2] ]
            r34 = [ r4[0]-r3[0],r4[1]-r3[1],r4[2]-r3[2] ]
            tn1 = vectorproduct(r13,r14)
            tn2 = vectorproduct(r14,r24)
            tn3 = vectorproduct(r24,r23)
            tn4 = vectorproduct(r23,r13)
            print('n={0}, i={1}, j={2} '.format(n,i,j))
            n1 = unitvec(tn1)
            n2 = unitvec(tn2)
            n3 = unitvec(tn3)
            n4 = unitvec(tn4)
            omegas = math.asin(dotprod(n1,n2))+math.asin(dotprod(n2,n3))+math.asin(dotprod(n3,n4))+math.asin(dotprod(n4,n1))   
            r3412 = vectorproduct(r34,r12)
            tmp = dotprod(r3412,r13)
            wofp = math.copysign(omegas/(4.0*math.pi) , tmp)
            wr = wr + wofp
    wr = 2.0*wr        
    return wr
 
    
def dihedral(r1,r2,r3,r4):
    """
    dihedral
    =======
    Calculate dihedral angle associated with 4 sets of ordered 3-D Cartesian coordinates r1,r2,r3,r4.
    Returns value in radians.
    """
    q1 = [r2[0]-r1[0],r2[1]-r1[1],r2[2]-r1[2]] # vector r1-r2
    q2 = [r3[0]-r2[0],r3[1]-r2[1],r3[2]-r2[2]] # vector r2-r3
    q3 = [r4[0]-r3[0],r4[1]-r3[1],r4[2]-r3[2]] # vector r3-r4 
    q1cq2 = vectorproduct(q1,q2)
    q2cq3 = vectorproduct(q2,q3)
    # calculate unit normals
    modq1cq2 = math.sqrt(dotprod(q1cq2,q1cq2))
    n1 = [q1cq2[0]/modq1cq2, q1cq2[1]/modq1cq2, q1cq2[2]/modq1cq2]
    modq2cq3 = math.sqrt(dotprod(q2cq3,q2cq3)) 
    n2 = [q2cq3[0]/modq2cq3, q2cq3[1]/modq2cq3, q2cq3[2]/modq2cq3] 
    # orthogonal unit vectors
    u1 = n2
    modq2 = math.sqrt(dotprod(q2,q2))
    u3 = [q2[0]/modq2, q2[1]/modq2, q2[2]/modq2]
    u2 = vectorproduct(u3,u1)
    # now the angle
    angle = -math.atan2(dotprod(n1,u2),dotprod(n1,u1))
    return angle

def normal_vec(triplet):
    """
    Return the unit normal vector to the plane defined by a triplet of atom positions [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
    """
    p1 = [triplet[0][0], triplet[0][1], triplet[0][2]]
    p2 = [triplet[1][0], triplet[1][1], triplet[1][2]]
    p3 = [triplet[2][0], triplet[2][1], triplet[2][2]]
    r1 = [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    r2 = [p3[0]-p2[0], p3[1]-p2[1], p3[2]-p2[2]]
    normvec = vectorproduct(r1,r2)
    modnormvec = math.sqrt(dotprod(normvec,normvec))
    return [normvec[0]/modnormvec,normvec[1]/modnormvec,normvec[2]/modnormvec] 
    
    
def numbered_menu(menutitle,optionlist):
    """
    numbered_menu
    -------------
    Given a menu title string and a list of strings to display as menu items, show a text menu
    with the menu items in a numbered list and ask the user to input a number to indicate their choice. 
    Returns an integer according to the user selection, with the integer value 99 reserved as a
    'back/exit' flag. 
    
    Example: 
    n = numbered_menu('Menu Title',['First option','Second option','Third option'])
    print("You chose option: {0}".format(n))
    
    """
    while True:
        print("{0}".format(menutitle))
        numitems = len(optionlist)
        for i in range(1, numitems+1):
            print("{0}: {1}".format(i,optionlist[i-1]))
        print("")
        try:
            val = int(input("Enter choice or 99 to go back/exit: "))
        except ValueError:
            print("Invalid option - please choose one of the numbered options or 99 to go back/exit")
            continue
        # Test if values in range, or 99 as escape value
        if ((val == 99) or ((val > 0) and (val < numitems+1))):
            break        
        print("Invalid option - please choose one of the numbered options or 99 to go back/exit")
        continue
    return val

def repheader():
    """
    Return a list of strings describing run-time environment for data provenance/reproducibility purposes
    """
    header=[]
    header.append("Running {0} on {1} using Python {2}".format(sys.argv[0],sys.platform,sys.version))
    header.append("Current working directory: {0}".format(os.path.abspath(os.getcwd())))
    header.append(' '.join(sys.argv))
    return(header)
    
def csvdump(csvfile,header,data):
    """
    Dump a CSV file to specified filename 'csvfile'
    Start file with list of header line strings
    Continue with data lines (list of lists)
    Close file after creation
    """
    if not csvfile == 'none':
        with open(csvfile,'w',newline='') as csvf:
            csvwriter = csv.writer(csvf, dialect='excel',delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            for line in header:
                csvwriter.writerow(['#'+line])
            for row in data:               
                csvwriter.writerow(row)

def progfeed(args,pinput,eflag):
    """
    Spawn an external executable program using a list 'args', feed it the specified interactive
    input list and return the results as a list of strings, with an error flag
    e.g. pname = ['simplecalculator.exe']
         pinput = ['1','4','3','2','5']
    """
    eflag = False
    try:
        message='\n'.join(pinput)+'\n'
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        cmdlog = process.communicate(message)[0]        
        if cmdlog == None:
            print('WARNING: Output not captured')
    except subprocess.CalledProcessError as e:
        eflag = True
        print('Subprocess error')
        print (e.output)
    return(cmdlog)
 