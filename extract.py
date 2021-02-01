import csv
import os

curDir = os.getcwd()
file = curDir+'\contacts\contacts.csv'
f = open('New.csv', "w")



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
                                    f.write(item) 
                                    f.write(', ')
                                f.write('\n')
                    data = []
    f.close()     

dataClean(file)


