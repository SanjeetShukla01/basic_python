Python does not have private variable. 
The intention of name mangling is to prevent accidental manipulation/reuse of any variable.
__x => mangled
__x__ => Not mangled
__ => not mangled


Mangling happens at compile time, so just by moving where the function is defined can change the behaviour 
https://www.youtube.com/watch?v=0hrEaA3N3lk

Dynamic fearures become hazy becuase of name mangling in pyton
In order to stay safe, we should use features of static languages. And should try to impose those features in python too. 

Compile Explore: