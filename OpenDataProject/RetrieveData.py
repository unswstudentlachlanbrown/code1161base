"""Retrieve data."""
import os
import pandas as pd

location = "nsw/bega/"
stateList = ["nsw"]


def downloadData(location):
    """Download data."""
    flags = "--no-verbose --no-parent --recursive --level={lvl}"
    url = "ftp://ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"
    os.system("wget " + flags.format(lvl="5") + " " + url + location)


def recursiveFileSearch(scope):
    """Search through a directory recursively for folders in that directory.

    Returns a list of lists that has each weather station and it's directory.
    e.g. [['bega', '/australia/nsw/bega'], ['ger','/australia/qld/ger'], ...]
    """
    subFolderList = [name for name in os.listdir(scope) if os.path.isdir(name)]
    if subFolderList == []:
        currentWord = ''
        for char in scope:
            if char == '/':
                currentWord = ''
            else:
                currentWord += char
        return [currentWord, scope]
    else:
        for folder in subFolderList:
            return recursiveFileSearch(scope + '/' + folder)


# downloadData(location)

# dataDir = "/ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"
# loc = os.getcwd() + "/OpenDataProject" + dataDir
loc = os.getcwd() + "/ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"


def flattenList(initialList):
    """Flatten a list (replaces all items in inner lists with the items)."""
    flatList = []
    for item in initialList:
        if isinstance(item, list):
            flatList.extend(flattenList(item))
        elif isinstance(item, tuple):
            flatList.extend(flattenList(list(item)))
        else:
            flatList.append(item)
    return flatList


def removeDuplicates(dupedList):
    """Remove duplicates from list."""
    count = 0
    uniqueList = []

    while count < len(dupedList):
        currentItem = dupedList[count]
        uniqueList.appen(currentItem)
        dupedList.remove(currentItem)

    return uniqueList


def listFiles(loc, fileCount):
    """Make a list of all file locations."""
    r = []
    for root, dirs, files in os.walk(loc):
        print root
        for name in files:
            if name[-4:] == ".csv":
                r.append(os.path.join(root, name))
        for subfolder in dirs:
            print "subfolda :O"
            r.append(listFiles(os.path.join(root, subfolder), fileCount))
    return r


def removeCurrentDirectory(directory):
    """Remove the cwd from a given directory."""
    print os.getcwd()
    return str(directory)[len(str(os.getcwd()))+1:]


def readFromCSV(directory):
    """Return a pandas dataframe from a csv file."""
    df = pd.read_csv(removeCurrentDirectory(directory))
    df.columns("station", "date", "evapotranspiration", "rain",
               "pan_evaporation", "max_temp", "min_temp", "max_humidity",
               "min_humidity", "wind_speed", "solar_radiation")
    df = df[df["station"] == df["station"][12]]


def arrangeData(location):
    """Put all scraped data into one file."""
    def listFiles(loc):
        """Make a list of all file locations."""
        r = []
        for root, dirs, files in os.walk(loc):
            for name in files:
                r.append(os.path.join(root, name))
            for subfolder in dirs:
                r.append(listFiles(os.path.join(root, subfolder)))
        return r

    directoryList = []

    # Flattens and removes duplicates from the list of file directories
    # It loops through the states to reduce RAM and CPU overloading
    for state in stateList:
        flatList = flattenList(listFiles(location, 0))
        directoryList.extend(removeDuplicates(flatList))


# arrangeData(loc)
githubURL = "/home/baptiste/code1161base/OpenDataProject"
csvData = "/ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/nsw/bega/bega-200901.csv"
print readFromCSV(githubURL + csvData)
