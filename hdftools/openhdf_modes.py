#!/usr/bin/python
import tables as HDF5
import pyhdf.HDF as HDF4
import pyhdf.SD as HDF4SD

""" This is a function to define dictionaries
 for different modes of opening files"""


class HDF4file():
    def __init__(self,SD,VD,VDfile):
        self.SD = SD
        self.VD = VD 
        self.VDfile = VDfile
###########################################################################
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
###########################################################################
def openhdf_modes(filename, filetype):

    # create a dictionary where the read-mode 
    # of the file is linked to a function that
    # reads in the file

    # definition of the modes
    # 'read'   read-only; no data can be modified.
    # 'write'  write; a new file is created (an existing file with the same 
    #               name would be deleted).
    # append   append; an existing file is opened for reading and writing, 
    #       and if the file does not exist it is created.

    #HDF5
    if filetype.upper() == 'HDF5':
        
        def hdf5read(filename):
            file = HDF5.open_file(filename, "r")
            return file
 
        def hdf5write(filename):
            file = HDF5.open_file(filename, "w")
            return file
 
        def hdf5append(filename): 
            file = HDF5.open_file(filename, "a")
            return file

        modehdf = {
            'read'        : hdf5read,
            'write'       : hdf5write,
            'append'      : hdf5append
	    }	

        

    #HDF4
    # this is more complicated because you have
    # two different read types for SDs and VDatas

    
    if filetype.upper() == 'HDF4':
        #SD
        def hdf4readSD(filename):
            SD      = HDF4SD.SD(filename, HDF4SD.SDC.READ)
            if is_empty(SD.datasets()): 
                SD.end()
                SD = None
          
            VDfile  = HDF4.HDF(filename, HDF4.HC.READ)
            try:
                VD      = VDfile.vstart()
            except AttributeError:
                #there are no Vdata in the file
                VD = None
                VDfile.close()
                VDfile = None

            file = HDF4file(SD,VD,VDfile)
            file.filename = filename

            return file

        def hdf4writeSD(filename):
            
            SD     = HDF4SD.SD(filename, HDF4SD.SSDC.WRITE|HDF4SD.SSDC.CREATE|HDF4SD.SSDC.TRUNC)
            if is_empty(SD.datasets()): 
                SD.end()
                SD = None
    
            VDfile = HDF4.HDF.HDF(filename, HDF4.HC.HC.WRITE|HDF4.HC.HC.CREATE|HDF4.HC.HC.TRUNC)
            try:
                VD     = VDfile.vstart()
            except AttributeError:
                #there are no Vdata in the file
                VD = None
                VDfile.close()
                VDfile = None

            file = HDF4file(SD,VD,VDfile)
            file.filename = filename

            return file

        def hdf4appendSD(filename):
            SD     = HDF4SD.SD(filename,HDF4SD.SSDC.WRITE)
            if is_empty(SD.datasets()): 
                SD.end()
                SD = None

            VDfile = HDF4.HDF.HDF(filename,HDF4.HC.HC.WRITE)
            try:
                VD     = VDfile.vstart()
            except AttributeError:
                #there are no Vdata in the file
                VD = None
                VDfile.close()
                VDfile = None

            file = HDF4file(SD,VD,VDfile)
            file.filename = filename

            return file

        modehdf = {
            'read'        : hdf4readSD,
            'write'       : hdf4writeSD,
            'append'      : hdf4appendSD
        }


    return modehdf
    