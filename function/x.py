import os

files = os.popen('ls *.htm*').readlines()


#print files

for i in range(len(files)):
	files[i] = files[i].strip("\n")

for i in files:
	
	os.system("iconv "+i+" -f gb2312 -t utf-8 > "+i+'1')
	os.system("rm -f "+i)
	os.system("mv "+i+'1'+" "+i)
