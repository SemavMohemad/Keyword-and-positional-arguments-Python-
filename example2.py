# First Example
def strange_function(*, x, y):
    print(f"x={x}; y={y}")


# This is keyword arguments function parameters; the argument sent are "one" and "two"
strange_function(x="one", y="two")


# while the below will not work; see error after function call
strange_function("one", "two")
"""
TypeError: strange_function() takes 0 positional arguments but 2 were given
"""
#----------------------------------------------------------------------------------------------------

# Second Example
# function definition to accept only keyword arguments
def print_three_members(*, member1, member2, member3):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")

# works fine
print_three_members(member1="Frank", member2="Dean", member3="Sammy")

#works fine
#and here we don't care about the order just give it the right key any where.
print_three_members(member1="Frank", member3="Dean", member2="Sammy")

# It will not work; we can not pass positional arguments; see error below 
print_three_members("Frank", "Dean", "Sammy")
'''
TypeError: print_three_members() takes 0 positional arguments but 3 were given
'''

#It will not work for the same reason as above
print_three_members(member1="Frank", member2="Dean", "Sammy")

# It will not work for the same reason 
print_three_members(member1="Frank", "Dean", member3="Sammy")

#----------------------------------------------------------------------------------------------------
#Note
# Bare asterisk can not be added at the end since after "*" (asterisk), 
# it expect keyword argument
def print_three_members(member1, member2, *):
    print(member1)
    print(member2)


# It will not work see error below 
print_three_members("member1","member2")
'''
SyntaxError: named arguments must follow bare *
'''

# when we have doubts about the number of arguments we should pass in a function we use :
# **kwargs (To define multi keyword arguments)
def fun2(**kwargs):
    for k, val in kwargs.items():
        print(k, val)
fun2(a=1, b=2, c=3)
