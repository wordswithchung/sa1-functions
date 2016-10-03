# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_cost(state_abbreviation, cost_amount, tax=0.05):
    """Calculates costs of items with tax

    Input needed: state abbreviation for location purchased; 
    tax rate is state-dependent. If "CA", tax rate is 7%.
    If not "CA", tax rate defaults to 5% (unless otherwise specified).
    The cost of the amount also needed.
    Total cost returned (cost + [cost x tax])
    """
    if state_abbreviation == "CA":
        return cost_amount + (cost_amount * 0.07)
    else:
        return cost_amount + (cost_amount * tax)

print calculate_cost("CA", 50)
print calculate_cost("TX", 150, 0.03)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """Determine whether fruit string is "strawberry", "cherry", or "blackberry"

    Input: fruit name as a string
    Output: if fruit name is not "strawberry", "cherry", or "blackberry", then
    return False. Else, return True.
    """

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False

print is_berry("apple")
print is_berry("cherry")

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    """Determine shipping cost based on truthiness of is_berry(fruit)
    """
    if is_berry(fruit) == True:
        return 0
    if is_berry(fruit) == False:
        return 5

print shipping_cost(is_berry("apple"))
print shipping_cost("cherry")

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """Determine truthiness of hometown (if it's San Jose)."""
    if town_name == "San Jose":
        return True
    else:
        return False

print is_hometown("New York")
print is_hometown("San Jose")

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """Return concatenation of strings"""
    return first_name + " " + last_name

print full_name("Chung", "Nguyen")
print full_name("Balloonicorn", "Jones")
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town_name, first_name, last_name):
    """Provide greeting based on if someone's also from San Jose."""
    if is_hometown(town_name) == True:
        print "Hi, {}, we're from the same place!".format(
                full_name(first_name, last_name))
    else:
        print "Hi {}, where are you from?".format(full_name(first_name,
            last_name))

print hometown_greeting("San Jose", "Barbara", "Walters")
print hometown_greeting("San Diego", "Barbra", "Streissand")


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x=1):
    """Outer and inner functions; inner function returns x + y

    Input: integer (x), which defaults to 1 if not provided
    Output: presumably sum of x and y
    NOTE: The instructions for this particular task is very confusing, as
    a value for y is necessary to call the function.
    """
    def add(y):
        return x + y

    return add(5)
    
print increment(4)
print increment()


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
"""Honestly, I do not understand what this particular question is asking for, 
but I'm going to go ahead and provide my best guess below!
"""

def increment(x=1):
    def add(y):
        return x + y
    return add(5)

def increment(x=1):
    def add(y):
        return x + y
    return add(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_number(number, list_of_numbers):
    """Take number provided and append the number to list of numbers."""
    list_of_numbers.append(number)
    return list_of_numbers

print append_number(1, [3, 2903, 183])


#####################################################################