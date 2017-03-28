'''
Created on Nov 15, 2016 11:45:04 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: decorators.function_inside_function

'''
def outer_function():
    print ("1. outer_function(): This is outer function!")
    def inner_function():
        print ("2. inner_function(): This is inner function, inside outer function!")
    print ("3. This is outside inner function, inside outer function!")
    return inner_function()

assign_me_as_object = outer_function()

