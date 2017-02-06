# Anaconda
## Simp,e Python Execution Workflows
### Execution Workflow 1
#### Tools: command line, python interpreter 
#### Code: no files, all in live interpreter
1. start interpreter
	* `python`
2. write code in interpreter
	1. `def myFunc():`
#### Usage:			 	
1. call functions from same interpreter session only
	`myFunction()`
#### Pros:								
1. check simple or internet code 
2. check your intuitions about data manipulation
	1. ex: what does myString[:-1] give me if myString = 'Hello'?
#### Cons:								
1. not resuable or saved
2. no editor
3. inefficient when writing more than a few lines of code

### Execution Workflow 2
#### Tools: command line, python interpreter, text editor: 
###### Req: 1 file w/ functions in myfile.py file
1. Code:			
	* Req: 1 file w/ only functions in myfile.py file
2. Usage: 					
	1. 'cd' into myfile.py file dir
	2. 'python' to start interpreter
	3. 'import myfile' to load module
	4. call function from module
3. Pros:					
	1. Using the python interpreter to call functions can be useful if you are working with functions that output something, and you want to have a simple interactive environment to try various inputs and see their outputs, e.g. search engines, chatbots, question asking systems, etc.
	2. interactive way to import various modules or packages and play with them live in the interpreter.
4. Cons:					
	1. usage commands are not saved, often we want to save the function calls somewhere

### Execution Workflow 3
###$ terminal + editor: 1 file: function, followed by function call in .py script
1. Code:				
2. Usage: 				
	1. 'cd' into myfile.py file dir
	2. 'python myfile.py' to run file 
3. Pros:					
	1. will both load your function and execute it (will execute everything in the .py synchronously)
4. Cons:					a
	1. not resuable, except in this exact use case, 
	2. bad coding practice
		* This is because the function is tied to the function call, they should be separate, in different files.
		* Also, from a git perspective, you should not need to edit the file that contains the function if all you are doing is changing how you are calling the function i.e. what arguments you pass it in some specific instance

### Execution Workflow 4
#### terminal + editor  
1. Code:	
	* 2 files:			
		 * file with functions only
		 * 'script' file to do imports and call functions 
			* a script file is a file containing mostly commands like you would enter in the command line or in an interpreter. it allows you to chain dependencies and function calls together in a modular and resuable fashion, keeping your functions separate.
2. Usage: 				
	1. 'cd' into .py file dir
	2. 'python scriptFile.py' to run file
3. Pros:					
	* Modular, Resuable 
	* often we want to call more than one command or function in some specific order
	* DRY - Don't Repeat Yourself 
4. Cons:					
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







