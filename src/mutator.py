import re
import os
from configparser import ConfigParser

EQUALITY_OPERATOR = 0
ARITHMETIC_OPERATOR = 1

mutant_toggle = [False, False]
mutant_append = ["_EqualityOperator", "_ArithmeticOperator"]

#edited by Luke and Drew
def read_filenames_from_config():
    if not os.path.exists('./config.ini'):
        print("Error: Config File does not exist")
        with open('config.ini', 'w') as f:
            f.write('testing')
        quit()
    else:
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        filenames = config.options('Filenames')

        for x in filenames:
            print(x)

    return filenames


def read_mutants_from_config():
    if not os.path.exists('./config.ini'):
        print("Error: Config File does not exist")
        with open('config.ini', 'w') as f:
            f.write('testing')
            quit()
    else:
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        mutants = config.options('Mutants')
        mutant_list = []

        for x in mutants:
            if config.get('Mutants', x) == '1':
                mutant_list.append(x)
        print(mutant_list)

    return mutant_list

read_mutants_from_config()
   # if False:
   #     mutant_toggle[EQUALITY_OPERATOR] = False
   # if False:
   #     mutant_toggle[ARITHMETIC_OPERATOR] = False



def mutate(filename, mutantType):
    print("Create EqualityOperator mutant")
    with open(filename, 'r+') as f:
        string_list = f.readlines()

    newfilename = filename.replace(".", mutant_append[mutantType] + ".")

    for line in string_list:
        newline = line.replace("==", "!=")
#        new_string_list.append(newline)
#    with open(newfilename + ".cc", 'w') as f:
#        for newline in new_string_list:
#            f.write('%s' % newline)
    return

def equality_operator_mutate():
    print("Creating Equality Operator Mutant...")

def select_mutant(x):
    switcher = {
        EQUALITY_OPERATOR:equality_operator_mutate
    }
    func = switcher.get(x, lambda: 'Invalid mutant ID: ' + x)
    func()

select_mutant(EQUALITY_OPERATOR)

#for file in filenames
#	for x in range(0, len(mutant_toggle)):
#            if mutant_toggle[x]:
#                        mutate(file, x)
