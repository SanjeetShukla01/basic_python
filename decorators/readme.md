https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a



Decorator: A decorator is a design pattern in Python that allows a user to add new functionality to an existing 
object without modifying its structure. Decorators are usually called before the definition of a 
function you want to decorate.


Creating a Decorator

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
```

Our decorator function takes a function as an argument, and we shall, therefore, define a function and pass it to 
our decorator. We learned earlier that we could assign a function to a variable. We'll use that trick to call our
decorator function.


```python
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()
```
However, Python provides a much easier way for us to apply decorators. We simply use the @ symbol before the
function we'd like to decorate. Let's show that in practice below.

```python
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
```



Step-1 Assigning Fucntion to a Variable
```python
def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)
```

Step-2 Defining Functions inside another function

```python
def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)

```