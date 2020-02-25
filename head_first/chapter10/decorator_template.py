from functools import wraps

def decoractor_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute before calling the decorated function
        
        # 2. Call the decorated function as required, returning its results if needed
            return func(*args, **kwargs)
    
        # 3. Code to call instead of calling the decorated function
    return wrapper
