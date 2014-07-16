
#!/usr/bin/python
import sys, getopt
from test_hdf_type import test_hdf_type
from openhdf_modes import openhdf_modes 

# This is a function to open any hdf file and return a file object
def openhdf(filename, verbose=None, read_mode=None, hdf4type=None):
	
	file = None

	# if no filename is provided ask at command line
	if filename is None:
		filename = input("Enter filename: ")

	if verbose is not None:
		print filename

	# figure out the flavor of the hdf file
	# HDF4 or 5 (supports 5-EOS as well)

	filetype = test_hdf_type(filename)

	if verbose is not None:
		print 'The filetype is : ', filetype

	# open the file
	# default is read-mode
	
	
	modehdf = openhdf_modes(filename,filetype, hdf4type)
	if modehdf is not None:
		if read_mode is None:
			read_mode = 'read'

		if verbose is not None:
			print 'Opening in ', read_mode, 'mode'

		file    = modehdf[read_mode.lower()](filename)
		file.filetype = filetype

	else:
		print 'Error openhdf: No way to open this file'
		print 'Options are:'
		print 'HDF5'
		print 'HDF4 hdf4type = SD'
		print 'HDF4 hdf4type = VD'

	return file


#Parse arguments provided at the command line
#usage openhdf.py -v -r (w,a) -f <filename> -hdf4 <type>
def main(argv):

	filename  = None
	read_mode = None
	hdf4type  = None
	verbose   = None

	try:
		opts, args = getopt.getopt(argv,"vrwaf:",["hdf4="])
	except getopt.GetoptError :
		print 'openhdf.py -v -r(w,a) -f <inputfile> --hdf4 <type>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'openhdf.py -v -r(w,a) -f <inputfile> --hdf4 <type>'
			sys.exit()
		elif opt in ("-f"):
			filename = arg
		elif opt in ("-r"):
			read_mode = 'read'
		elif opt in ("-w"):
			read_mode = "write"
		elif opt in ("-a"):
			read_mode = "append"
		elif opt in ("--hdf4"):
			hdf4type = arg
		elif opt in ("-v"):
			verbose = True

	return filename, verbose, read_mode, hdf4type

if __name__ == "__main__":

	# if running from command line and no arguments given, ask for inputs
	if len(sys.argv) == 1:
		filename = raw_input("Enter filename: ")
		if not filename:
			print 'filename is required, exiting'
			exit(0)

		read_mode = raw_input("Enter mode to read file (default is read): ")
		if not read_mode:
			read_mode = 'read'

		hdf4type = raw_input("Enter hdf4data type (default is None): ")
		if not hdf4type:
			hdf4type = None

		verbose = raw_input("Run verbose (default is No): ")
		if not verbose:
			verbose = None
	else:
		filename, verbose, read_mode, hdf4type = main(sys.argv[1:])

	openhdf(filename=filename, verbose=verbose, read_mode=read_mode, hdf4type=hdf4type)
				



