#File with I/O

#'r' open for reading (default) 
#'w' open for writing, truncating the file first 
#'x' open for exclusive creation, failing if the file already exists 
#'a' open for writing, appending to the end of the file if it exists 
#'b' binary mode 
#'t' text mode (default) 
#'+' open a disk file for updating (reading and writing) 
#'U' universal newlines mode (deprecated) 

import os,sys
import array
import functools

if not os.path.exists('somedir'):
	os.mkdir("somedir")

#重定向
with open('somedir/spamspam.txt', 'w+') as f:
    print('This will be written to somedir/spamspam.txt\nhave fun', file=f) 

with open('somedir/spamspam.txt', 'rt') as f:
	for line in f:
		print(line)

#二进制读
with open('somedir/spamspam.txt', 'rb') as f:
	for line in f:
		print(line)

#二进制写和读操作
with open('somedir/spamspam.bin', 'wb') as f:
	text = "hello world"
	f.write(text.encode('utf-32'))

with open('somedir/spamspam.bin', 'rb') as f:
	temp = f.read().decode('utf-32')
	with open('somedir/spamspam8.bin', 'wb') as f:
		f.write(temp.encode('utf-8'))

with open('somedir/spamspam.bin', 'wb+') as f:
	print(f.read().decode('utf-32'))

nums= array.array("i",[1,2,3,4])
with open('data.bin','wb') as f:
	f.write(nums)

RECORD_SIZE = 5
with open('somedir/spamspam.bin', 'rb') as f:
	records = iter(functools.partial(f.read, RECORD_SIZE),b'')
	with open('somedir/newfile.bin','wb') as f1:
		for x in records:
			f1.write(x)
		

#with自动关闭文件