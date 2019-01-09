'''
Example code to run through the functions
Created by Lynton Brown 01/09/2019
'''

import chmodValues as ch ##Import module
import os

print("%s version: %s"%(ch.__name__, ch.__version__)) ##Display Version Number

fileToCheck=ch.Check(os.getcwd()) ##Hold permission data in variable
print("\'%s\' permission value: %s"%(os.getcwd(),fileToCheck)) ##Display permission data

print(ch.Help()) ##Display permission stucture

ch.ManualEntry() ##Manually enter file path
ch.ManualEntry(True) ##Manually enter file path and display permission stucture
