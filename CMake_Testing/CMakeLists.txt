message("Running CMakeLists.txt test file")
execute_process(
	COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/makenewcmakelist.py ${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists.txt
)
message("Python script has run?")
add_subdirectory(mutants)
