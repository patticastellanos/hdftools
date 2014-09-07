#!/usr/bin/python

import pprint.pprint
#########################################################################
def listhdf(hdf):
    "a function to list the contents of the hdf file"
    
    if hdf.filetype is 'HDF4':
        #look for SD data
        if hdf.SD is not None:
            pprint(hdf.SD.datasets())