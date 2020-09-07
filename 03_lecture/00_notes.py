# Encapsulation -- hiding the implementation details of an object

# Abstraction -- dealing with the level of detail that is most appropriate to a task

# Inheritance -- inheritance allows our object classes to inherit attributes and methods from other classes in the program.

# Polymorphism -- the ability to treat a class differently depending on which subclass is implemented


# -----------------  A Starting Point  ------------
# A good starting point is to describe your problem in detailed sentences. 
# Once you have some text that describes your general problem, you then go through and find all of the nouns in the text. 
# The nouns then become the classes in your program. Any verbs associated with a noun become methods on the class. 
# Any adjectives associated with the noun become the attributes on the class.



# --------------------    LEGB (Local, Enclosing, Global, Builtin) rule   -------------
# Local scope ---- will always be searched first and includes any variables assigned within a function.
# Enclosing -- Python starts by looking in Local, and then searches the Enclosing scope.
# Global -- A variable declared at the global level is not enclosed inside any function.
# Builtin -- If a variable is not found in Local, Enclosing, or Global scope, then the builtin variables are searched.


#                   global Keyword
# We can declare a global variable in a function by using the global keyword.
def my_func():
    global x 
    x = 100
my_func()
print(x)
