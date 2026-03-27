# Special Way To Pass Values To Functions:

## First let's understand Keyword And Positional Arguments:

In other languages like C or C++ , you must pass arguments in a a specific order ,but in python
when you pass arguments into function it doesn’t guess — it grabs things in the exact order you gave them. No switching. No assumptions. Just straight-up, “first thing goes to first place, second thing to second place,” and so on.

###### 🚀See below example :

```
def define(name, work):
    print(f"Hello my name is {name} and I'm working as {work}")
#Now watch what happens when we use positional arguments:

define("Simav", "Software Developer")  # Run -> Hello my name is Simav and I'm working as Software Developer

# Cool, but let's see another scenario

define("Software Developer", "Simav")  # Run -> Hello my name is Software Developer and I'm working as Simav

```

This leads to incorrect behavior even though the code runs successfully, and your code is now technically working — but not doing what you meant. That’s the gotcha with positional arguments: they rely completely on order. Python doesn’t care what you meant to say — it only cares what you actually typed.
That’s why Python gives us other ways to be more specific (Keyword argument) :

```
def define(name, work):
    print(f"Hello my name is {name} and I'm working as {work}")

define(name="Simav", work="Software Developer")  # Run -> Hello my name is Simav and I'm working as Software Developer

define(work="Software Developer", name="Simav")  # Run -> Hello my name is Simav and I'm working as Software Developer

```

So now we don't care where we write it because each value is explicitly tied to a parameter name.

### 🎯 When should we use positional & keyword arguments?

#### ✨ Use a positional argument when:

1. There are few parameters.
2. The meaning is obvious.
3. The order is natural.

```
pow(4,2) #-> base,exponent
abs(-4) # -> absolute of number
```

#### ✨ Use a keyword argument when:

1. To avoid mistakes
2. Make a code readability
3. There are many arguments

_🔥You can also mixing them but positional must come first._

## 🎯Now let's dive into special case (\*) and (/):

The asterisk (\*) and forward slash (/) define whether you can pass positional or keyword arguments to your functions.

ou use a bare asterisk to define a boundary between arguments that you can pass by either position or keyword from those that you must pass by keyword. You use the slash to define a boundary between those arguments that you must pass by position from those that you can pass by either position or keyword. Here’s a visual that summarizes how to use these symbols:

| Left Side                       | Divider | Right Side                      |
| ------------------------------- | ------- | :------------------------------ |
| Positional or keyword arguments | \*      | Keyword-only arguments          |
| Positional-only arguments       | /       | Positional or keyword arguments |

You can also use both symbols together , we will see in next examples.

## Only Positional Arguments (/):

In Python, any argument that’s not passed by keyword is passed by position. You must pass positional arguments in the same order that you defined their parameters in the function header. You always pass positional arguments before keyword arguments. Several of Python’s built-in functions require that you pass all the arguments by position .
[Examples click here](./positionalArg.py)

**✨Some reasons why we use only positional arguments:**

- One reason is that people rename their function arguments and then all of the function calls which used keywords no longer work properly.[For example click here](./whyusepositional.py)

- For clarity and conciseness: For simple functions with few parameters (like len() or split()), passing arguments by position makes the code clean and easy to read. The function's name often makes the expected argument's meaning obvious, so explicitly naming it with a keyword argument provides minimal extra value.

## Only Keyword Argument (\*) :

Passing your arguments by keyword makes your code more readable and also makes using the function more meaningful to your users. You can pass keyword arguments in any order, but they must come after positional arguments, if applicable.
see this
[Examples](./example2.py)

**✨Why use them?** They make your code more readable and reduce the chances of bugs– especially in functions with optional or many parameters. They’re also essential when working with third-party libraries or APIs where you might not remember the exact order.[see this examples](./whyusekeyword.py)

## Combining positional-only arguments with keyword-only arguments :

you can enforce a mix of positional-only and keyword-only arguments in a function definition by using the special markers / (forward slash) and \* (asterisk) in the function signature.
[see examples](./examples.py)

## 🎯What's means (\*arg) and (\*\*kwg) ?

#### Variable-Length Positional Arguments (\*args) In Python :

Sometimes, you won’t know in advance how many values a function needs to accept. That’s where \*args comes in– it allows you to pass an arbitrary number of positional arguments. They are also known as arbitrary positional arguments.

**✨Why use them?** They’re perfect for functions that need to process lists of inputs, like summing numbers or joining strings, without limiting the function to a fixed number of parameters.[see examples](./manypositional.py)

#### Variable-Length Keyword Arguments (\*\*kwargs) In Python :

Just like \*args collects excess positional arguments, \*\*kwargs collects excess keyword arguments into a dictionary. It is also known as arbitrary keyword arguments.

**✨Why use them?** They give you maximum flexibility. Great for configuration-heavy functions, plugin systems, or passing optional features. You can accept and handle dynamic sets of named inputs cleanly.[see example](./manykeyword.py)

### multi keyword arguments & multi positional arguments

[see example](./examplemix.py)

Some rules for \*arg and \*\*kwargs :

1. when you define a function, \*args must come before \*\*kwargs.

```
✅ Valid:
defexample(a, *args, **kwargs):
print(a, args, kwargs)

❌ Invalid:
defexample(a, **kwargs, *args):
pass
```

2. Also, in function calls, positional arguments must come before keyword arguments.

```
✅ Valid:
example(1,2,3, x=10)

❌ Invalid:
example(a=1,2,3)
```

3. You don’t have to name them args and kwargs .

```
defdemo(*values, **options):
print(values)
print(options)

demo(10,20, debug=True)
```

resources:

[python.plainenglish](https://python.plainenglish.io/understanding-python-function-arguments-positional-keyword-default-ca71a7fa3453)

[RealPaython](https://realpython.com/python-asterisk-and-slash-special-parameters/)

[Builtin Functions](https://docs.python.org/3/library/functions.html)

[The Python Coding Book](https://thepythoncodingbook.com/2022/12/11/positional-only-and-keyword-only-arguments-in-python/)
[tutorialspoint](https://www.tutorialspoint.com/python/python_positional_arguments.htm)

[Usage of only positional arguments](https://stackoverflow.com/questions/58477827/why-use-positional-only-parameters-in-python-3-8)

[PEP 570](https://peps.python.org/pep-0570/#abstract)

[Best resource for keyword argument](https://unstop.com/blog/keyword-arguments-in-python#:~:text=If%20you%20swap%20the%20values,ve%20used%20key=value%20syntax.)

[\*arg & \*\*kwargs](https://mimo.org/glossary/python/args-kwargs)
