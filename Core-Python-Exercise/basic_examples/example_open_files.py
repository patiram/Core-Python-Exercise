'''

@author: patir
'''

filename = input('Enter a file name: ')
try:
    f = open(filename, "r")
except:
    print ('There is no file named', filename)

