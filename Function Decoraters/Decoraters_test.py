import functools

##################### DECORATERS #####################
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper



def make_list(func):
    def inner():
        y = func()
        z = y.split()
        print("making list of: "+y)
        return z
    return inner



def trace(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f'TRACE: calling {func.__name__}()'
              f' with {args}, {kwargs}')
        
        original_result = func(*args,**kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result}')
        return original_result
    return wrapper

        
#################### FUNCTIONS #########################


@uppercase
@trace
def greet():
    return 'hello'



@make_list
@trace
def ordinary():
    return "I am Ordinary"
    

################# FUNCTION CALLS ##################

greet()
print('\n')
ordinary()




        

