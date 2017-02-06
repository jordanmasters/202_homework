# Anaconda


## Python File Execution Workflows


		1. terminal + python interpreter
			1. Write: 				
				* No files
				1. 'python' to start interpreter
				2. write code in interpreter
			2. Usage:			 	
				1. call functions from same interpreter session only
						   
			3. Pros:								
				1. check simple or internet code 
				2. check your intuitions about data manipulation
					* ex: what does myString[:-1] give me if myString = 'Hello'?
			4. Cons:								
				1. not resuable or saved
				2. no editor
				3. inefficient when writing more than a few lines of code

		2. terminal + editor  -> Write:				1 file: function() in myfile.py file
						   -> Usage: 				1) 'cd' into myfile.py file dir
						   							2) 'python' to start interpreter
						   							3) 'import myfile' to load module
						   							4) call function from module
						   -> Pros:					a) Using the python interpreter to call functions can be useful if you are working with functions that output something, and you want to have a simple interactive environment to try various inputs and see their outputs, e.g. search engines, chatbots, question asking systems, etc.
						   							b) interactive way to import various modules or packages and play with them live in the interpreter.
						   -> Cons:					a) usage commands are not saved, often we want to save the function calls somewhere

		3. terminal + editor  -> Write:				1 file: function, followed by function call in .py script
						   -> Usage: 				1) 'cd' into myfile.py file dir
						   							2) 'python myfile.py' to run file 
						   -> Pros:					a) will both load your function and execute it (will execute everything in the .py synchronously)
						   -> Cons:					a) not resuable, except in this exact use case, bad coding practice
						   								1) This is because the function is tied to the function call, they should be separate, in different files.
						   								2) Also, from a git perspective, you should not need to edit the file that contains the function if all you are doing is changing how you are calling the function i.e. what arguments you pass it in some specific instance


		4. terminal + editor  
		-> Write:				2 files:
																a) file with functions only
																b) 'script' file to do imports and call functions 
																	- a script file is a file containing mostly commands like you would enter in the command line or in an interpreter. it allows you to chain dependencies and function calls together in a modular and resuable fashion, keeping your functions separate.
						   -> Usage: 				1) 'cd' into .py file dir
						   							2) 'python scriptFile.py' to run file
						   -> Pros:					a) Modular, Resuable 
						   							b) often we want to call more than one command or function in some specific order
						   							c) DRY - Don't Repeat Yourself 
						   -> Cons:					a) little bit more organization upfront












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







