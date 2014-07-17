#!/usr/bin/python
# This is a function to define dictionaries
# for different modes of opening files

def openhdf_modes(filename, filetype,hdf4type=None):

    modehdf = None
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

    if filetype.upper() == 'HDF4' and hdf4type is None:
        print 'Please provide an HDF4type'
        print 'Your options are HDF4type = "SD" or "VD"'
        return

    if filetype.upper() == 'HDF5':
        import tables as HDF5

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
    # this is more comlicated because you need to know if
    # you want to read a Scientific Dataset or a Vdata

    
    if filetype.upper() == 'HDF4':
        #SD
        if hdf4type.upper() == 'SD':
            import pyhdf.SD as HDF4

            def hdf4readSD(filename):
                file = HDF4.SD(filename, HDF4.SDC.READ)
                file.filename = filename
                return file

            def hdf4writeSD(filename):
                file = HDF4.SD(filename, HDF4.SSDC.WRITE|HDF4.SSDC.CREATE|HDF4.SSDC.TRUNC)
                file.filename = filename
                return file

            def hdf4appendSD(filename):
                file =HDF4.SD(filename,HDF4.SSDC.WRITE)
                file.filename = filename
                return file


            modehdf = {
                    'read'        : hdf4readSD,
                    'write'       : hdf4writeSD,
                    'append'      : hdf4appendSD
            }


        #VData
        if hdf4type.upper() == 'VD':
            import pyhdf.HDF as HDF4
            import pyhdf.VS as HDF4VS

            def hdf4readVD(filename):
                f = HDF4.HDF(filename, HDF4.HC.READ)
                file = f.vstart()
                file.filename = filename
                return file

            def hdf4writeVD(filename):
                f = HDF4.HDF(filename, HDF4.HC.WRITE|HDF4.HC.CREATE|HDF4.HC.TRUNC)
                file = f.vstart()
                file.filename = filename
                return file

            def hdf4appendVD(filename):
                f =HDF4.HDF(filename,HDF4.HC.WRITE)
                file = f.vstart()
                file.filename = filename
                return file

            modehdf = {
                    'read'        : hdf4readVD,
                    'write'       : hdf4writeVD,
                    'append'      : hdf4appendVD
            }


    return modehdf
    