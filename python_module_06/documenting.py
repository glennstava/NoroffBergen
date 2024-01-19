import ping3
import platform

class Cars:
    # Sets the docstrings property of the class
    __doc__ = "This is an overview of what MyClass does."

    def Car_function():
        # A one-line docstring for this method
        '''This is an overview of what my_class_function does'''
        print("Called MyClass function")
        
    def my_function():
        print("Called function")

    def my_other_method():
        """This is a mult-line
        descriptive docstring."""
        print("Called my_other_method.")

    # Sets the docstrings property of the function.
#    my_function.__doc__ = "This is an overview of what MyFunction does."

# help(Cars)
help(ping3)