def pow(base: float, exponent: int) -> float:
    pass


pow(4.5, 10)
pow(4.5, exponent=10)
pow(exponent=10, base=4.5)


# If the arguments were subsequently renamed:
def pow(base: float, exp: int) -> float:
    """
    CHANGE LOG OR VERSION HISTORY:
    `exponent` renamed to `exp`
    """
    pass


pow(4.5, 10)  # OK
pow(4.5, exponent=10)  # TypeError
pow(exponent=10, base=4.5)  # TypeError


# abs(number, /) it is defined only to take positional arguments

var1: int = abs(value=-234)
"""
Error
Expected 1 more positional argument
"""
# while below works fine
var2: int = abs(-234)

# For this reason should be only positional
