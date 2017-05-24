import os


def recursiveFileSearch(scope):
    """Search through a directory recursively for folders in that directory.

    Returns a list of lists that has each weather station and it's directory.
    e.g. [['bega', '/australia/nsw/bega'], ['ger','/australia/qld/ger'], ...]
    """
    # sub = subFolderList  ///  n = name
    print('runningRecFunc')
    sub = [os.path.abspath(n) for n in os.listdir(scope) if os.path.isdir(n)]
    if sub == []:
        print('\nRunning the end case\n')
        return [scope.split('/')[-2], scope]
    else:
        print('\nRunning the recursive case\n')
        folderList = []
        for folder in sub:
            print(scope + folder + '/')
            folderList.append(recursiveFileSearch(folder + '/'))
        return folderList


print ("\n\nHere's the end result:\n\n" + str(recursiveFileSearch('.')))
