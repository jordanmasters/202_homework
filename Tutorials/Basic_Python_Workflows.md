# Python Basics

## Scrapy - Getting Quotes Data
1) make a new project directory
```shell
mkdir PythonBasics1 && cd $_
```

2) Clone a simple quotes bot repo provided by scrapy
```shell
git clone https://github.com/scrapy/quotesbot.git myScraper
cd myScraper
mkdir scrapedData
```
3) Let's start using Scrapy! Make sure you have it installed
```shell
scrapy
# if it is not a command then do:
pip install scrapy
```
4) Check the spiders we have available
```shell
scrapy list
```
6) Use one of those spider classes to pull and save data as .json or .csv
```shell
scrapy crawl toscrape-css -o scrapedData/quotes.json
```
7) Let's do it again and make 3 csv files we can work with later 
* yes, they will all have the same exact data, but importantly, they will also all have the same data structure
```shell
scrapy crawl toscrape-css -o scrapedData/quotes1.csv
scrapy crawl toscrape-css -o scrapedData/quotes2.csv
scrapy crawl toscrape-css -o scrapedData/quotes3.csv
```
8) move back into PythonBasics1 dir
```shell
cd ..
```

## Simple Python Execution Workflows - Merging CSV files

### Before Python, let's merge these files in the command line

```shell
mkdir mergedData # make a folder where we will soon put our merged data
cat myScraper/scrapedData/*.csv > mergedData/merged0.csv
```
#### Pros
* fast, short code

#### Cons
* not easy to customize
* we had headers in each of the files, and all of headers are now in the merged file

#### Can we get closer?
```shell
tail -n +2 myScraper/scrapedData/*.csv > mergedData/merged0-1.csv
```
#### This is fast but could be limiting if we want to do more with the data, let's try it in python

### Python Workflow 1 - Use interpreter to write and execute code
#### Tools: command line, python interpreter 
#### Code: no files, all in live interpreter



1) start interpreter
```shell
python
```
2) CSV Merge Code: copy paste into interpreter
```python
import os
import csv

def merge_csvs_into_list(directory):
	"""	
	This function assumes all csvs in the directory have the same data structure (number of columns)
	:param directory: the directory with csv files we want to merge
	:returns: return list of lists of combined csv content  
	"""
	merged_csv_list = []
	csv_count = 0
	header = []
	for filename in os.listdir(directory):
		if filename.endswith(".csv"): 
			csv_count += 1
			print 'opening', os.path.join(directory, filename)
			f = open(os.path.join(directory, filename), 'rU')
			# simplify to basic list functions like readlines and split
			csv_f = csv.reader(f)
			csv_list = list(csv_f)
			header = csv_list.pop(0)
			for line in csv_list:
				merged_csv_list.append(line)
		else:
			continue
	print 'merged', csv_count, 'csv files into a python list'
	print 'merged list has', len(merged_csv_list), 'rows'
	return merged_csv_list, header

def write_csv_from_list(new_file_path, cvs_list, header):
	"""	
	:param new_file_path: the directory with csv files
	:param cvs_list: list of lists
	:param header: list of header strings
	:returns: return list of lists of merged csv contnt  
	"""
	with open(new_file_path, "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		cvs_list.insert(0, header)
		writer.writerows(cvs_list)
```
#### Usage:	python interpreter - same interpreter session only
1) Call the function to merge all csvs in a folder into a python list 
```python
merged_csv_list, header = merge_csvs_into_list('myScraper/scrapedData')
```
2) Call function to join list of lists w/ list of header, then export to csv
```python
write_csv_from_list('mergedData/merged1.csv', merged_csv_list, header)
```

#### Pros:								
1) check simple code (one liners), often w/ toy data 
2) check your intuitions about data manipulation
	* ex: what does `myString[:-1]` give me when `myString = 'Hello'`?

#### Cons:								
1) not reusable or saved
2) no editor
3) inefficient when writing more than a few lines of code

### Python Workflow 2 - Use interpreter to import code from custom modules and execute code
#### Tools: command line, python interpreter, text editor
#### Code: 1 module (file)
* Instead of writing our functions in the temporary memory of the interpreter, we can write them in a csv_merge.py file somewhere
* copy and paste the CSV Merge Code into a new file csv_merge.py, just inside the PythonBasics1 directory
#### Usage: python interpreter				

2) start interpreter
```shell
python
```
3) load module into current terminal session
```python
import csv_merge
```
4) call functions from module with module namespace
```python
merged_csv_list, header = csv_merge.merge_csvs_into_list('myScraper/scrapedData')
csv_merge.write_csv_from_list('mergedData/merged2.csv', merged_csv_list, header)

```


#### Pros:					
1) Using the python interpreter to call functions can be useful if want a simple environment to try various inputs interactively and see their outputs, e.g. search engines, chatbots, question asking systems, etc
2) interactive way to import and test various modules or packages
3) Modular, Resuable

#### Cons:					
1) usage commands are not saved, often we want to save the function calls somewhere

### Python Workflow 3 - Command line to run custom modules w/ non-modular code
#### Tools: terminal + editor: 
#### Code: 1 file: function, followed by function call in csv_merge.py script
#### Usage: 	

1) move code to into csv_merge.py file dir and change the output: mergedData/merged2.csv -> mergedData/merged3.csv

2) Run file from command line
```shell
python csv_merge.py
```		

#### Pros:					
1) will both load your function and execute it (will execute everything in the .py synchronously)

#### Cons:
1) not that resuable, except in this exact use case
2) bad coding practice (not modular)
	* This is because the function is tied to the function call, they could be separate, in different files.
	* Also, from a git perspective, you should not need to edit the file that contains the function if all you are doing is changing how you are calling the function i.e. what arguments you pass it in some specific instance

### Python Workflow 4 - Command line to run code from script file w/ modular code
#### terminal + editor  
#### Code: 2 files:			
1) 1 file with functions only
2) 1 file as a 'script' file to do imports and call functions 
			* a script file is a file containing mostly commands like you would enter in the command line or in an interpreter. it allows you to chain dependencies and function calls together in a modular and resuable fashion, keeping your functions separate.

#### Usage: 				
1) make a new file called run_quotes_merge.py

2) put the calls to the function inside run_quotes_merge.py

3) change the output location: mergedData/merged3.csv -> mergedData/merged4.csv
3) Run script file from command line
```shell
python run_quotes_merge.py
```

#### Pros:					
1) Modular, Resuable 
2) often we want to call a number of commands in some specific order, and save it for later, but keep the functions separate
3) DRY - Don't Repeat Yourself 

#### Cons:					
* little bit more organization upfront










