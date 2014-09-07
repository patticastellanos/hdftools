#!/usr/bin/python
import pyhdf.HDF as HDF4
import pyhdf.SD as SD
import tables as HDF5
#########################################################################
def listhdf(hdf):
    "a function to list the contents of the hdf file"
    
    if hdf.filetype is 'HDF4':
        #look for SD data
        if hdf.SD is not None:
            print hdf.SD.datasets()