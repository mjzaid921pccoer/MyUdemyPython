"""
Build in objects have variety of methods
In jyputer notebook ex Listvar. press[Tab]
to explore variety of methods available
Shift+Tab:to know more about specific method
or
help(mylist.insert)
or
phython documentation on website
"""
#LIST
mylist=[]
#adding elements in list
mylist.append(1)
#remove elements from end of list i.e index=-1
print(mylist.pop())

"""
Function
"""
#syntax parameter with value is default parameter
def name_of_fun(parameter='User'):
	"""DOCSTRING explains function"""
	print("hello ",parameter.upper(),' Welcome')
name=input('Enter your name:')
name_of_fun(name)


























