def func(*args):
    print(args)

# You can see I can send multi positional argument as per function argument definition above
func("arg1","arg2","arg3","arg4")
'''
It prints our a tuple so the  as below
('arg1', 'arg2', 'arg3', 'arg4')
'''
#----------------------------------------------------------------------------------------------------
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Total: {total}")
add_numbers(10, 20, 30)

# Let us experiment with *args by putting in with other parameters as below
def print_varying_members(member1, member2, *args, member3):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")
    print(f"*args contains {args}")

# Let us call the function above
print_varying_members("Frank", member2="Dean", member3="Sammy")
'''
member1 is Frank
member2 is Dean
member3 is Sammy
*args contains ()  --> args tuple is empty because you didn’t pass any additional arguments beyond the defined parameters.
'''
# Let me call by using "member2" parameter as positional argument
print_varying_members("Frank", "Dean", member3="Sammy")
'''
--> You see same result nothing changed
member1 is Frank
member2 is Dean
member3 is Sammy
*args contains ()  --> args tuple is empty because you didn’t pass any additional arguments beyond the defined parameters.
'''

# Let us add additional parameter
print_varying_members("Frank", "Dean", "arg2", "arg3", member3="Sammy")
'''
member1 is Frank
member2 is Dean
member3 is Sammy
*args contains ('arg2', 'arg3') --> you see the args tuple is now note empty since you passed additional positional arguments
'''

# Let us make the last arguments as positional argument call
print_varying_members("Frank", "Dean", "Sammy") # Argument missing for parameter "member3"
'''
You can see that it assume the first parameter and the second as positional arguments until it
reach the last argument "Sammy" which it will be taken by the multi positional argument definition (*args)
and after that it find out the the parameter "member3" is missing
'''
# same issue as above since since "Sammy" will be taken into the "*args" or the multi positional argument parameter definition
print_varying_members("Frank", member2="Dean", "Sammy") # Argument missing for parameter "member3"
'''
"Sammy" argument as positional is taken by the "*args"
'''


# Let us try this
print_varying_members(member1="Frank", "Dean", member3="Sammy") # Argument missing for parameter "member2"
'''
"Dean" argument as positional is taken by the "*args"
'''


