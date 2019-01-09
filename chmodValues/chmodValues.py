'''
Function to determin the file permissions for a given file. Useful
when modifying locked files as a tool to ensure the file has the
same premissions after a filechange as it did before the file change
Created By Lynton Brown 01/09/2019
'''

from os import stat as _stat
from os.path import isfile as _isfile
from os.path import isdir as _isdir

__version__="1.0"

def Check(FilePath):
    """Check(FilPath)
    Check the permission of file and return value
    """
    if(_isfile(FilePath) or _isdir(FilePath)):
        chmodValue=((oct(_stat(FilePath).st_mode &0O777))[-3:])
        return(int(chmodValue))
    else:
        chmodValue="File Not Found"
        return(chmodValue)

def Help():
    """call this function with print to review value deffinitions
    """
    valueMeanings=[
        'First Number = User',
        'Second Number = Group',
        'Third Number = Other',
        '0 = No Permission',
        '1 = Execute Only',
        '2 = Write Only',
        '3 = Write and Execute',
        '4 = Read Only',
        '5 = Read and Execute',
        '6 = Read and Write',
        '7 = Read, Write and Execute']
    return('\n'.join(valueMeanings))

def ManualEntry(displayHelp=False):
    """Call This Function to Prompt User for input
    displayHelp=True will display chmod value deffinitions
    """
    print(Check(input('Enter file path: \n\t'))) ##Manual Check Debug
    if displayHelp:
        print(Help()) ##Debug
    return
