# This is from left  we only send positional only arguments
# parameter "c" can be both while parameter "d" has to be keyword argument
def another_strange_function(a, b, /, c, *, d):
    print(f'a={a}; b={b}; c={c}; d={d}')

# This works fine 
another_strange_function("a", "b", c="c", d ="d")

# This works fine since the "c" parameter can be either positional or keywords arguments
another_strange_function("a", "b", "c", d ="d")

# It will not work since "a" parameter has to be positional argument
another_strange_function(a="a", "b", "c", d ="d")

# same issue since "b" parameter has to be positional argument
another_strange_function("a", b="b", "c", d ="d")

# It will not work since "d" parameter has to be keyword argument
another_strange_function("a", "b", "c", "d")
