# QuantVec
The successor to AIMPAC2 https://github.com/srk/AIMPAC2-Suite .

Tools and main codes will be migrated into this repository in stages, beginning with the existing AIMPAC2-Suite tools.

The research group pip repository (https://beaconresearch.org/pip/) is currently the main home of many of the Python packages: this Github repository is currently being updated with the most recent research group versions. If you cannot find a package here, please look there, or contact stevenrkirk@gmail.com for the most recent packages. 

# QuantVec tools
Most QuantVec tools are implemented in Python 3 and are released as 'pip'-installable source distribution archives, following a calendar versioning scheme. Most of these Python-based tools also depend on the modules 'beacon_utils' and 'molgraph', so these must be installed prior to the tools themselves.

The intended installation procedure is (using 'pip3' as a synonym for 'pip'):

    pip3 install beacon_utils-YYYYMMDD.N.tar.gz
    pip3 install molgraph-YYYYMMDD.N.tar.gz

then

    pip3 install toolname-YYYYMMDD.N.tar.gz

# Utilities
A number of utility programs (mostly Bash scripts) may be found in the QuantVec-tools/utils folder.
