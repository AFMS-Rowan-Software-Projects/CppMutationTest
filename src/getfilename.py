import re
import sys

filename = str(sys.argv[1])

def getFilenamesFromCMakeLists(filename):
    with open(filename) as f:
        read_data = f.read()
    iterator = re.finditer(r'[^ ]*\.cpp[)]*$', read_data, re.MULTILINE)
    hasMatches = False
    filenames = []
    for m in iterator:
        hasMatches = True
        filenames.append(m.group(0))
    if not hasMatches:
        filenames.append("No matches.")
    return filenames

print(getFilenamesFromCMakeLists(filename))
