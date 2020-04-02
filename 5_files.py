"""In Jypiter Notebook
%%writefile myfile.txt
hello this is content of my file

To open file in read write append and close 
"""

"""METHOD 1"""

myfile=open('NewTextFile.txt',mode='r')
print(myfile.read())
myfile.close()
"""It is important to close open file to execute error free problems. 
here in method one To read file content we opened file in Read mode.
And once file is read cursor is at end of file content 
Note:- If we want to read file more than one time before closing it then we need to seek cursor at 0 to read content from start of file
"""
myfile=open('NewTextFile.txt',mode='r')
print(myfile.read())
myfile.seek(0)
ContentasList=myfile.readlines()
print(ContentasList)
myfile.close()

"""
.readlines convert every content of line in file as list objects
"""
myfile=open('NewTextFile.txt',mode='w')
myfile.write('This content are being written as mode is w and this content of file is going to be override / this file is going to be created if this file does not exist')
myfile.close()

myfile=open('NewTextFile.txt',mode='a')
myfile.write('\n \n This content are being appended by mode a')
myfile.close()

"""METHOD 2 """

with open('NewTextFile.txt',mode='r') as myfile:
	print(myfile.read())
with open('NewTextFile.txt',mode='w') as myfile:
	myfile.write('Content are being override/created')

"""Note:- Method 2 is commonly followed because we need not always write close() to close file with open do it for us """
