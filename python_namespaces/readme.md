## What is a namespace in python?
It is a system that ensures that names in a program are unique and can be used without any conflict. 
Everything in python is an object. Python implements namespaces as dictionaries. There is a name to object mapping, where name is key and object is value. 

#### Types of Namespaces:
Build in: These are part of python, and loads when we start python interpreter
Global: These are part of our program. 
Enclosing: When one function encloses another
Local: Namespace within a function or code level/block you are working in

#### Querying each namespaces
dir(__built-in__) Will return built-in namespaces
globals() will return global namespace in a program
locals() will return local namespaces in the scope

Scope helps python to return correct names when referenced in a code. 
A name has a meaning within specific scope
That means what gets returned depends on scope within which i reference a name
Python will search a specific hierarchy to find a name
Python begins with searching locally, and if not found
1. It looks at enclosing functions
2. It looks globally
3. it looks at built-ins, if still not found.
4. It returns a NameError exception
