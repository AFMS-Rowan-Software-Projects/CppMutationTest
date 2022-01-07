import os
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)
mutants = config.options('Mutants')
mutant_list = []

for x in mutants:
    if config.get('Mutants',x) == '1':
        mutant_list.append(x)
print(mutant_list)

 
