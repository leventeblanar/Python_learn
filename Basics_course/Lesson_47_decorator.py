# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an athument to the decorator

#             @add_sprinkles 
#             get_ice_cream("vanilla")

# def add_sprinkles(func):          This is a decorator
#     def wrapper():
#         func()
#     return wrapper


def add_sprinkles(func):          # This is a decorator
    def wrapper(*args, **kwargs):
        print("*You add sprinkles*")
        func(*args, **kwargs)
    return wrapper                # the wrapper is needed as without it the print method would run without the function being called

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):   # base function
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla") 