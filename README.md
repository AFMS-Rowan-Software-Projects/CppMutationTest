#########################################
README.md Instructions
#########################################

1. Repository Location: git clone https://github.com/esspee39/PorcupinesMutator.git
2. Edit the config.ini inside of "PorcupinesMutator/src" to select the desired mutants
3. Change directory to gtest-demo and run the following commands to compile and test the selected mutants
4. Commands:
	1. cmake -S. -Bbuild
	2. cmake --build build
	3. cd build
	4. ctest -T test
5. A basic explanation of the tests will be printed to the screen to show the results of the selected mutants that were chosen to be tested.
6. To test all at once, change directory to "PorcupinesMutator/tests" and run the following command: python3 -m unittest.

#########################################
Mutants
#########################################

Each mutant is specifically labeled to outline which mutation will occur. A full list of mutants are available within the config.ini as well as
inside of "PorcupinesMutator/tests". The first part of the name is what the original code begins as, and the second part of the name is what it is being
mutated to

#########################################
Errors
#########################################

If the code fails to compile, please make sure all required software is installed and functional prior to running the tests.
Please refer to the User Manual when installing required software to run the program.