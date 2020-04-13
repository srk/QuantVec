Extract scalar values from one or more scalar values from a bond critical point in one or more .sumviz/.sum files.

    > cpscalar -h
    
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
    
    Multiple parameters may appear, in any order, separated by spaces
    Output columns are in the same order as the parameters.

    Examples:
    python cpscalar.py myfile.sumviz C1 C2 --vals rho lap metal H
    python cpscalar.py filelist.txt C1 C2 --vals H stiff pol
    
    Authors: Steven Kirk (stevenrkirk@gmail.com)
             Samantha Jenkins (samanthajsuman@gmail.com)
             Xu Tianlv (xutl@hunnu.edu.cn)
    Bug fixes: 20171029 (discovered by Jiahui)
               20180518 (discovered by Alireza)
               20180706 (SRK)
               20181228 (Tianlv - stress tensor ellipticity added)

    usage: cpscalar [-h]
                    [--vals {rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,st     ress_pol,bpl,gbl,curv,stress_ellip} [{rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip} ...]]
                    infile atom_1_name atom_2_name

    Show critical point scalar values

    positional arguments:
      infile                Name of input file, or file containing list of input
                            filenames
      atom_1_name           First atom specifying BCP of interest
      atom_2_name           Second atom specifying BCP of interest
    
    optional arguments:
      -h, --help            show this help message and exit
      --vals {rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip} [{rho,lap,ellip,H,V,G,K,L,metal,stiff,stress_stiff,stress_ellip,stress_ellip_hessrho,pol,stress_pol,bpl,gbl,curv,stress_ellip} ...]
                            Scalar values to display
