'''

@author: patir
'''
import subprocess,os

os.system('ls')
subprocess.call(['ls', '-1'], shell=True)
