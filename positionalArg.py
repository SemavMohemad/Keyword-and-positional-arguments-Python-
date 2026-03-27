# First let's see this
def print_members(member1, member2, member3):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")


print_members("Frank", "Dean", "Sammy")
print_members(member1="Frank", member2="Dean", member3="Sammy")


# it will give you the same result because we don't specify what the parameters should be.
# ----------------------------------------------------------------------------------------------
# If we want the function only accept Positional Arguments :
def print_three_members(member1, member2, member3, /):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")


print_three_members("Frank", "Dean", "Sammy")
# It works fine since all the arguments for the defined parameters are passed as
# positional
# ----------------------------------------------------------------------------------------------
print_three_members("Frank", "Sammy")
# see here we should give it the same numbers of parameters
# see error below

"""
    print_three_members("Frank", "Sammy")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
TypeError: print_three_members() missing 1 required positional argument: 'member3'
"""
# ----------------------------------------------------------------------------------------------
print_three_members("Frank", "Dean", "Sammy", "Bob")
# if you pass more than the number of formal arguments
# see error below
"""
    print_three_members("Frank", "Dean", "Sammy", "Bob")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: print_three_members() takes 3 positional arguments but 4 were given
"""
# ----------------------------------------------------------------------------------------------
print_three_members(member1="Frank", member2="Sammy", member3="Dean")
# It will not work since I have passed the parameters "member1" as keyword with argument "Frank"
# see error below
"""
TypeError: print_three_members() got some positional-only arguments passed as keyword arguments: 'member1, member2, member3'
"""
# ----------------------------------------------------------------------------------------------
print_three_members("Frank", "Dean", member3="Sammy")
# It will not work as mentioned above see error #
"""
TypeError: print_three_members() got some positional-only arguments passed as keyword arguments: 'member3'
"""
