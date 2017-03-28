def decorator_fxn(original_fxn):
    def wrapper_fxn(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_fxn.__name__))
        return original_fxn(*args, **kwargs)
    return wrapper_fxn

@decorator_fxn
def display(name, age):
    print('display fxn ran {}, {}'.format(name,age))

# display = decorator_fxn(display)
display("adsf", "asd")