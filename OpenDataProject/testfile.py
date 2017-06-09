import os
print os.getcwd()
for root, dirs, files in os.walk(os.getcwd()):
    print root
    print dirs
    print files









# for subfolder in dirs:
#    directories.append(listFiles(os.path.join(root, subfolder)))

def findSpectLetterValue(spectLetter):
    letters = ['M', 'K', 'G', 'F', 'A', 'B', 'O']
    letterOrder = zip(range(len(letters)), letters)
    for letter in letterOrder:
        if letter[1] == spectLetter[0]:
            return (letter[0]*10 + int(spectLetter[1]))

hygData['spectNumber'] = [findSpectLetterValue(spectValue) for spectValue in hygData['spect']]
y = hyg_data['spect']
