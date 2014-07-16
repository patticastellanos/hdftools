#!/usr/bin/python
import pyhdf.SD, pyhdf.VS
import tables

# This is a function to close any HDF file

def closehdf(file,verbose=None):

	if verbose is not None:
			print 'Closeing hdf file:', file.filename

	if type(file) in (pyhdf.SD.SD, pyhdf.VS.VS):		
		file.end
	elif type(file) is tables.file.File:
		file.close()


		




	