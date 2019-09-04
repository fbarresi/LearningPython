def test():
    """
    This function show how you can write a simple python function
    """
    print("Hey Python!")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)



if __name__ == "__main__":
    print(test.__doc__)
    test()

    # functions with *args and **kwargs
    args = ("two", 3, 5) # args is tuple
    print(type(args))
    test_args_kwargs(*args)

    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5} #kwargs is dictionary
    print(type(kwargs))

    test_args_kwargs(**kwargs)