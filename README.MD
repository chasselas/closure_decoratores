#Python
-everthing in python is object
-function in python in first class function(you can pass function as a parameter)

# Closure
- access to variables, functions, classes from different(outer, actual retrieved) scope
- variables are storted in functions objects
## Creation

1. Need to have min 2 function, one outer and oun inner
2 Outer function should return declaration of inner function
3. Inner function have to use something from outer function (variable, other function, class) and only this wille be recorded


## Use case:
-persistence(trwalosc)

## Cons
- if you not understand you can leak memory

## Main rules:

-DRY - don' t repeat yourself'
- KISS - kepp it simple, stupid

## Decorator
- add additional functionality to function (augmented function)
- 3 types of decorators
    1. function decorato
        - need to use closure for creating
    2. class decorator
    3. decorator as desing pattern
        -different from python decorator functionality
