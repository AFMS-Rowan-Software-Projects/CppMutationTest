import os
from configparser import ConfigParser

if not os.path.exists('../config.ini'):
    print ("Error: Config File does not exist")
    with open('readme.ini', 'w') as f:
        f.write('Test')
    quit()
else:
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    temp = config.options('Filenames')
	
    for x in temp:
        print(x)

  
