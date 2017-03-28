f = open('text.txt', 'r')
print (f.name)
print(f.mode)
f.close()
# this contact manager automatically care about closing the file 
with open('text.txt', 'r') as f:
	#f_contents = f.read() #for small file
	#print(f_contents)
	# f_contents = f.readlines()
	# for line in f_contents:
	# 	print(line, end='')
	# print(f_contents)

	#this is iterate line by line from file and prevent momery issue
	# for line in f:
	# 	print(line, end='')

	#size
	# f_contents = f.read(100)
	# print(f_contents, end='')
	#iterate for large size
	size_to_read = 10 #100 characters
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents, end='*')
		f_contents = f.read(size_to_read)

	f.seek(0) # set position to begaining to file

with open('text2.txt', 'w') as f:
print(f.closed)

#working to binary file or picture file

with open('abc.jpg', 'rb') as rf:
	with open('abc_copy.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)


# chunk size way

with open('abc.jpg', 'rb') as rf:
	with open('abc_copy.jpg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.writ(rf_chunk)
			rf_chunk = rf.read(chunk_size)

