import csv
import os
import argparse

"""
    Takes a csv file located at filepath, scans the column filenameColumn, adds all values to returnDict
    as keys (with value True), and returns returnDict
"""
def filenamesToDict(filepath, filenameColumn='Filenames'):
    returnDict = {}

    with open(filepath, newline='') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            filename = row[filenameColumn]
            if filename not in returnDict:
                returnDict[filename] = True
        return returnDict


"""
    Remove an individual file, according to fileDict. Blacklist is a boolean that controls whether or not fileDict
    contains the files to remove (blacklist=True) or the files to keep (blacklist=False)
"""
def deleteFile(file, fileDict, blacklist):
    if blacklist:
        if file in fileDict:
            os.remove(file)
    else:
        if file not in fileDict:
            os.remove(file)

"""
    From directory starting at path, delete all files that match a key in fileDict. Deep configures whether
    To only delete from current directory or to go down all subdirectories until end of tree
"""
def deleteFiles(fileDict, path=os.getcwd(), blacklist=True, deep=True):
    if deep:
        directories = os.walk(path)
        for directory in directories:
            dirPath = directory[0]
            files = directory[2]

            for file in files:
                deleteFile(f'{dirPath}/{file}', fileDict, blacklist)
    else:
        directory = os.listdir(path)
        for file in directory:
            deleteFile(f'{path}/{file}', fileDict, blacklist)


parser = argparse.ArgumentParser(description='Delete files in this directory and subdirectories based on a .csv file')
parser.add_argument('csvPath', help='the path of the csv file to read from')
parser.add_argument('-dPath', default=os.getcwd(), help='the directory in which to start deletion (defaults to cwd)')
parser.add_argument('-cName', default='Filenames', help='the name of the csv column that identifies filenames (defaults to "Filenames")')
parser.add_argument('-w', action='store_false', help='whitelist - keep only files listed in csv and delete everything else')
parser.add_argument('-s', action='store_false', help='shallow delete - only delete in directory at -dPath, disregard subdirectories')

args = parser.parse_args()

if args.csvPath:
    toDelete = filenamesToDict(args.csvPath, args.cName)
    deleteFiles(toDelete, args.dPath, args.w, args.s)
