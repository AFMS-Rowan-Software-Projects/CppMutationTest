include(FetchContent)
FetchContent_Declare(gtest
  QUIET
  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz
)
# configure build of googletest
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(gtest)
include(GoogleTest)

#TODO hide this in cmake module include(MutationTest) - includes MutationTest.cmake
#Custom function used to dynamically create mutated targets
function(create_mutated_target TARGET_NAME TEST_FILE CLASS_TO_MUTATE TARGET_INCLUDE_PATH)
  #execute_process()
  #TODO call python script to mutate CLASS_TO_MUTATE

  #dynamically create the cmakelists.txt with the below stuff
  add_executable(
    ${TARGET_NAME}
        ${TEST_FILE}
        ${CLASS_TO_MUTATE}
  )

  target_include_directories(
    ${TARGET_NAME}
      PRIVATE
        ${TARGET_INCLUDE_PATH}
  )
    
  target_link_libraries(
    ${TARGET_NAME}
      PRIVATE
        gtest_main #Link against gtest_main to run google tests
    )

  # automatic discovery of unit tests
  gtest_discover_tests(
    ${TARGET_NAME}
  )
endfunction()

#User calls these
create_mutated_target(test_add ../src/example.cpp example_add.cpp ../src)
create_mutated_target(test_subtract ../src/example.cpp example_subtract.cpp ../src)
#TODO add_subdirectory(mutation_tests)

