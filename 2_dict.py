"""
Dictionary {'key':'value'} separated by commas
Unordered mapping key-value pair
object i.e value rettrieved by keyname
"""

priceDict={'apple':100,'milk':60,'bread':35,'tea':20,'mess':200}

"""Nested Dict"""
paymentDict={'electricity':3000,'rent':8000,'fees':{'Examfee':1000,'AdmissionFee':1500,'UniversityFee':3000,'TuitionFee':50000},'grocery':priceDict}

print()

print(type(priceDict),priceDict)

print()
print(paymentDict)

print()
print(priceDict['mess'])

"""Update value of key"""
priceDict['mess']=250
print()
print(priceDict)

"""Adding more KeyValue pair to Dict"""
priceDict['snacks']=150
priceDict['name']='ABCD'

print()
print(priceDict)

"""set of all keys in Dictionary"""
print()
print(priceDict.keys())
print(priceDict.values())
print(priceDict.items())

print()
print(paymentDict.keys())
print(paymentDict.values())
print(paymentDict.items())

"""Access Data"""
print()
print(paymentDict['grocery']['mess'])
print()
print(priceDict['name'].lower())
