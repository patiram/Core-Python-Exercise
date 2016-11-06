'''
Created on Oct 28, 2016 1:35:52 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: singleton_design_pattern.singleton_private_inner_class

'''
"""
This is the example for singleton design pattern using private inner class
"""

class OuterPublic:
    class __InnerPrivate:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OuterPublic.instance:
            OuterPublic.instance = OuterPublic.__InnerPrivate(arg)
        else:
            OuterPublic.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OuterPublic('meat')
print(x)
y = OuterPublic('eggs')
print(y)
z = OuterPublic('abc')
print(z)
print(x)
print(y)
print('x')
print('y')
print('z')