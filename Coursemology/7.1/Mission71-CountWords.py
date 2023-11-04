#Programming I
#######################
#     Mission 7.1     #
#     Process File    #
#######################
#Background
#Tom has created a text file. He would like to know the number of
#lines, words and characters in the file. He indicates that spaces 
#and end-of-line characters are also considered characters.
#Help him read the data file and perform the counting and return
#the number of lines, words and characters as a list.
#
#E.g. if your data file contains the 2 lines below
#Hello World
#I like Python Programming
#The return value should be [ 2,6,38 ]
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) The data file to be used is 'datafile.txt'
#START CODING FROM HERE
#======================
#function to process the file
def process_file(filename):
     infile = open(filename) # open the file
     lineCount = 0
     wordCount = 0
     charCount = 0
     #code to process the file and count number of lines, words and characters
     #as lineCount, wrodCount, charCount
     while True:
          file = infile.readline()
          if file == "":
               break
          else:
               lineCount += 1
          charCount += len(file)
          newfile = file.split(" ")
          wordCount += len(newfile)
               
     infile.close()          # close file
     return [lineCount,wordCount,charCount] #return the values - do not remove