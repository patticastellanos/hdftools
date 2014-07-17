===========
HDF Tools
===========

HDF Tools is a wrapper for the file handling functionality in `pyhdf` and and `PyTables`.  It provides a single interface to read, create, and append any HDF file regardless of its format: HDF4, HDF5, or HDF-EOS.
It is most useful for earth scientists who want to use a simple function call to handle data files from multiple sources. Typical usage
often looks like this:

    #!/usr/bin/env python

    from hdftools import opnenhdf

    file = openhdf(filename)


Installation
=========

HDF Tools relies on having the HDF4 and HDF5 libraries, as well as the pyhdf and PyTables packages installed. Below are instructions for downloading the most current versions (as of the date of this publcation) of these libraries and packages on Mac OSx.  Please see the deverloper websites for instruction for other platforms or versions.

	HDF4 Library
	--------------
	1. Download and install the JPEG, PNG, and SZIP libraries
		* JPEG and PNG:
			* Download the disk image from this `link <http://ethan.tira-thompson.com/Mac%20OS%20X%20Ports_files/libjpeg-libpng%20%28universal%29.dmg>`_.
			* Follow the installers prompts and complete the installation in ${LibDir}.
		* SZIP:
			* Downlaod the tarball to your install directory
				curl http://www.hdfgroup.org/ftp/HDF/HDF_Current/src/hdf-4.2.10.tar.gz | tar xzf -
			* Execute the following at the command line:
				./configure --prefix=${LibDir} --enable-shared --enable-production
				make
				make check
				make install
	2. Download the latest version of HDF4:
		curl http://www.hdfgroup.org/ftp/HDF/HDF_Current/src/hdf-4.2.10.tar.gz | tar xzf -
	3. Execute the following at the command line:
		./configure --prefix=${LibDir} --disable-fortran --enable-production --with-szlib=${LibDir} CPPFLAGS=-I${LibDir}/include LDFLAGS=-L${LibDir}/lib
		make
		make check
		make install

	pyhdf
	-------------
	1. Download the latest version of pyhdf
	svn checkout https://pysclint.svn.sourceforge.net/svnroot/pysclint/trunk/pyhdf
	2. Execute at the command line
	sudo env INCLUDE_DIRS=${LibDir}/include LIBRARY_DIRS=${LibDir}/lib python setup.py install

	HDF5 Library
	--------------
	1. Download the latest version of HDF5
		curl http://http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.13.tar.gz | tar xzf -
	2. Execute at the command line:
		./configure --prefix=${LibDir} --disable-fortran --enable-production --with-	szlib=${LibDir} CPPFLAGS=-I${LibDir}/include LDFLAGS=-L${LibDir}/lib
		make
		make check
		make install

	PyTables
	--------------
	1. Install nuexpr
		easy_install numexpr
	2. Install cython
		easy_install cython
	3. Download latest version from http://downloads.sourceforge.net/project/pytables/pytables 
	4. Execute at the command line:
	sudo python setup.py build_ext  --hdf5=${LibDir} --inplace
	sudo python setup.py install  --hdf5=${LibDir}

