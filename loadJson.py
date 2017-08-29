import json

def loadJson(pathToFile):
    with open(pathToFile, encoding = 'utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data

def dumpJson(pathToFile, data):
    fName = pathToFile
    with open(fName, 'w') as jsonFile:
        jsonFile.write(json.dumps(data))
    print("Updated {0}".format(fName))
