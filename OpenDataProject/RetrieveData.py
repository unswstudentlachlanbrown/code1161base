"""Retrieve data."""
import os
import pandas as pd
import time
# import matplotlib as mpl

# Useful in the case that this is expanded to other states of Australia.
location = "nsw/"
stateList = ["nsw"]


def downloadData(location):
    """Download data."""
    # See my week 11 medium post for a detailed explanation of these flags
    flags = "--no-verbose --no-parent --recursive --level={lvl}"
    # The url of the directory that contains all the useful data
    url = "ftp://ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"
    # Calls a linux terminal command to download the data
    os.system("wget " + flags.format(lvl="5") + " " + url + location)


# Path to location of important files downloaded.
loc = os.getcwd() + "/ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"


def flattenList(initialList):
    """Flatten a list (replaces all items in inner lists with the items)."""
    flatList = []
    for item in initialList:
        if isinstance(item, list):
            # Recursively searches through the list found within the list and
            # extends the current list with the items found within the smaller
            # list. The 'extend' method is the key here, as it merges two lists
            # without having the additional list as an item within the other
            # list as the 'append' method would.
            flatList.extend(flattenList(item))
        elif isinstance(item, tuple):
            # Same as above, except ensuring that the item is a list when
            # recursively searched through.
            flatList.extend(flattenList(list(item)))
        else:
            # Appends any found items to the list.
            flatList.append(item)
    return flatList


def removeDuplicates(dupedList):
    """Remove duplicates from list.

    Although this function is no longer needed (it was a workaround for a
    bug that I've fixed) I've kept it in in case it's needed in the future
    especially as it is likely it could be used.
    """
    count = 0
    uniqueList = []

    # A while loop was used to avoid issues incurred with running a for loop
    # on a list that was being editted within the loop
    while count < len(dupedList):
        currentItem = dupedList[count]
        uniqueList.append(currentItem)
        dupedList.remove(currentItem)

    return uniqueList


def listFiles(loc):
    """Make a list of all file locations."""
    directories = []
    # The following loops thorugh all subfolders and files within loc
    for root, dirs, files in os.walk(loc):
        for name in files:
            # Ensures that it's only picking up the csv files
            if name[-4:] == ".csv":
                directories.append(os.path.join(root, name))
    return directories


def removeCurrentDirectory(directory):
    """Remove the cwd from a given directory."""
    return str(directory)[len(str(os.getcwd()))+1:]


def readFromCSV(directory):
    """Return a pandas dataframe from a csv file."""
    # Read in dataframe from csv file
    df = pd.read_csv(removeCurrentDirectory(directory))
    # Rename columns appropriately
    df.columns = ["station", "date", "evapotranspiration", "rain",
                  "pan_evaporation", "max_temp", "min_temp", "max_humidity",
                  "min_humidity", "wind_speed", "solar_radiation"]
    # Removes all the non-data rows
    df = df[df["station"] == df["station"][12]]
    return df


def arrangeData(loc):
    """Put all scraped data into one file."""
    directoryList = []

    # Flattens and removes duplicates from the list of file directories
    # It loops through the states to reduce RAM and CPU overloading
    for state in stateList:
        directoryList = listFiles(loc)
        dataFrameList = []
        print directoryList
        for csvFile in directoryList:
            dataFrameList.append(readFromCSV(csvFile))
        print dataFrameList
    masterDataFrame = pd.concat(dataFrameList)
    return masterDataFrame


def finishedCSV():
    """Determine whether the csv file is already present."""
    exceptionRaised = False
    try:
        # Tries to open the file
        open('weatherDataNSW.csv')
    except Exception:
        exceptionRaised = True

    # Returns True if present and False if not
    return not exceptionRaised


def alreadyPresentQuestion(question, csv='CSV', both='BOTH',
                           neither='NEITHER'):
    """Question user's motives if files are present and run the functions."""
    running = True
    while running:
        userInput2 = raw_input(question)
        if userInput2.upper() == csv:
            print "This will most likely take some time."
            print "Beginning csv updating process..."
            time.sleep(3)
            mainDataFrame = arrangeData(loc)
            print mainDataFrame
            print "Beginning saving to csv process..."
            time.sleep(3)
            mainDataFrame.to_csv('weatherDataNSW.csv')
            print "Finished!"
            time.sleep(1)
            print "Quitting in process..."
            running = False
            break
        elif userInput2.upper == both:
            print "This will most likely take some time."
            print "Beginning file downloading process..."
            time.sleep(3)
            downloadData(location)
            print "Beginning csv updating process..."
            time.sleep(3)
            mainDataFrame = arrangeData(loc)
            print mainDataFrame
            print "Beginning saving to csv process..."
            time.sleep(3)
            mainDataFrame.to_csv('weatherDataNSW.csv')
            print "Finished!"
            time.sleep(1)
            print "Quitting in process..."
            running = False
            break
        elif userInput2.upper == neither:
            print "Quitting in process..."
            running = False
            break
        else:
            print "I didn't quite understand you there."
            print "Could you type in a Y for yes or an N for no?"


def downloadLocationFile():
    """Download the location data file."""
    # See my week 11 medium post for a detailed explanation of these flags
    flags = "--no-verbose --no-parent"
    # The url of the directory that contains the useful data
    url = "ftp://ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"
    # Calls a linux terminal command to download the data
    os.system("wget " + flags.format(lvl="5") + " " + url + "stations_db.txt")


def main():
    """Deal with user interface and running other functions."""
    running = True
    while running:
        userInput = raw_input("Would you like to download the database? [Y/N]")
        if userInput.upper() == "Y" or userInput.upper() == "YES":
            if listFiles(loc) != [] and finishedCSV():
                print "There's already a completed csv present."
                print "You can either update the csv with the current data,"
                print "update both the data and the csv, or neither."
                question = "What do you want to do? [CSV/BOTH/NEITHER]"
                alreadyPresentQuestion(question, csv='CSV', both='BOTH',
                                       neither='NEITHER')
                running = False
                break
            elif listFiles(loc) != []:
                print "There's already some downloaded files present."
                print "You can either update the csv with the current data,"
                print "or update both the data and the csv."
                question = "What do you want to do? [CSV/BOTH]"
                alreadyPresentQuestion(question, csv='CSV', both='BOTH')
                running = False
                break
            elif finishedCSV():
                print "There's already a completed csv present."
                print "You can either update the csv with downloaded data,"
                print "or decide to cancel now."
                question = "Do you still want to update? [Y/N]"
                alreadyPresentQuestion(question, both='Y', neither='N')
                running = False
                break
            else:
                print "This will most likely take some time."
                print "Beginning file downloading process..."
                time.sleep(3)
                downloadData(location)
                print "Beginning csv updating process..."
                time.sleep(3)
                mainDataFrame = arrangeData(loc)
                print mainDataFrame
                print "Beginning saving to csv process..."
                time.sleep(3)
                mainDataFrame.to_csv('weatherDataNSW.csv')
                print "Finished!"
                time.sleep(1)
                print "Quitting in process..."
                running = False
                # Fake return to skip the downloading of the location data
                return ''
        elif userInput.upper == "N" or userInput.upper() == "NO":
            print "Quitting in process..."
            running = False
            break
        else:
            print "I didn't quite understand you there."
            print "Could you type in a Y for yes or an N for no?"
    downloadLocationFile()


# print "DATAFRAMES:"
# mainDataFrame = arrangeData(loc)
# print mainDataFrame
# mainDataFrame.to_csv('weatherDataNSW.csv')

main()
