#!/usr/bin/python
import pyhdf.SD, pyhdf.VS
import tables

# This is a program to define a variable list class 
# and return it with information from the given file

class fieldlist:
	"""A class that contains information about the fields in
		in an HDF file"""

	def __init__(self, file):

		#Depending on the type of file there are different ways
		# to fill the lists
		if type(file) is pyhdf.SD.SD:
			fieldnames = file.datasets().keys()

			path      = ['/']*file.datasets().__len__()

			dims = []
			for field in fieldnames:
				data = file.select(field)

				dims.append(data.dimensions().values())



				



	#fieldnames
	#path
	#datatype
	#dims
	


