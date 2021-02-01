'''
Our student managment system genearates a contact report in a messy CSV. 
This will strip the information that we need from the sheet and save it as
a clean CSV. This needs to be replicable if we to regenerate the report
from year to year. 

This script probably won't be particularly useful to others since it is highly
customized for cleaning up our specific report. 

When done we should get a CSV with rows formated like this:
'Last, First','Student ID','Homeroom','Contact 1','Phone #1',ect
'''

import csv
import os

curDir = os.getcwd()
oldFile = curDir+'\contacts\contacts.csv'
newFile = open('New.csv', "w")

def dataClean(filePath):
    data = [] #Buffer list 
    with open(filePath, "rt") as the_file:
        reader = csv.reader(the_file, delimiter=",")
        for line in reader:
            if line[5]:
                if line[6]:
                    if line[6][0].isdigit():
                        data.append(line[2].title())
                        data.append(line[6])
                else:
                    data.append(line[5])
            if line[5] == '':
                    if data:
                        if len(data) > 2: 
                            
                            if data[2][1].isdigit():
                                print(data[2])
                                for item in data:
                                    # print(item)
                                    newFile.write(item) 
                                    newFile.write(', ')
                                newFile.write('\n')
                    data = []
    newFile.close()     

dataClean(file)


