import re
import sys
import os

filename = str(sys.argv[1])
current_name = "EqualityOperator"
build_dir = '../mutants/' + current_name

def makeCMakeListsForMutant(filename,mutant_name):
    with open(filename) as f:
        read_data = f.read()
    read_data = read_data.replace('.cpp', '_' + mutant_name + '.cpp')
    return read_data

new_filename = filename.replace(".txt", "_" + current_name + ".txt")
new_filename = new_filename.replace("../", "")

if not (os.path.exists('../mutants')):
    os.mkdir('../mutants')
    if not (os.path.exists(build_dir)):
            os.mkdir(build_dir)

with open(build_dir + "/" + new_filename, 'w+') as f:
    f.write(makeCMakeListsForMutant(filename,current_name))
