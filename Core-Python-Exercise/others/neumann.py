'''
Created on Nov 10, 2016 3:52:49 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: context_managers.neumann

'''

result = list()
def random_number(num):
        m1 = int((pow(num, 2) % 1000000) / 100)
        return m1
n = int(input("Enter 4 digit numbers:"))
val = int(input("Enter how much random numbers want to generate:"))
for i in range(val):
    r = random_number(n)
    n = r
    result.append(r)
for r in result:
    print('{0:04}'.format(r))
    

    
    
        
