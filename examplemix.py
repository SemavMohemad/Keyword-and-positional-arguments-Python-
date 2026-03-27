# Define multi positional arguments and after it multi keyword arguments
def func(*args, **kwargs):
    print(args)
    print(kwargs)


func("arg1", "arg2", arg3="Three", arg4="Four")
"""
we can see the output as below 
('arg1', 'arg2')  --> You see the many positional arguments is converted to tuple data type 
{'arg3': 'Three', 'arg4': 'Four'} --> You see the multi keywords arguments is converted to a dictionary data type 
"""


# -----------------------------------------------------
def student_info(*args, **kwargs):
    print("Subjects:", args)  # Positional arguments
    print("Details:", kwargs)  # Keyword arguments


# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")
