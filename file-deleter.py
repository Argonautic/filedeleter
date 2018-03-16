import csv
import os

"""
    Takes a csv file located at filepath, scans the column filenameColumn, adds all values to returnDict
    as keys (with value True), and returns returnDict
"""
def filenamesToDict(filepath, filenameColumn='Filenames', headersExist=True, returnDict={}):
    with open(filepath, newline='') as csvfile:
        csvReader = csv.DictReader(csvfile)
        if headersExist:
            next(csvReader)
        for row in csvReader:
            filename = row[filenameColumn]
            if filename not in returnDict:
                returnDict[filename] = True
        return returnDict

"""
    From directory starting at path, delete all files that match a key in fileDict. Deep configures whether
    To only delete from current directory or to go down all subdirectories until end of tree
"""
def deleteFiles(fileDict, path=os.getcwd(), deep=True):
    if deep:
        directories = os.walk(path)
        for directory in directories:
            dirPath = directory[0]
            files = directory[2]

            for file in files:
                filePath = f'{dirPath}/{file}'
                print(filePath)
                if filePath in fileDict:
                    os.remove(filePath)
    else:
        directory = os.listdir(path)
        for file in directory:
            print(f'{path}/{file}')
            if file in fileDict:                
                os.remove(filePath)


toDelete = filenamesToDict('to-delete.csv')
deleteFiles(toDelete, deep=False)
