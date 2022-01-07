import re
import readline
#mutate == to !=

#Where file.txt is the file you want to mutate
file = open('EO1.cpp', 'a+')

#Where file1.txt is a copy of the file thats being mutated
with open('EO1.cpp', 'r') as input:
    with open('EO1_EqualityOperator.cpp', 'w') as output:
        for line in input:
            output.write(re.sub('==', '!=', line))
            file.close()
