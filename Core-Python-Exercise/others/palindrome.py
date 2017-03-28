'''
Created on Nov 10, 2016 3:16:02 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: context_managers.palindrome

'''
import re
from idlelib.ReplaceDialog import replace

my_list = ["Stats", "Amore", "Roma", "No 'x' in Nixon", "Was it a cat I saw?"]

my_list = ["".join(re.findall("[a-zA-Z]+", wd.lower())) for wd in my_list]
reversed_list = [wd[::-1] for wd in my_list]

print(my_list)
print(reversed_list)

def my_filter(list1, list2):
    for w in list1:
        if w in list2:
            yield w
            
            
# r = (w for w in my_list )
    

result = my_filter(my_list, reversed_list)

print(list(result))


# result = list(filter(my_filter(list1, list2), (my_list, reversed_list))
