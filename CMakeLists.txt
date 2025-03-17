cmake_minimum_required(VERSION 3.22)

# Setup project
project(LwLibPROJECT)

if(NOT PROJECT_IS_TOP_LEVEL)
    add_subdirectory(lwpkt)
else()
    enable_testing()
    add_executable(${PROJECT_NAME})
    target_sources(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/dev/main.c
        ${CMAKE_CURRENT_LIST_DIR}/libs/lwrb/src/lwrb/lwrb.c
        ${CMAKE_CURRENT_LIST_DIR}/examples/example_lwpkt.c
        ${CMAKE_CURRENT_LIST_DIR}/examples/example_lwpkt_evt.c
        ${CMAKE_CURRENT_LIST_DIR}/test/lwpkt_test.c
    )
    target_include_directories(${PROJECT_NAME} PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/dev
        ${CMAKE_CURRENT_LIST_DIR}/libs/lwrb/src/include
    )

    # Add subdir with lwpkt and link to project
    set(LWPKT_OPTS_FILE ${CMAKE_CURRENT_LIST_DIR}/dev/lwpkt_opts.h)
    add_subdirectory(lwpkt)
    target_link_libraries(${PROJECT_NAME} PUBLIC lwpkt)

    # Add compile options to the library, which will propagate options to executable through public link
    target_compile_definitions(lwpkt PUBLIC WIN32 _DEBUG CONSOLE LWPKT_DEV)
    target_compile_options(lwpkt PUBLIC -Wall -Wextra -Wpedantic)
    target_include_directories(lwpkt PUBLIC ${CMAKE_CURRENT_LIST_DIR}/libs/lwrb/src/include)

    # Add test
    add_test(NAME Test COMMAND $<TARGET_FILE:${CMAKE_PROJECT_NAME}>)
endif()