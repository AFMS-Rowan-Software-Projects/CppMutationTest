import re
import readline
#mutate != to ==


#Where file.txt is the file you want to mutate
file = open('EO2.cpp', 'a+')

#Where file1.txt is a copy of the file thats being mutated
with open('EO2.cpp', 'r') as input:
    with open('EO2_EqualityOperator.cpp', 'w') as output:
        for line in input:
            output.write(re.sub('!=', '==', line))
            file.close()
