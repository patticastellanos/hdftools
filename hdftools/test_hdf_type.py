
# This is a simple function to return the type of HDF file that is passed to it
def test_hdf_type(filename):

	
	import pyhdf.HDF as HDF4
	import tables as HDF5

	#check to see if file is an hdf4 file
	#returns 1 if HDF4 file
	#returns 0 if not an HDF4 file
	hdf4flag = HDF4.ishdf(filename)

	if hdf4flag == 1:
		filetype = 'HDF4'

	
	#check to see if file is hdf5 (also support hdf5-eos)
	# returns >0 if True
	# returns 0 if False
	hdf5flag = HDF5.isHDF5File(filename)
	if hdf5flag > 0:
		filetype = 'HDF5'

	return filetype