"""
This is multiline comment:
List square bracket [] object separated by commas
Ordered Sequence
Support Indexing Slicing
Immutable
Can be Nested
"""

"""syntax and defination"""
TEsem2list=['DAA','WT','SPOS','ESIoT','SMD']
print( 'length of list is:' , len(TEsem2list) )
print(type(TEsem2list),' contains TEsem2list[] are:',TEsem2list)
for val in TEsem2list:
	print(val)

"""Slicing"""
FromIndexToEnd=2
print(TEsem2list[FromIndexToEnd:])
EndBeforeIndex=4
print(TEsem2list[1:EndBeforeIndex])

"""Merging"""
TEsem2list2=['STCL','PBL']
TEsem2list=TEsem2list+TEsem2list2
print(TEsem2list)

"""Adding"""
TEsem2list.append('T&Pactivity')
print(TEsem2list)

"""Removing :PBL from 6 index"""
print(TEsem2list.pop(6))
print(TEsem2list)

"""Sorting"""
TEsem2list.sort()
print(TEsem2list)

"""Reversing"""
TEsem2list.reverse()
print(TEsem2list)

"""Nesting list inside List:T&Pactivity with activities"""
"""Mutable so value can be updated"""
TEsem2list[1]=['aptitude','coding','softskill','interview']
TEsem2list[1].sort()
print(TEsem2list)
