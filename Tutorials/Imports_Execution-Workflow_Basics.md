# Anaconda
## Simp,e Python Execution Workflows
### Execution Workflow 1
#### Tools: command line, python interpreter 
#### Code: no files, all in live interpreter

1. start interpreter
	* `python`
2. write code in interpreter
	* `def myFunc(x):
			return x^2:`

#### Usage:	python interpreter	 	
1. call functions from same interpreter session only
	* `myFunction()`

#### Pros:								
1. check simple code (one liners), often w/ toy data 
2. check your intuitions about data manipulation
	1. ex: what does `myString[:-1]` give me when `myString = 'Hello'`?

#### Cons:								
1. not reusable or saved
2. no editor
3. inefficient when writing more than a few lines of code

### Execution Workflow 2
#### Tools: command line, python interpreter, text editor: 
#### Code: 1 module (file)
* Instead of writing our functions in the temporary memory of the interpreter, we can write them in a .py file somewhere

#### Usage: python interpreter				
1. move to into myfile.py file dir
	* `$ cd`
2. start interpreter
	* `$ python`
3. load module into current terminal session
	* `>>> import myfile`
4. call function from module
	* `>>> myfile.myFunction()`


#### Pros:					
1. Using the python interpreter to call functions can be useful if you are working with functions that output something, and you want to have a simple interactive environment to try various inputs and see their outputs, e.g. search engines, chatbots, question asking systems, etc.
2. interactive way to import various modules or packages and play with them live in the interpreter.

#### Cons:					
1. usage commands are not saved, often we want to save the function calls somewhere

### Execution Workflow 3
#### Tools: terminal + editor: 
#### Code: 1 file: function, followed by function call in .py script
#### Usage: 				
1. move to into myfile.py file dir
	* `$ cd`
2. Run file from command line
	* `$ python myfile.py`

#### Pros:					
1. will both load your function and execute it (will execute everything in the .py synchronously)

#### Cons:
1. not resuable, except in this exact use case, 
2. bad coding practice
	* This is because the function is tied to the function call, they should be separate, in different files.
	* Also, from a git perspective, you should not need to edit the file that contains the function if all you are doing is changing how you are calling the function i.e. what arguments you pass it in some specific instance

### Execution Workflow 4
#### terminal + editor  
#### Code: 2 files:			
1. 1 file with functions only
2. 1 file as a 'script' file to do imports and call functions 
			* a script file is a file containing mostly commands like you would enter in the command line or in an interpreter. it allows you to chain dependencies and function calls together in a modular and resuable fashion, keeping your functions separate.

#### Usage: 				
1. move to into myfile.py file dir
	* `$ cd`
2. Run file from command line
	* `$ python myfile.py`

#### Pros:					
1. Modular, Resuable 
2. often we want to call more than one command or function in some specific order
3. DRY - Don't Repeat Yourself 

#### Cons:					
	* little bit more organization upfront












							   python -> import -> call function from python interpreter



			terminal 1 file -> python filename.py

			terminal -> python -> call function





tools:
	Python Notebook
	spyder
	terminal
	qt console




Coding:
	python packages vs libraries







