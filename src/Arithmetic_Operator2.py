import re
import readline
#Mutate / to *

#Where file.txt is the file you want to mutate
file = open('AO2.cpp', 'a+')

#Where file1.txt is a copy of the file thats being mutated
with open('AO2.cpp', 'r') as input:
    with open('AO2_ArithmeticOperator.cpp', 'w') as output:
        for line in input:
            output.write(re.sub('[/]([^/*%+-])', '*', line))
            file.close()
