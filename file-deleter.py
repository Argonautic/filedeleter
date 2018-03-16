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
                if file in fileDict:
                    filePath = f'{dirPath}/{file}'
                    os.remove(filePath)
    else:
        dirPath = os.listdir(path)
        for file in directory:
            if file in fileDict:
                os.remove(f'{path}/{file}')


toDelete = filenamesToDict('to-delete.csv')
deleteFiles(toDelete)
