# POS-Terminal
A typical Point of sales terminal
typical in old fashioned Point Of Sales terminal that at the end of the day a day's worth of data is collected in plain text file. 
these text files are formatted in the form of three letter string followed by quantity of item sold.
this program extracts the lines from the bus files and takes the entries and places them into the appropriate report file for easy inventory management by the accounting department.

in effect the files bus1.txt, bus2.txt, and bus3.txt is collected from the point of sales (POS) machines.
these bus files are placed in the same directory as the classify.py program.
when classify.py program is run, it reads the bus files and places each entry into the appropriate report files.
for example when processing nus1.txt the program reads the first line which is "abc 345" and places it in the file named "abc_report.txt" if the file does not exist it is created and the entry placed in it.

classify.py was tested using Python version 2.7.17
