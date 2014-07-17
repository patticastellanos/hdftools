#!/usr/bin/python
from test_hdf_type import test_hdf_type
from openhdf_modes import openhdf_modes 

#########################################################################
""" This is a function to open any hdf file and return a file object"""
def openhdf(filename, verbose=None, read_mode=None, hdf4type=None):
	
	if verbose is not None:
		print filename

	""" figure out the flavor of the hdf file
	 HDF4 or 5 (supports 5-EOS as well)"""
	filetype = test_hdf_type(filename)

	# Raise an exception if not an HDF file
	if (filetype is None):
			raise Exception("File type is not HDF")
	
	if verbose is not None:
		print 'The filetype is : ', filetype

	""" open the file
	 default is read-mode"""
	
	#this returns a dictionary of functions for the file type	
	modehdf = openhdf_modes(filename,filetype)
	if read_mode is None:
		read_mode = 'read'
	elif read_mode.lower() not in ['read','write','append']:
		raise Exception("Read mode error.  Must be 'read','write',or 'append'")

	if verbose is not None:
		print 'Opening in ', read_mode, 'mode'

	file    = modehdf[read_mode.lower()](filename)
	file.filetype = filetype

	return file