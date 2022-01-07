import os
import sys
from configparser import ConfigParser
import shutil
from mutant_dictionary import all_mutants
from mutant_dictionary import all_mutant_keys

class GenerateMutants():

    if not os.path.exists('./config.ini'): #Config parser - From Drew's and Luke's Code
        print("Error: Config File does not exist")
        with open('config.ini', 'w', encoding="utf-8") as f:
            f.write('testing')
            sys.exit()
    else:
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        mutants = config.options('Mutants')
        filename = "../CMakeLists.txt"
        mutant_list = []
        active_mutants = []

        if os.path.exists('../mutants'):
            os.system("rm -r ../mutants/")

        for x in mutants: #Pareses config for mutants that are marked active
            if config.get('Mutants', x) == '1':
                mutant_list.append(x) #Creates list of active mutants from config file

        for x in all_mutant_keys:
            if x.lower() in mutant_list:
                active_mutants.append(all_mutants[x])

        if not os.path.exists('../mutants'):
            os.mkdir('../mutants')

        for i in active_mutants:  #Creates folders for all active mutants
            build_dir = '../mutants/' + i.get_name()
            if not os.path.exists(build_dir):
                os.mkdir(build_dir) #Creates folder
            with open(filename, "r", encoding="utf-8") as f:
                read_data = f.read()
            read_data = read_data.replace('.cpp', '_' + i.get_name() + '.cpp')
            newpath = '../mutants/' + i.get_name() + "/" + \
                      filename.replace(".txt", "_" + i.get_name() + ".txt")
            with open(newpath, "a+", encoding="utf-8") as f: #Writes CMakeLists file for mutant
                f.write(read_data)
            shutil.move('../mutants/CMakeLists_' + i.get_name() + '.txt',
                        '../mutants/' + i.get_name() + '/CMakeLists_' + i.get_name() + '.txt')
        sys.exit()
