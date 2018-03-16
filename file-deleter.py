import csv
import os
import argparse

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


parser = argparse.ArgumentParser(description='Delete files in this directory and subdirectories based on a .csv file')
parser.add_argument('csvPath', help='the path of the csv file to read from')
parser.add_argument('-dPath', default=os.getcwd(), help='the directory in which to start deletion (defaults to cwd)')
parser.add_argument('-n', action='store_true', help="no headers/don't skip headers in your csv file")
parser.add_argument('-s', action='store_true', help='shallow delete - only delete in directory at dPath, disregard subdirectories')

args = parser.parse_args()

# toDelete = filenamesToDict('to-delete.csv')
# deleteFiles(toDelete)
