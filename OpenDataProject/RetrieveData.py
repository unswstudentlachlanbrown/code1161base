"""Retrieve data."""
import os

location = "nsw/bega/"


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


# def correctDirectory():
#     """Correct Dictionary."""
#     os.system("cd ..")
#     cwd = os.getcwd()
#     print(cwd)
#     print(type(cwd))

loc = os.getcwd() + "ftp.bom.gov.au/anon/gen/clim_data/IDCKWCDEA0/tables/"


def arrangeData():
    """Put all scraped data into one file."""
    def list_files():
        r = []
        for root, dirs, files in os.walk(loc):
            for name in files:
                r.append(os.path.join(root, name))
                print os.path.join(root, name)
        return r
    print list_files()


def list_files(directory):
    """List Files."""


arrangeData()
