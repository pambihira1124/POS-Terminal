#!/usr/bin/python
import os
import re

# Get a list of files in the directory.
files=os.listdir('./')

# Loop through each of the files.
for myfile in files:
	
	# Look for a file name with a specific pattern.
	match=re.match("bus\d{1,}\.txt",myfile)

	# Perform the operation if a match is found
	if match:
		print "Processing: "+myfile+"\n"
		f=open(myfile,"r")
		for x in f:

			# Open the appropriate file.
			a=x.split(" ")
			wfn=a[0]+"_report.txt"
			wf=open(wfn,"a")

			# Write the data to the file.
			wf.write(x)
			wf.close()

		f.close()

# End of Python program.

