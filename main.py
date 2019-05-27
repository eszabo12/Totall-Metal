from program import program
import os

'''
I haven't finished with this code yet-- I literally started this project 2 days ago
the aim of this document is to loop through all of the store procedures in a given
directory. for each store procedure, create a StoreProcedure object. if the object
has another store procedure called within it, then the code goes to that store 
procedure and repeats in a while loop until no remaining store procedures need to
be changed within the file. then it goes on to the next file in the directory
 
'''
def main2():
	directoryStr = "Users/Elle/Documents/TMR"
	directory = os.fsencode(directoryStr)
	for file in os.listdir(directory):
