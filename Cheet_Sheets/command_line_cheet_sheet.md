# Command Line Cheet Sheet

## NAVIGATION:
pwd (print working directory)
cd  (change directory)
cd .. (move back to parent directory)
cd /Volumes/Macintosh\ HD/  (deal with folders that have spaces in them)
cd "/Volumes/Macintosh HD/" (deal with folders that have spaces in them)
ls (list files in current directory)
ls -a (& show hidden files)
ls -l (& show files as vertial list )
ls -la (& both -a and -l tags combined)
clear
history

## DEALING W/ FILES & FOLDERS:
Create new or edit existing file:
			quit with
emacs text.txt  	ctrl+cmd+x 
nano test.txt		ctrl+x
vi test.txt			:q return
then answer y/n to save prompt and then hit enter

mkfile 1g test.abc

cat test.txt
head test.txt (print first 10 lines - tail does last 10)
head -n30 test.txt (print first 30 lines of file)

cp or ditto
cp test.txt test2.txt (make a copy of a file 1 at file 2 path)
mv test.txt folder (move a file into a folder)


## Other: 
uptime  (computer uptime)
killall SystemUIServer (sometimes this process becomes a bit runaway, you can safely kill it and it will restart instantly)
yes (set system load 100% with terminal - load testing)
top (so system top processes)
top -o cpu (Order by CPU usage)

cat test.txt ('vomit' all contents of file into the termial) 
head -n30
uptime

python -m SimpleHTTPServer 8000 (start a http server in some folder, then direct browser to http://localhost:8000/)
this works basically the same way as python jyputer notebook we may see later.
ctrl+c (cancel a currently running terminal process - works for most things like servers or files that process for a while, but does not work text editors, see command line editors exit commands above)


ping -c 10 www.apple.com (check latency to some server)

say "This Mac runs OS X, not OS ex" (mac will speak the text aloud, can read from a text file.)
say -f /path

